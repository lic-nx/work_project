__all__ = ['Config']

import os


class Config:
    PORT = 8000
    HOST = '0.0.0.0'
    USER_BD = os.getenv('POSTGRES_USER')
    PASS_BD = os.getenv('POSTGRES_PASSWORD')
    HOST_BD = os.getenv('POSTGRES_HOST')
    PORT_BD = os.getenv('POSTGRES_PORT')
    NAME_BD = os.getenv('POSTGRES_DB')
    DB_CONTAINER_NAME = os.getenv('DB_CONTAINER_NAME')
    EXTERNAL_CONTOUR_URL = os.getenv('EXTERNAL_CONTOUR_URL')
    CLIENT_CONTOUR_URL = os.getenv('CLIENT_CONTOUR_URL')
    CLIENT_TOKEN = os.getenv('CLIENT_TOKEN')
    TOKEN = os.getenv('TOKEN')
    JSONS_PATH = os.getenv('JSONS_PATH')
    SMTP_EMAIL = os.getenv('SMTP_EMAIL')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
    SMSC_LOGIN = os.getenv('SMSC_LOGIN')
    SMSC_PASSWORD = os.getenv('SMSC_PASSWORD')
    SMSC_EMAIL_SENDER = os.getenv('SMSC_EMAIL_SENDER')
    CHECK_CLIENTS_INTERVAL = os.getenv('CHECK_CLIENTS_INTERVAL', 180)
    PARSING_ORDERS_INTERVAL = os.getenv('PARSING_ORDERS_INTERVAL', 300)
    PARSING_TIME = os.getenv('PARSING_TIME', 0)
    SECRET_HMAC_KEY = os.getenv('SECRET_HMAC_KEY')


class RabbitMQConfig:
    RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
    RABBITMQ_PORT = os.getenv("RABBITMQ_PORT")
    RABBITMQ_LOGIN = os.getenv("RABBITMQ_LOGIN")
    RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
    RABBITMQ_EXCHANGE = os.getenv("RABBITMQ_EXCHANGE")
    RABBITMQ_ROUT = os.getenv("RABBITMQ_ROUT")
    RABBITMQ_VHOST = os.getenv("RABBITMQ_VHOST")


app_settings = Config()
rabbit_settings = RabbitMQConfig()
