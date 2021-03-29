# -*- coding: utf-8 -*-

{
    'name': 'Print Journal Entries Report in Odoo',
    'version': '13.0.0.0',
    'category': 'Account',
    'summary': 'Allow to print pdf report of Journal Entries.',
    'description': """
    

    
""",
   
    'author': ' ',
    'website': ' ',
    'depends': ['base','account'],
    'data': [
            'report/report_journal_entries.xml',
            'report/report_journal_entries_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    "images":[""],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
