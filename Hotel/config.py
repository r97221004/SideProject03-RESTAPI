from datetime import timedelta
import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "flask123")
    JWT_EXPIRATION_DELTA = timedelta(seconds=300)
    JWT_AUTH_URL_RULE = "/auth/login"
    JWT_AUTH_HEADER_PREFIX = os.getenv("JWT_AUTH_HEADER_PREFIX", "FLASK")
    PROPAGATE_EXCEPTIONS = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL",
                                        f'mysql+pymysql://root:{os.getenv("PASSWORD")}@localhost:3306/demo')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", 'sqlite:///data.db')
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)


app_config = {
    "testing": TestingConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
