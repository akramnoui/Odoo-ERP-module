# -*- coding: utf-8 -*-

from xml.dom import ValidationErr
from odoo import models, fields, api 

class demande(models.Model):
    _name = 'esi.demande'
    _description = "modele de demande"

    f_name = fields.Char('First Name')
    l_name = fields.Char('Last Name')
    adresse = fields.Char('Adresse e-mail')
    matricule = fields.Char('matricule')
    # specialite = fields.Char('specialité')
    diplome = fields.Selection([('master', 'Master'), ('Ingénieur','ingénieur')])
    
    file = fields.Binary(string='file', attachment=True)

    file_name = fields.Char("File Name")

@api.constrains('file')
def _check_file(self):
       if str(self.file_name.split(".")[1]) != 'pdf' :
            raise ValidationErr("Cannot upload file different from .pdf file")
    
    # sexe = fields.Selection([('Male' , 'male') , ('Female'), ('female')])
    # adress = fields.Char()
    # birthday = fields.Date()
class diplome(models.Model):
    _name = 'esi.demande'
    _description = "modele de demande"

    f_name = fields.Char('First Name')
    l_name = fields.Char('Last Name')
    adresse = fields.Char('Adresse e-mail')