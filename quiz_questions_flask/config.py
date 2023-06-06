import os
import secrets
import string

from dotenv import load_dotenv

load_dotenv()

app_dir = os.path.abspath(os.path.dirname(__file__))

LINK = os.environ.get("LINK")


def set_secret_key(quantity: int) -> str:
    """
    Создает секретный ключ типа '9vfMa4Wz57dKk6djw76dF' из букв
    латинского алфавита (в нижнем и верхнем регистре) и цифр.
    Длина ключа передается в аргументах функции.
    """
    alphabet = string.ascii_letters + string.digits
    secret_key = ''.join(secrets.choice(alphabet) for i in range(quantity))
    return secret_key


class BaseConfig:
    # SECRET_KEY = os.environ.get("SECRET_KEY") or "SECRET_KEY"
    SECRET_KEY = os.environ.get("SECRET_KEY") or set_secret_key(21)
    SQLALCHEMY_TRACK_MODIFICATION = False

    # class Config:
    #     # Имя файла, откуда будут прочитаны данные
    #     # (относительно текущей рабочей директории)
    #     env_file = '.env'
    #     # Кодировка читаемого файла
    #     env_file_encoding = 'utf-8'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEVELOPMENT_DATABASE_URI") \
                              or "sqlite:///develop.db"


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TESTING_DATABASE_URI") or \
                              "sqlite:///test.db"


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("PRODUCTION_DATABASE_`URI") or \
                              "sqlite:///product.db"
