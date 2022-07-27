from odoo import models, fields, api
from odoo.exceptions import UserError

class HrPrintModel(models.TransientModel):
    _name = "nursery.hr"

    wcif_rate = fields.Float(string="WCIF Rate", required=True)
    zimdef_rate = fields.Float(string="ZIMDEF Rate", digits=(12,4), default=0.005)

    def print_nssa_remittance_report(self):
        self.ensure_one()
        wcif = self.read()[0]["wcif_rate"]
        if(wcif <= 0):
            raise UserError("WCIF_RATE must be greater than 0")
        payslips = self.env["hr.payslip"].search([])
        company = self.env["res.company"].search([])[0]
        nps = 0.09
        total_wages = 0
        nps_contributions = 0
        wcif_contributions = 0

        for payslip in payslips:
            total_wages += payslip.contract_id.wage

        for payslip in payslips:
            nps_contributions += (payslip.contract_id.wage * nps)
        
        for payslip in payslips:
            wcif_contributions += (payslip.contract_id.wage * wcif)
        
        data = {
            "wcif": wcif,
            "employees_count": len(payslips),
            "total_wages": total_wages,
            "wcif_contributions": wcif_contributions,
            "nps_contributions": nps_contributions,
            "contribution_date": payslips[0].date_from,
            "employer": company.name,
            "address": company.partner_id.street + ", " + company.partner_id.city,
            "contact": company.phone
        }
        return self.env.ref('nursery.action_nssa_remittance_report').report_action(None, data=data)

    def print_nssa_form_report(self):
        payslips = self.env["hr.payslip"].search([])
        # return self.env.ref('nursery.action_nssa_report').report_action(None, data=payslips)
        return self.env.ref('nursery.action_nssa_form_report').report_action(payslips)

    def print_zimra_form_report(self):
        payslips = self.env["hr.payslip"].search([])
        company = self.env["res.company"].search([])[0]
        total_wages = 0
        gross_paye = 0

        for payslip in payslips:
            total_wages += payslip.contract_id.wage

        for payslip in payslips:
            for line in payslip.line_ids:
                if(line.code == 'PAYE' or line.name == "P.A.Y.E"):
                    gross_paye += line.amount

        aids = gross_paye * 0.03
        
        data = {
            "employer": company.name,
            "month": payslips[0].date_from.strftime("%B"),
            "address": company.partner_id.street + ", " + company.partner_id.city,
            "city": company.partner_id.city,
            "country": company.partner_id.company_id.name,
            "contact": company.phone,
            "email": company.email,
            "bpn": company.company_registry,
            "total_wages": total_wages,
            "employees_count": len(payslips),
            "gross_paye": gross_paye * -1,
            "aids": aids * -1,
            "total_tax": aids + gross_paye,
            "period": payslips[0].date_from.strftime("%m/%d/%Y") + " - " + payslips[0].date_to.strftime("%m/%d/%Y"),
            "due_date": str(int(payslips[0].date_to.strftime("%m")) + 1) + payslips[0].date_to.strftime("/%d/%Y")
        }

        print(data)
        return self.env.ref('nursery.action_zimra_p2_report').report_action(None, data=data)

    def print_payroll_summary_report(self):
        wcif = self.read()[0]["wcif_rate"]
        zimdef = self.read()[0]["zimdef_rate"]
        company = self.env["res.company"].search([])[0]
        if(wcif <= 0):
            raise UserError("WCIF_RATE must be greater than 0")
        payslips = self.env["hr.payslip"].search([])
        # payslips = self.env["hr.payslip"].search([("status", "=", "done")])

        # variable instantiated here
        basic = 0
        allowances = 0
        paye = 0
        aids = 0
        nssa = 0
        nec = 0
        wcif_contributions = 0
        gross = 0
        net = 0

        for payslip in payslips:
            basic += payslip.contract_id.wage
            wcif_contributions += (payslip.contract_id.wage * wcif)
            zimdef += (payslip.contract_id.wage * 0.005)
            for line in payslip.line_ids:
                if(line.category_id.name == "Allowance" or line.category_id.code == "ALW"):
                    allowances += line.amount
                if(line.code == "PAYE" or line.name == "P.A.Y.E"):
                    paye += line.amount
                if(line.code == "AIDS" or line.name == "AIDS Levy"):
                    aids += line.amount
                if(line.code == "NSSA" or line.name == "NSSA"):
                    nssa += line.amount
                if(line.code == "NEC" or line.name == "NEC"):
                    nec += line.amount
                if(line.code == "GROSS" or line.name == "Gross"):
                    gross += line.amount
                if(line.code == "NET" or line.name == "Net"):
                    net += line.amount
        
        deductions = paye + aids + nssa + nec
        emp_contributions = nssa + nec + wcif_contributions + zimdef
        
        data = {
            "basic": basic, "allowances": allowances, "paye": -paye, "aids": float("{:.3f}".format(-aids)),
            "nssa": float("{:.3f}".format(-nssa)), "nec": float("{:.3f}".format(-nec)), "wcif_contributions":  float("{:.3f}".format(wcif_contributions)), "zimdef":  float("{:.3f}".format(zimdef)),
            "gross": gross, "net": net, "deductions": -deductions, "emp_contributions": float("{:.3f}".format(emp_contributions)),
            "company": company.name, "period": payslips[0].date_from.strftime("%m/%d/%Y") + " TO " + payslips[0].date_to.strftime("%m/%d/%Y"),
            "entries": len(payslips)
        }
        # print(data)
        return self.env.ref('nursery.action_payroll_summary_report').report_action(None, data=data)



    def print_payroll_payout_report(self):
        payslips = self.env["hr.payslip"].search([])
        return self.env.ref('nursery.action_payroll_payout_report').report_action(payslips)



class HrPrintRemmitanceModel(models.AbstractModel):
    _name = "report_nursery_action_nssa_remittance_report"

    def _get_report_values(self, docids, data=None):
        pass
