    
    
class Config:
    # SQLALCHEMY_DATABASE_URI= 'sqlite:///data.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Aa137540@localhost:3306/demo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "flask123"