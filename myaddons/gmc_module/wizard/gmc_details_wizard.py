from odoo import api,fields,models,_
from datetime import datetime
import xlwt 
import StringIO
import cStringIO
import base64


class gmc_details_wizard(models.TransientModel):
    _name='gmc.details.wizard'
    gmc_policy_id = fields.Many2one('gmcmodule.policytable',string='Policy Type')
    
    def button_excel(self, data, context=None):
        try:
            import xlwt
            from xlwt import *
        except Exception, e:
            raise wizard.except_wizard(_('User Error'), _('Please Install xlwt Library.!'))
        filename = 'GMC Details.xls'
        string = 'Employee Details'
        wb = xlwt.Workbook(encoding='utf-8')
        worksheet = wb.add_sheet(string)
        style_value = xlwt.easyxf('font: bold on ,colour_index 0x36;' "borders: top double , bottom double ,left double , right double;")
        style_header = xlwt.easyxf('font: bold on ,colour_index black;' "borders: top double , bottom double ,left double , right double;")
        style = XFStyle()
        fnt = Font()
        fnt.colour_index = 0x36
        fnt.bold = True
        fnt.width = 256 * 30
        style.font = fnt
        style1 = XFStyle()
        fnt = Font()
        fnt.colour_index = 0x86
        fnt.bold = True
        fnt.width = 256 * 30
        style1.font = fnt
       
        worksheet.write(0,0,'Sl.No',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,1,'EmpCode',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,2,'Employee Name',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,3,'Sum Insured(in Lac)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,4,'Prorata Premium in Rs.',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))

        if self.gmc_policy_id:
            self._cr.execute("""SELECT id FROM gmcmodule.employeetable
                    WHERE policytype_id = %s""",(self.gmc_policy_id.id))
            employee_ids = self._cr.fetchall()
            b = 1
            cnt = 0
            for thisemployee_id in employee_ids:
                b+=1
                cnt+=1
                thisemployee_obj=self.env['gmcmodule.employeetable'].browse(thisemployee_id[0])
                worksheet.write(b, 0, cnt)
                worksheet.write(b, 1, thisemployee_obj.cardno or '')
                worksheet.write(b, 2, thisemployee_obj.name or '')
                worksheet.write(b, 3, thisemployee_obj.suminsured or '')
                worksheet.write(b, 4, thisemployee_obj.proratapremium or '')

        fp = cStringIO.StringIO()
        wb.save(fp)
        out = base64.encodestring(fp.getvalue())
        view_gmcreport_id=self.env['view.gmcreport'].create({'file_name':out,'datas_fname':filename})
        return {
        'res_id'   :view_gmcreport_id.id,
        'name'     :'GMC Details Report',
        'view_type':'form',
        'view_mode':'form',
        'res_model':'view.gmcreport',
        'view_id'  : False ,
        'type'     :'ir.actions.act_window',
    }
      
class view_gmcreport(models.TransientModel):
    _name = 'view.gmcreport'
    _rec_name = 'datas_fname'
    datas_fname=fields.Char('File Name', size=256)
    file_name=fields.Binary('Report')
    
