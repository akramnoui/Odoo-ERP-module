# -*- coding: utf-8 -*-

from xml.dom import ValidationErr
from odoo import models, fields, api 
from dateutil.relativedelta import relativedelta

class demande(models.Model):
    _name = 'esi.demande'
    _inherit = ["mail.thread" , "mail.activity.mixin"]
    _description = "modele de demande"
    f_name = fields.Char('First Name')
    l_name = fields.Char('Last Name')
    adress = fields.Char('Adresse e-mail')
    matricule = fields.Char('Matricule')
    birthday = fields.Date()
    diplome_id = Many2one=('esi.diplome')
    file = fields.Binary(string='file', attachment=True)
    file_name = fields.Char("File Name")
    current_user = fields.Many2one('res.users','Current User', default=lambda self: self.env.user)
    statut = fields.Selection([('en attente' , 'En attente') , ('approuvée', 'Approuvée') , ('manquant' , 'Manquant') ] , default='En attente')
    active = fields.Boolean("Active", default=True)
        


    @api.constrains('file')
    def _check_file(self):
        if str(self.file_name.split(".")[1]) != 'pdf' :
                raise ValidationErr("Cannot upload file different from .pdf file")
        
        # sexe = fields.Selection([('Male' , 'male') , ('Female'), ('female')])
    def _archive(self, max_age_days=1):
        domain = [
            ('active', '=', True),
          #  ('create_date', '<', fields.Datetime.now() - relativedelta(days=max_age_days)),
        ]
        self.search(domain).unlink()
    
