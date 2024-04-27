import os

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'bundle'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

class Config:
    WTF_CSRF_ENABLED = False
    WTF_CSRF_CHECK_DEFAULT = False
    SECRET_KEY = '123456'
    SQLALCHEMY_DATABASE_URI = DB_URI