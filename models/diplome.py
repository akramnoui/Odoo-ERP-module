# -*- coding: utf-8 -*-

from xml.dom import ValidationErr
from odoo import models, fields, api 

class diplome(models.Model):
    _name = 'esi.diplome'
    _description = "modele de diplome"

    f_name = fields.Char('First Name')
    l_name = fields.Char('Last Name')
    adresse = fields.Char('Adresse e-mail')
    matricule = fields.Char('matricule')
    specialite = fields.Selection([('SIT' , 'SIT') , ('SIQ', 'SIQ') , ('SIL' , 'SIL') , ('SID','SID') ] , string = "specialité")
    type = fields.Selection([('master', 'Master'), ('Ingénieur','ingénieur')])
    etudiant_id =  fields.Many2one('res.users','Etudiant', default=lambda self: self.env.user)
    
    file = fields.Binary(string='Attachements', attachment=True)

    file_name = fields.Char("File Name")

@api.constrains('file')
def _check_file(self):
       if str(self.file_name.split(".")[1]) != 'pdf' :
            raise ValidationErr("Cannot upload file different from .pdf file")
    
    # sexe = fields.Selection([('Male' , 'male') , ('Female'), ('female')])
    # adress = fields.Char()
    # birthday = fields.Date()
