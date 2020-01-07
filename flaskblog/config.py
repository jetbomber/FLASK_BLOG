import os


class Config:
    SECRET_KEY = "485a0434bdced76116a05fcf2a67ecf4"
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db"
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "rwwebdevtest"
    MAIL_PASSWORD = "yaafdlijgjxynplv"
