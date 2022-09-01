from pathlib import Path
from .env_handler import EnvHandler


"""
List all environment names
"""
def list_env_names(install_dir):
    env_handler = EnvHandler(working_dir=install_dir)
    return env_handler.list_customized_env_names()


"""
Get current user home directory
"""
def get_default_workspace():
    return str(Path.home()) + '/stdocker'


"""
Convert version
e.g: 
2.4.5 > 245
2.4.3-p2 > 243p2
"""
def convert_version(version):
    version = version.replace(".", "").replace("-", "").replace("_", "")
    return version
