# Shinetech Docker CLI

[![PyPI version][pypi_badge]][pypi_link]

Shinetech Docker CLI is a more intelligent, user-friendly and advanced configurable local development environment built with Docker.

- [Getting Started](#getting-started)
- [Use Cases](#use-cases)
  * [Run docker command](#run-docker-command)
  * [Run docker-compose command](#run-docker-compose-command)
  * [Run docker exec command](#run-docker-exec-command)
  * [Log in to the specified server using SSH](#log-in-to-the-specified-server-using-ssh)
  * [Launch docker services](#launch-docker-services)
  * [Stop docker services](#stop-docker-services)
  * [Restart specified docker service](#restart-specified-docker-service)
  * [Configure local environment](#configure-local-environment)
  * [Build local development environment with your configuration](#build-local-development-environment-with-your-configuration)
  * [Export and import database](#export-and-import-database)
    * [Export database](#export-database)
    * [Import database](#import-database)
  * [Show the local environment and workspace information](#show-the-local-environment-and-workspace-information)
  * [List all environments](#list-all-environments)
  * [Initial workspace](#initial-workspace)
  * [Create and setup project](#create-and-setup-project)
    * [Create a new PHP project based on a base template or framework skeleton](#create-a-new-php-project-based-on-a-base-template-or-framework-skeleton)
    * [Create a new Magento project based on the source code or composer](#create-a-new-magento-project-based-on-the-source-code-or-composer)
    * [Create a new Javascript project based on a base template or framework skeleton](#create-a-new-javascript-project-based-on-a-base-template-or-framework-skeleton)
    * [Build an existing project based on existing code and database](#build-an-existing-project-based-on-existing-code-and-database)
  * [Upgrade Shinetech Docker](#upgrade-shinetech-docker)
  * [Switch network mode for a container](#switch-network-mode-for-a-container)
  * [Edit or show configuration of docker-compose.yml](#edit-or-show-configuration-of-docker-compose-yml)

## Getting Started

```shell
sudo pip3 install stdocker
```

If you get error `ERROR: Could not find a version that satisfies the requirement`, please use the following command to install:
```shell
python3 -m pip install stdocker==1.0.13
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
  about                   Show the local environment and workspace...
  bash                    Bash session for running container
  build                   Build local development environment with your...
  configure               Configure local environment, will guide you...
  create-js-project       Create a new Javascript project based on a base...
  create-magento-project  Create a new Magento project based on the...
  create-php-project      Create a new PHP project based on a base...
  database                Export or import database
  docker-compose          Execute sudo docker-compose * command
  docker-exec             Execute sudo docker exec * command
  docker-run              Execute sudo docker * command
  editor                  Edit or show configuration of docker-compose.yml
  envs                    List all environments
  restart                 Restarts all stopped and running services, or...
  setup-project           Build a existing project based on existing code...
  start                   Launch docker services
  status                  List all running containers
  stop                    Stop docker services
  switch-network          Configure network mode for a container
  upgrade                 Upgrade Shinetech Docker
  workspace               Initial workspace
```

For the detailed usage of each command, you can use the following command to view:

```shell
stdocker [COMMAND] --help
```
e.g:
```shell
stdocker create-project --help
```

### Run docker command

If you want to run `sudo docker *` command, you can use our command like this:
```shell
stdocker docker-run <DOCKER_COMMAND>
```
You can check `sudo docker` and see which original command we supported. Please use double quotes if `DOCKER_COMMAND` contains spaces or other parameters.

e.g:
```shell
stdocker docker-run info
```
This command is equivalent to:
```shell
sudo docker info
```

### Run docker-compose command

If you want to run `sudo docker-compose *` command, you can use our command like this:
```shell
stdocker docker-compose <DOCKER_COMPOSE_COMMAND>
```
You can check `sudo docker-compose` and see which original command we supported. Please use double quotes if `DOCKER_COMPOSE_COMMAND` contains spaces or other parameters.

e.g:
```shell
stdocker docker-compose ps
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
stdev_nginx_1           /docker-entrypoint.sh /usr ...   Up      0.0.0.0:443->443/tcp,:::443->443/tcp, 0.0.0.0:6081->6081/tcp,:::6081->6081/tcp, 0.0.0.0:80->80/tcp,:::80->80/tcp      
stdev_phpfpm_1          /docker-entrypoint.sh php-fpm    Up      9000/tcp                                                                                                              
stdev_phpmyadmin_1      /docker-entrypoint.sh apac ...   Up      0.0.0.0:8443->443/tcp,:::8443->443/tcp, 0.0.0.0:8080->80/tcp,:::8080->80/tcp                                          
stdev_phpredisadmin_1   tini -- php -S 0.0.0.0:80        Up      0.0.0.0:8089->80/tcp,:::8089->80/tcp                                                                                  
stdev_rabbitmq_1        docker-entrypoint.sh rabbi ...   Up      15671/tcp, 0.0.0.0:15672->15672/tcp,:::15672->15672/tcp, 15691/tcp, 15692/tcp, 25672/tcp, 4369/tcp, 5671/tcp, 5672/tcp
stdev_redis_1           docker-entrypoint.sh redis ...   Up      0.0.0.0:6379->6379/tcp,:::6379->6379/tcp
```

**NOTE:**
You can also use `stdocker status` list all running docker containers.

### Run docker exec command

If you want to run `sudo docker exec *` command, you can use our command like this:
```shell
stdocker docker-exec <COMMAND>
```
You can check `sudo docker exec --help` and see which original command we supported. Please use double quotes if `COMMAND` contains spaces or other parameters.

e.g:
```shell
stdocker docker-exec "-it stdev_phpfpm_1 /bin/bash"
```
This command is equivalent to:
```shell
sudo docker exec -it stdev_phpfpm_1 /bin/bash
```

### Log in to the specified server using SSH

```shell
stdocker bash <SERVICE>
```

e.g:
```shell
stdocker bash phpfpm
stdocker bash mysql
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
stdocker restart # Restart all services
stdocker restart nginx
stdocker restart phpfpm
```

### Configure local environment

It will guide you through creating your .env and docker-compose.yml

```shell
stdocker configure
```

### Build local development environment with your configuration

Switch and build your development environment using the following command:
```shell
stdocker build <ENV>
```

If `ENV` is empty, it will guide you to create your customized configuration, otherwise will base on your specified env to build services.

```shell
stdocker build
stdocker build --env=magento_244
```

### Export and import database

```shell
stdocker database <ACTION{import|export}>
```

#### Export database:
```shell
stdocker database export --dbname=test
stdocker database export --dbname=test --backup-sql-file=test_20220823.sql
```

#### Import database:
```shell
stdocker database import --dbname=test --backup-sql-file=test_20220823.sql
```

### Show the local environment and workspace information

```shell
stdocker about
```
You can see the following information:
```
Current environment:
 - lamp
Your workspace information:
 - Workspace: /home/sunfeng/stdocker
 - Project Directory: /home/sunfeng/stdocker/www
 - Nginx VHosts: /home/sunfeng/stdocker/config/services/nginx/sites-enabled
 - Nginx Log: /home/sunfeng/stdocker/var/logs/nginx
 - Apache VHosts: /home/sunfeng/stdocker/config/services/apache/sites-enabled
 - Apache Log: /home/sunfeng/stdocker/var/logs/apache2
 - SSL CA: /home/sunfeng/stdocker/config/services/ca
 - php.ini: /home/sunfeng/stdocker/config/services/php/php.ini
 - Composer auth.json: /home/sunfeng/stdocker/config/services/composer/auth.json
 - MySQL Log: /home/sunfeng/stdocker/var/logs/mysql
```

### List all environments

```shell
stdocker envs
```
You can see the following information:
```
+---------------+-------------+------------+-----+-------+---------+------------+---------------+------------+-------+---------------+----------+-------------+---------+---------------+------------+-------+
|               |  Env Code   | Web Server | PHP | MySQL | MariaDB | phpMyAdmin | Elasticsearch | Elasticvue | Redis | phpRedisAdmin | RabbitMQ | Mailcatcher | MongoDB | Mongo Express | PostgreSQL | Pgweb |
+---------------+-------------+------------+-----+-------+---------+------------+---------------+------------+-------+---------------+----------+-------------+---------+---------------+------------+-------+
|  Basic LNMP   |    basic    |   nginx    | 7.4 |  8.0  |    N    |     Y      |       N       |     N      |   N   |       N       |    N     |      N      |    N    |       N       |     N      |   N   |
+---------------+-------------+------------+-----+-------+---------+------------+---------------+------------+-------+---------------+----------+-------------+---------+---------------+------------+-------+
|   Full LNMP   |    full     |   nginx    | 7.4 |  8.0  |    N    |     Y      |     7.16      |     Y      |  6.2  |       Y       |   3.9    |      Y      |    Y    |       Y       |     Y      |   Y   |
+---------------+-------------+------------+-----+-------+---------+------------+---------------+------------+-------+---------------+----------+-------------+---------+---------------+------------+-------+
|     LAMP      |    lamp     |   apache   | 7.4 |  8.0  |    N    |     Y      |     7.16      |     N      |  6.2  |       N       |   3.9    |      Y      |    N    |       N       |     N      |   N   |
+---------------+-------------+------------+-----+-------+---------+------------+---------------+------------+-------+---------------+----------+-------------+---------+---------------+------------+-------+
|     LNMP      |    lnmp     |   nginx    | 7.4 |  8.0  |    N    |     Y      |     7.16      |     N      |  6.2  |       N       |   3.9    |      Y      |    N    |       N       |     N      |   N   |
+---------------+-------------+------------+-----+-------+---------+------------+---------------+------------+-------+---------------+----------+-------------+---------+---------------+------------+-------+
|  Magento 2.3  | magento_23  |   nginx    | 7.3 |  5.7  |    N    |     Y      |      7.6      |     Y      |  5.0  |       Y       |   3.8    |      Y      |    N    |       N       |     N      |   N   |
+---------------+-------------+------------+-----+-------+---------+------------+---------------+------------+-------+---------------+----------+-------------+---------+---------------+------------+-------+
|  Magento 2.4  | magento_24  |   nginx    | 7.4 |  8.0  |    N    |     Y      |     7.16      |     Y      |  6.2  |       Y       |   3.8    |      Y      |    N    |       N       |     N      |   N   |
+---------------+-------------+------------+-----+-------+---------+------------+---------------+------------+-------+---------------+----------+-------------+---------+---------------+------------+-------+
| Magento 2.4.4 | magento_244 |   nginx    | 7.4 |  8.0  |    N    |     Y      |     7.16      |     Y      |  6.2  |       Y       |   3.9    |      Y      |    N    |       N       |     N      |   N   |
+---------------+-------------+------------+-----+-------+---------+------------+---------------+------------+-------+---------------+----------+-------------+---------+---------------+------------+-------+
| Magento 2.4.5 | magento_245 |   nginx    | 8.1 |  8.0  |    N    |     Y      |     7.17      |     Y      |  6.2  |       Y       |   3.9    |      Y      |    N    |       N       |     N      |   N   |
+---------------+-------------+------------+-----+-------+---------+------------+---------------+------------+-------+---------------+----------+-------------+---------+---------------+------------+-------+
```

The highlight row is your current environment, you can use `Env Code` for `stdocker build --env=<ENV>` command.

### Initial workspace

It will initial your workspace to your home or specified directory, and update env config.

```shell
stdocker workspace
```

### Create and setup project

#### Create a new PHP project based on a base template or framework skeleton

```shell
stdocker create-php-project [OPTIONS]
```

Create a Magento 2 project:
```shell
stdocker create-php-project --platform=magento --project-name=m2project --target-version=2.4.5
```

e.g:

Create a Symfony project:
```shell
stdocker create-php-project --platform=symfony --project-name=sfproject
```

#### Create a new Magento project based on the source code or composer

Please download the Magento source code from the official website first if use source code to create project.

```shell
stdocker create-magento-project [OPTIONS]
```

e.g:

Create a Magento 2.4.5 project with source code:
```shell
stdocker create-magento-project --target-version=2.4.5 --source-code-file=/home/sunfeng/Downloads/adobe-commerce-2.4.5-2022-07-21-08-24-23.zip
```

Create a Magento 2.4.5 project with custom project name:
```shell
stdocker create-magento-project --target-version=2.4.5 --source-code-file=/home/sunfeng/Downloads/adobe-commerce-2.4.5-2022-07-21-08-24-23.zip --project-name=testproject
```

Create a Magento 2.4.5 project with composer:
```shell
stdocker create-magento-project --target-version=2.4.5
```

#### Create a new Javascript project based on a base template or framework skeleton

```shell
stdocker create-js-project [OPTIONS]
```

e.g:

Create a React project:
```shell
stdocker create-js-project --platform=react --project-name=reactproject
```

#### Build an existing project based on existing code and database

```shell
stdocker setup-project [OPTIONS]
```

Setup HP project:
```shell
stdocker setup-project --project-name=hp --db-sql-file=/home/sunfeng/Downloads/20220824201501.sql --country=id
```

### Upgrade Shinetech Docker

```shell
stdocker upgrade
```

Upgrade to the specified version:
```shell
stdocker upgrade --target_version=1.0.1
```

If you want to restart docker services after upgrade, please use the following command:
```shell
stdocker upgrade --force
```

### Switch network mode for a container

```shell
stdocker switch-network [OPTIONS] SERVICE
```

```shell
stdocker switch-network phpfpm --network-mode=host
stdocker switch-network phpfpm --network-mode=bridge
```

### Edit or show configuration of docker-compose.yml

```shell
stdocker editor [OPTIONS]
```

Show the configuration in terminal:
```shell
stdocker editor
```

Edit the configuration via vim:
```shell
stdocker editor --edit-mode
```


[pypi_badge]: https://badge.fury.io/py/stdocker.svg
[pypi_link]: http://badge.fury.io/py/stdocker
