from odoo import models , fields, api 

class Demande(models.Model): 
    f_name = fields.Char('First Name')
    l_name = fields.Char('Last Name')
    sexe = fields.Selection([('Male' , 'male') , ('Female'), ('female')])
    adress = fields.Char()
    birthday = fields.Date()
