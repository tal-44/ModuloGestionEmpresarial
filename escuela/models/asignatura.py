from odoo import models, fields

class Asignatura(models.Model):
    _name = 'escuela.asignatura'
    _description = 'Asignatura'

    codigo = fields.Char(string='Código de Asignatura', required=True)
    nombre = fields.Char(string='Nombre de Asignatura', required=True)
    horas = fields.Integer(string='Número de Horas')
    grupo_ids = fields.Many2many('escuela.grupo', string='Grupos')
