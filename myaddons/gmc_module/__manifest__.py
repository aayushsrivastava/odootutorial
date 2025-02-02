{
	'name': 'GMC Module',
    'summary' : "Employee Group Mediclaim",
	'description' : """Employee Group Mediclaim""",
	'author' : "ISGEC IT",
	'license' : "AGPL-3",
	'website' : "www.isgec.com",
	'category' : 'Uncategorized',
	'version' : '12.0.1.0.0',
	'depends' : ['base','hr_module'],
	'data' : [
			'security/groups.xml',
			'views/gmcmodule_policytable.xml',
			'views/gmcmodule_employeetable.xml',
			'views/gmcmodule_membertable.xml',
			'security/ir.model.access.csv',
			'security/security.xml',
			'data/sequence.xml',
			'views/report_template.xml',
			'views/report_view.xml',
			'wizard/gmc_details_wizard_view.xml'
			],	
}
