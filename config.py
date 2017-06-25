import os.path
"""
    Archivo de configuracion.
"""
DEBUG = True


SQLALCHEMY_DATABASE_URI = '{}'.format(
    'mysql+pymysql://username_db:youpassword@localhost/name_bd')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'Chinotto123+6'
