{
    'name': 'Gestión Escolar',
    'version': '1.0',
    'summary': 'Módulo para gestionar estudiantes, asignaturas y grupos en una escuela',
    'author': 'Juan',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estudiante_views.xml',
        'views/asignatura_views.xml',
        'views/grupo_views.xml',
        'views/menu.xml',
        'reports/grupo_report.xml',
    ],
    'installable': True,
    'application': True,
}
