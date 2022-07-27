odoo-bin -d database -u module

python ../odoo-bin -u "real-estate"

SOME USEFUL STEPS IN CREATING PAYROLL

1) first we create a menu in munu_view.xml
- the menu expects an action
- however calling it only allows server actions
2) we create a server action in view.xml
- alternatively we call a wizard action if we need to pass some arbitary values
- both require an action on the model specified: this is a function in hr_print.py model
- the function then calls the report using .report_action(data)
3) we create the report action in view.xml
- it must specify a paperformat or null
- it calls a qweb report in 
4) we create a qweb report in payroll_report_template.xml

KNOWN ISSUES

odoo 15 enterprise .report_action(data) not working we need a work around since
the implementation relies on this functionality