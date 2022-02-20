# -*- coding: utf-8 -*-

# from typing_extensions import Self
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
    annee = fields.Date(string='Année d''obtention')
    diplome_id = fields.Many2one('esi.diplome')
    file = fields.Binary(string='Attachement', attachment=True)
    file_name = fields.Char("File Name")
    type = fields.Selection([('master', 'Master'), ('Ingénieur','ingénieur')])
    specialite = fields.Selection([('SIT' , 'SIT') , ('SIQ', 'SIQ') , ('SIL' , 'SIL') , ('SID','SID') ] , string = "specialité")
    statut = fields.Selection([('en attente' , 'En attente') , ('approuvée', 'Approuvée') , ('manquant' , 'Manquant') ] , default= "En attente")
    active = fields.Boolean("Active", default=True)
        


    @api.constrains('file')
    def _check_file(self):
        if str(self.file_name.split(".")[1]) != 'pdf' :
                raise ValidationErr("Cannot upload file different from .pdf file")
        
        # sexe = fields.Selection([('Male' , 'male') , ('Female'), ('female')])
    @api.model
    def get_default_auType(self):
     default_auType = 'En attente'
     return default_auType

    auType = fields.Selection(selection=[('type1', 'Type 1'),('type2', 'Type 2'),], string='Type', )  
    def _archive(self, max_age_days=90):
        domain = [
            ('active', '=', True),
            ('create_date', '<', fields.Datetime.now() - relativedelta(days=max_age_days)),
        ]
        tab = self.search(domain)
        for record in tab:
            record.active = False
            
    
