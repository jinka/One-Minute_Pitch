import os

class Config:

   SECRET_KEY = "try harder" #os.environ.get("SECRET_KEY")
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://daud:jinkoos@localhost/pitch'
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}