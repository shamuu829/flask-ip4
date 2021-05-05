import os

class Config:
    
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://shamsa:Shamsa123@localhost/myblog'
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}