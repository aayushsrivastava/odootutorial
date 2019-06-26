{
	'name': 'GMC Module',
    'summary' : "Employee Group Mediclaim",
	'description' : """Employee Group Mediclaim""",
	'author' : "ISGEC IT",
	'license' : "AGPL-3",
	'website' : "www.isgec.com",
	'category' : 'Uncategorized',
	'version' : '12.0.1.0.0',
	'depends' : ['base'],
	'data' : [
		     'security/groups.xml',
		     'views/gmcmodule_policytable.xml',
			'views/gmcmodule_employeetable.xml',
	         'security/ir.model.access.csv',
	         ],	
}
