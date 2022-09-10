import os

# Shinetech Docker installation directory
install_dir = '/opt/shinetech/stdocker'

# The directory where the stdocker command is currently executed
current_dir = os.getcwd()

base_domain = '.dev.php9.cc'

platforms = ['generic', 'magento', 'zend', 'symfony', 'laravel', 'yii',
             'slim', 'cakephp', 'codeigniter', 'wordpress', 'drupal']

projects = ['hp']
