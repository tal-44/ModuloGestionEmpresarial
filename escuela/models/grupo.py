from odoo import models, fields

class Grupo(models.Model):
    _name = 'escuela.grupo'
    _description = 'Grupo'

    descripcion = fields.Char(string='Descripción', required=True)
    modulo_profesional = fields.Selection([
        ('SMR', 'SMR'),
        ('DAM', 'DAM'),
        ('DAW', 'DAW'),
        ('ASIR', 'ASIR')
    ], string='Módulo Profesional', default='SMR')

    curso = fields.Selection([
        ('1', '1'),
        ('2', '2')
    ], string='Curso', default='1')

    estudiante_ids = fields.One2many('escuela.estudiante', 'grupo_id', string='Estudiantes')
    asignatura_ids = fields.Many2many('escuela.asignatura', string='Asignaturas')
