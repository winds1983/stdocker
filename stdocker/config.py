import os

# Shinetech Docker installation directory
install_dir = '/opt/shinetech/stdocker'

# The directory where the stdocker command is currently executed
current_dir = os.getcwd()

base_domain = '.dev.php9.cc'

php_platforms = ['generic', 'magento', 'zend', 'symfony', 'laravel', 'yii',
                 'slim', 'cakephp', 'codeigniter', 'wordpress', 'drupal']

js_platforms = ['angular', 'react', 'vue', 'nextjs', 'nestjs', 'nuxtjs', 'vue_storefront', 'magento_pwa']
js_languages = ['javascript', 'typescript']

# enterprise = Adobe Commerce
# community = Magento Open Source
magento_versions = ['enterprise', 'community']

projects = ['hp']

# Default is bridge network
network_modes = ['bridge', 'overlay', 'host', 'ipvlan', 'macvlan']
