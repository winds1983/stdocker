import os
from beautifultable import BeautifulTable
from termcolor import colored
from .yaml_parser import YamlParser
from .env_parser import EnvParser

from .config import install_dir


class EnvHandler(object):

    def __init__(self, working_dir=None):
        if working_dir is None:
            self.working_dir = install_dir
        else:
            self.working_dir = working_dir

    """
    Get all env configs
    """
    def get_env_values(self):
        env_file = self.working_dir + '/.env'
        env_handler = EnvParser(env_file=env_file)
        return env_handler.get_values()

    """
    Get current env from .env
    """
    def get_current_env(self):
        env_values = self.get_env_values()
        return env_values['DEFAULT_ENV']

    """
    Get configs for current env
    Will convert yaml to dict
    """
    def get_current_env_configs(self):
        config_file = self.get_current_env_config_file()
        yaml_parser = YamlParser(yaml_file=config_file)
        return yaml_parser.load_yaml_to_dict()

    """
    Get config file for current env
    e.g: /opt/shinetech/stdocker/config/env/templates/magento_244.yml
    """
    def get_current_env_config_file(self):
        current_env = self.get_current_env()

        custom_env_dir = self.working_dir + '/var/env'
        predefined_env_dir = self.working_dir + '/config/env/templates'

        config_file = predefined_env_dir + '/' + current_env + '.yml'
        if not os.path.exists(config_file):
            config_file = custom_env_dir + '/' + current_env + '.yml'
            if not os.path.exists(config_file):
                return None

        return config_file

    """
    List all customized environment names
    """
    def list_customized_env_names(self):
        env_files = self.list_customized_env_files()

        envs = []
        for env_file in env_files:
            if env_file != '.gitkeep':
                env = env_file.split('.')
                envs.append(env[0])

        envs.sort(reverse=False)

        return envs

    """
    List detailed config for all customized environments
    """
    def list_customized_detailed_envs(self):
        env_files = self.list_customized_env_files(with_dir=True)

        envs = []
        for env_file in env_files:
            if '.gitkeep' not in env_file:
                yaml_parser = YamlParser(yaml_file=env_file)
                detail_data = yaml_parser.load_yaml_to_dict()

                filename = os.path.basename(env_file)
                env_name = filename.split('.')
                env = env_name[0]
                detail_data['env'] = env

                envs.append(detail_data)

        return envs

    """
    List files for all customized environments
    """
    def list_customized_env_files(self, with_dir=False):
        custom_env_dir = self.working_dir + '/var/env'
        predefined_env_dir = self.working_dir + '/config/env/templates'

        custom_env_files = os.listdir(custom_env_dir)
        predefined_env_files = os.listdir(predefined_env_dir)

        env_files = []
        if with_dir:
            for filename in predefined_env_files:
                file_path = predefined_env_dir + '/' + filename
                env_files.append(file_path)

            for filename in custom_env_files:
                file_path = custom_env_dir + '/' + filename
                env_files.append(file_path)
        else:
            env_files = predefined_env_files + custom_env_files

        env_files.sort(reverse=False)

        return env_files

    def list_env_table(self):
        current_env = self.get_current_env()
        customized_envs = self.list_customized_detailed_envs()
        # env_names = self.list_customized_env_names()
        services = ['webserver', 'php', 'mysql', 'mariadb',
                    'phpmyadmin', 'elasticsearch', 'elasticvue',
                    'redis', 'phpredisadmin', 'rabbitmq', 'mailcatcher',
                    'mongo', 'mongoexpress', 'postgres', 'pgweb', 'memcached', 'webgrind']
        service_names = ['Web Server', 'PHP', 'MySQL', 'MariaDB',
                         'phpMyAdmin', 'Elasticsearch', 'Elasticvue',
                         'Redis', 'phpRedisAdmin', 'RabbitMQ', 'Mailcatcher',
                         'MongoDB', 'Mongo Express', 'PostgreSQL', 'Pgweb', 'Memcached', 'Webgrind']

        table = BeautifulTable(maxwidth=200)
        columns_headers = ['Env Code'] + service_names

        env_detail_names = []
        for item in customized_envs:
            env_detail_names.append(item['name'])
            env = item['env']
            # description = item['description']

            services_status = []
            if env == current_env:
                services_status.append(colored(env, 'red'))
            else:
                services_status.append(env)

            for service in services:
                status = 'N'
                if service in item['services'].keys():
                    if item['services'][service] is True or item['services'][service] == 'yes':
                        status = 'Y'
                    elif item['services'][service] is False or item['services'][service] == 'no':
                        status = 'N'
                    else:
                        status = item['services'][service]

                if env == current_env:
                    services_status.append(colored(status, 'red'))
                else:
                    services_status.append(status)

            table.rows.append(services_status)

        table.rows.header = env_detail_names
        table.columns.header = columns_headers

        return table
