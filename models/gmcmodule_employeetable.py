from odoo import models, fields, api

class GmcModuleEmployeeTable(models.Model):
	_name = 'gmcmodule.employeetable'
	
	cardno = fields.Char('Card No.', required=True)
	name = fields.Char('Name', required=True)
	dateofjoining = fields.Date('Date of Joining', required=True)
	policytype_id = fields.Many2one('gmcmodule.policytable', ondelete='set null', string='Policy Type', index=True)
	suminsured = fields.Float('Sum Insured(in Lac)', required=True)	
	proratapremium = fields.Float('Prorata Premium in Rs.', compute='_compute_premium', store=True)
	coveringdays = fields.Integer('Covering Days', required=True)
	startdate = fields.Date('Start Date', related='policytype_id.startdate', store=True)
	enddate = fields.Date('End Date', related='policytype_id.enddate', store=True)	
	
	@api.depends('coveringdays', 'policytype_id', 'suminsured')
	def _compute_premium(self):
		for record in self:
			record.proratapremium = ((record.policytype_id.premium)/365) * record.coveringdays * record.suminsured

	@api.multi
	def name_get(self):
		res = []
		for record in self:
			name = record.name
			if record.cardno:
 				name = record.cardno + "-" + record.name
			res.append((record.id, name))
		return res

