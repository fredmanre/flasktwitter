import os.path
"""
    Archivo de configuracion.
"""
DEBUG = True


SQLALCHEMY_DATABASE_URI = '{}'.format(
    'mysql+pymysql://fredmanre:perrodeagua@localhost/flasktwitter')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'Chinotto123+6'
