import os
import dotenv
from dotenv import load_dotenv, find_dotenv, dotenv_values

from .config import install_dir


class EnvParser(object):

    def __init__(self, env_file=None):
        if env_file is not None:
            self.env_file = env_file
        else:
            self.env_file = self.get_env_file()
        self.load_env()

    def load_env(self):
        load_dotenv(self.env_file)

    """
    Find it under the root directory path/to/.env
    """
    def get_env_file(self):
        env_file = find_dotenv()
        if not os.path.exists(env_file):
            # /opt/shinetech/stdocker/.env
            env_file = install_dir + '/.env'
        return env_file

    """
    Retrieve all variables to OrderedDict
    """
    def get_values(self):
        return dotenv_values(self.env_file)

    """
    Get value of single variable
    """
    def get_value(self, key):
        return os.getenv(key)

    """
    Create or modify variables
    NOTE: need to remove quotes
        Correct: DOCUMENT_ROOT=/home/sunfeng/stdocker/www
        Incorrect: DOCUMENT_ROOT="/home/sunfeng/stdocker/www"
    In auto mode, don't add quotes if the value is only made of alphanumeric characters
    https://github.com/theskumar/python-dotenv/compare/v0.17.1...v0.18.0
    """
    def set_value(self, key, value):
        return dotenv.set_key(self.env_file, key, value, quote_mode='auto')


