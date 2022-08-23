# Shinetech Docker CLI

[![Build Status][build_status_badge]][build_status_link]
[![PyPI version][pypi_badge]][pypi_link]

Shinetech Docker CLI is a more intelligent, user-friendly and advanced configurable local development environment built with Docker.

## Getting Started

```shell
pip3 install stdocker
```

It based on the internal docker project `Shinetech Docker`, please install it first. If you do not have permission to use Shinetech Docker, please ignore this package.

After the installation is successful, you can run the `stdocker` command in any directory and perform the operations you need.

## Use Cases

Run the following command to view the command help.
```shell
stdocker
```
or
```shell
stdocker --help
```
You can see the following information:
```
Usage: stdocker [OPTIONS] COMMAND [ARGS]...

  Shinetech Docker CLI

Options:
  -d, --working-dir PATH  Location of the installation directory, defaults to
                          /opt/shinetech/stdocker.
  --version               Show the version and exit.
  --help                  Show this message and exit.

Commands:
  about         Show the local environment and workspace information
  build         Build local development environment with your configuration
  compose       Execute sudo docker-compose * command
  configure     Configure local environment, will guide you through...
  database      Export or import database
  exec          Execute sudo docker exec * command
  init-project  Initial the project
  restart       Restart specified docker service
  run           Execute sudo docker * command
  ssh           Log in to the specified server using SSH
  start         Launch docker services
  stop          Stop docker services
  upgrade       Upgrade Shinetech Docker
```

### Run docker command

If you want to run `sudo docker *` command, you can use our command like this:
```shell
stdocker run <DOCKER_COMMAND>
```
You can check `sudo docker` and see which original command we supported. Please use double quotes if `DOCKER_COMMAND` contains spaces or other parameters.

e.g:
```shell
stdocker run info
```
This command is equivalent to:
```shell
sudo docker info
```

### Run docker-compose command

If you want to run `sudo docker-compose *` command, you can use our command like this:
```shell
stdocker compose <DOCKER_COMPOSE_COMMAND>
```
You can check `sudo docker-compose` and see which original command we supported. Please use double quotes if `DOCKER_COMPOSE_COMMAND` contains spaces or other parameters.

e.g:
```shell
stdocker compose ps
```
This command is equivalent to:
```shell
sudo docker-compose ps
```
You will see the following result:
```
        Name                       Command               State                                                           Ports                                                         
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
stdev_elasticsearch_1   /bin/tini -- /usr/local/bi ...   Up      0.0.0.0:9200->9200/tcp,:::9200->9200/tcp, 9300/tcp                                                                    
stdev_elasticvue_1      nginx -g daemon off;             Up      80/tcp, 0.0.0.0:8082->8080/tcp,:::8082->8080/tcp                                                                      
stdev_mailcatcher_1     mailcatcher --smtp-ip=0.0. ...   Up      1025/tcp, 0.0.0.0:1080->1080/tcp,:::1080->1080/tcp                                                                    
stdev_mysql_1           docker-entrypoint.sh mysqld      Up      0.0.0.0:3306->3306/tcp,:::3306->3306/tcp, 33060/tcp                                                                   
stdev_nginx_1           /docker-entrypoint.sh ngin ...   Up      0.0.0.0:443->443/tcp,:::443->443/tcp, 0.0.0.0:80->80/tcp,:::80->80/tcp                                                
stdev_phpfpm_1          /docker-entrypoint.sh php-fpm    Up      9000/tcp                                                                                                              
stdev_phpmyadmin_1      /docker-entrypoint.sh apac ...   Up      0.0.0.0:8443->443/tcp,:::8443->443/tcp, 0.0.0.0:8080->80/tcp,:::8080->80/tcp                                          
stdev_phpredisadmin_1   tini -- php -S 0.0.0.0:80        Up      0.0.0.0:8089->80/tcp,:::8089->80/tcp                                                                                  
stdev_rabbitmq_1        docker-entrypoint.sh rabbi ...   Up      15671/tcp, 0.0.0.0:15672->15672/tcp,:::15672->15672/tcp, 15691/tcp, 15692/tcp, 25672/tcp, 4369/tcp, 5671/tcp, 5672/tcp
stdev_redis_1           docker-entrypoint.sh redis ...   Up      0.0.0.0:6379->6379/tcp,:::6379->6379/tcp 
```

### Run docker exec command

If you want to run `sudo docker exec *` command, you can use our command like this:
```shell
stdocker exec <COMMAND>
```
You can check `sudo docker exec --help` and see which original command we supported. Please use double quotes if `COMMAND` contains spaces or other parameters.

e.g:
```shell
stdocker exec "-it stdev_phpfpm_1 /bin/bash"
```
This command is equivalent to:
```shell
sudo docker exec -it stdev_phpfpm_1 /bin/bash
```

### Log in to the specified server using SSH

```shell
stdocker ssh <SERVICE>
```

e.g:
```shell
stdocker ssh phpfpm
stdocker ssh mysql
```
This command is equivalent to:
```shell
sudo docker exec -it stdev_phpfpm_1 /bin/bash
sudo docker exec -it stdev_mysql_1 /bin/bash
```

### Launch docker services

It will stop local services and launch the docker services

```shell
stdocker start
```

### Stop docker services

It will stop the docker services and launch local services

```shell
stdocker stop
```

### Restart specified docker service

```shell
stdocker restart <SERVICE>
```

e.g:
```shell
stdocker restart nginx
stdocker restart phpfpm
```

### Configure local environment

It will guide you through creating your .env and docker-compose.yml

```shell
stdocker configure
```

### Build local development environment with your configuration

```shell
stdocker build <ENV>
```

If `ENV` is empty, it will guide you to create your customized configuration, otherwise will base on your specified env to build services.

```shell
stdocker build
stdocker build --env=magento_244
```

### Export or import database

```shell
stdocker database <ACTION{import|export}>
```

#### Export database:
```shell
stdocker database export --dbname=test
stdocker database export --dbname=test --backup_sql_file=test_20220823.sql
```

#### Import database:
```shell
stdocker database import --dbname=test --backup_sql_file=test_20220823.sql
```

### Show the local environment and workspace information

```shell
stdocker about
```
You can see the following information:
```
Current environment:
 - magento_244
Your workspace information:
 - Workspace: /home/sunfeng/stdocker
 - Project Directory: ./www
 - Nginx VHosts: ./config/services/nginx/sites-enabled
 - Nginx Log: ./var/logs/nginx
 - Apache VHosts: ./config/services/apache/sites-enabled
 - Apache Log: ./var/logs/apache2
 - SSL CA: ./config/services/ca
 - php.ini: ./config/services/php/php.ini
 - MySQL Log: ./var/logs/mysql
```

### Initial the project

```shell
stdocker init-project [OPTIONS]
```

Initial a Magento 2 project:
```shell
stdocker init-project --platform=magento2 --name=m2project
```

Initial a Symfony project:
```shell
stdocker init-project --platform=symfony --name=sfproject
```

### Upgrade Shinetech Docker

```shell
stdocker upgrade
```

Upgrade to the specified version:
```shell
stdocker upgrade --target_version=1.0.1
```


[build_status_badge]: https://github.com/winds1983/stdocker/actions/workflows/test.yml/badge.svg
[build_status_link]: https://github.com/winds1983/stdocker/actions/workflows/test.yml
[pypi_badge]: https://badge.fury.io/py/stdocker.svg
[pypi_link]: http://badge.fury.io/py/stdocker
