import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# https://medium.com/@lewis.devs/how-to-send-an-e-mail-with-flask-a13e751a5cab

class Config:
    DEBUG = True  # You can set this to False if you don't want debugging
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')

