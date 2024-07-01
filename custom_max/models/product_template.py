from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    package = fields.Char(string="Package")
    sub_category = fields.Char(string="Sub Category")
    quantity = fields.Float(string="Quantity")
    sub_quantity = fields.Float(string="Sub Quantity")
    issued_quantity = fields.Float(string="Issued Quantity")
    total_quantity = fields.Float(string="Total Quantity")
    remark = fields.Text(string="Remark")
    part_number = fields.Char(string="Part Number")
    type_no = fields.Char(string="Type No")
    part_name = fields.Char(string="Part Name")
    # value_ids = fields.Float(string="Value" , invisible="1")

    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = ['|', ('part_number', operator, name), ('sub_category', operator, name)]
        return self.search(domain + args, limit=limit).name_get()
