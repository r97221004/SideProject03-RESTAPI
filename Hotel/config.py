from datetime import timedelta 
import os   


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "flask123"
    JWT_EXPIRATION_DELTA = timedelta(seconds = 300)
    JWT_AUTH_URL_RULE = "/auth/login"
    JWT_AUTH_HEADER_PREFIX = "FLASK"

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", 'mysql+pymysql://root:Aa137540@localhost:3306/demo')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", 'sqlite:///data.db')


app_config = {
    "testing": TestingConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
