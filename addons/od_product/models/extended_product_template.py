import base64
from odoo import api, models, fields
from odoo.http import request
from odoo.addons.website.models.website import slugify

'''
    This extends the ProductTemplate model functionalities by adding two fields and 
    their respective business logic.
'''
class ExtendedProductTemplate(models.Model):
    _inherit = "product.template"
    
    slug = fields.Char(string = "slug", compute = "_compute_slug")
    additional_barcode = fields.Image(string = "Additional barcode", compute = "_compute_additional_barcode")
    
    '''
        Computes a slug based on the name of a record.
    '''
    @api.depends("name")
    def _compute_slug(self):
        for record in self:
            record.slug = slugify(record.name)
    
    '''
        Computes a EAN13 barcode based on the id of a record using odoo's internal api.
    '''
    def _compute_additional_barcode(self):
        for record in self:
            image = request.env['ir.actions.report'].barcode(barcode_type = "EAN13", value = str(record.id), humanreadable = 1)
            record.additional_barcode = base64.b64encode(image)