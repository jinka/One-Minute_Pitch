import os

class Config:


   SECRET_KEY = "try harder" #os.environ.get("SECRET_KEY")
   #WTF_CSRF_SECRET_KEY="a csrf secret key"
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://daud:jinkoos@localhost/pitch'

class ProdConfig(Config):
    pass

    


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}