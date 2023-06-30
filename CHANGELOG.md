# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this
project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.1.1] - 2023-06-30

### Added

- Fix install or upgrade docker compose command


## [1.1.0] - 2023-06-30

### Added

- Add install or upgrade docker compose command


## [1.0.18] - 2023-05-04

### Fixed

- Fix project name and directory bugs for create Magento project


## [1.0.17] - 2023-01-17

### Added

- Add Magento 2 PWA project creation support


## [1.0.16] - 2023-01-04

### Added

- Add Vue Storefront and NuxtJS project creation support


## [1.0.15] - 2022-12-16

### Added

- Improve start and stop command to support the specified services


## [1.0.14] - 2022-12-15

### Added

- Show or live tail docker container logs


## [1.0.13] - 2022-11-18

### Added

- Add switch docker container network command
- Add edit or show configuration of docker-compose.yml command
- Update command docs
- Build publish script


## [1.0.12] - 2022-11-10

### Added

- Add create js project command
- Rebuild restart command for restarts all stopped and running services


## [1.0.11] - 2022-11-04

### Added

- Add Webgrind to env list

### Fixed

- Fix yes or no display issue for env list

## [1.0.10] - 2022-09-13

### Added

- Add CakePHP, CodeIgniter and Drupal project creation
- Fix bugs and adjust warning message color


## [1.0.9] - 2022-09-09

### Added

- Rebuild create and setup project command
- Update project creation parameters
- Add composer auth.json in about command
- Update use cases


## [1.0.8] - 2022-09-08

### Added

- Adjust platforms for init project command
- Add MariaDB to env table
- Add sort for env table
- Add webserver for create project and magento project
- Add Zend framework to platforms
- Add status command to list all running containers
- Add target version to init magento command and make source code is not required
- Add memcached for env table


## [1.0.7] - 2022-09-01

### Added

- Add list envs command and rebuild env handler code
- Optimize env table and colored current env


## [1.0.6] - 2022-08-31

### Fixed

- Fix version convert bug and optimize init magento command


## [1.0.5] - 2022-08-30

### Added

- Add conformation when project already exists for initial project
- Add initial the Magento project command


## [1.0.4] - 2022-08-29

### Added

- Add force restart docker services for upgrade
- Update use cases documents
- Improve initial project command


## [1.0.3] - 2022-08-26

### Fixed

- Fix bugs


## [1.0.2] - 2022-08-26

### Added

- Add workspace command
- Remove GitHub actions
- Add workspace to init project command

### Fixed

- Fix bug and optimize code


## [1.0.1] - 2022-08-23

### Added

- Improve cli
- Improve documents

### Fixed

- Fix cli bug


## [1.0.0] - 2022-08-22

### Added

- Build Shinetech Docker CLI code architecture
- Implement all functions

### Fixed

- Fix bug: Warning: 'classifiers' should be a list, got type 'tuple'
