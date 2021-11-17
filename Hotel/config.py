from datetime import timedelta    
    
class Config:
    # SQLALCHEMY_DATABASE_URI= 'sqlite:///data.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Aa137540@localhost:3306/demo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "flask123"
    JWT_EXPIRATION_DELTA = timedelta(seconds = 300)
    JWT_AUTH_URL_RULE = "/auth/login"
    JWT_AUTH_HEADER_PREFIX = "FLASK"