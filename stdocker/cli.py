import os
import sys
import re
from typing import Any, Dict, List
from .utils import list_env_names, get_default_workspace, convert_version
from .env_handler import EnvHandler

try:
    import click
except ImportError:
    sys.stderr.write('It seems stdocker is not installed with cli option. \n'
                     'Run pip3 install "stdocker[cli]" to fix this.')
    sys.exit(1)

from .version import __version__
from .config import install_dir
from .config import current_dir
from .config import base_domain
from .config import php_platforms, js_platforms, js_languages
from .config import projects
from .config import network_modes


"""
Check if project name is valid
"""
def check_project_name(ctx, param, value):
    if not param.required and value is None:
        return value
    pattern = re.compile('^[a-zA-Z][0-9a-zA-Z]{0,50}$')
    matched = pattern.match(value)
    if matched is None:
        click.echo(
            click.style(f"Invalid project name: Limit length to 1-50 characters (1 character in front + up to 49 characters in back)",
                        fg='red'))
        ctx.abort()
    return value


@click.group()
@click.option('-d', '--working-dir', default=install_dir,
              type=click.Path(dir_okay=True),
              help="Location of the installation directory, defaults to " + install_dir + ".")
@click.version_option(version=__version__, prog_name='Shinetech Docker CLI')
@click.pass_context
def cli(ctx: click.Context, working_dir: Any) -> None:
    """Shinetech Docker CLI"""
    ctx.obj = {}
    ctx.obj['WORKING_DIR'] = working_dir
    ctx.obj['CURRENT_DIR'] = current_dir
    # All scripts will based on working dir to run
    os.chdir(working_dir)  # Debug directory: /var/www/html/Shinetech/shinetech-docker


@cli.command()
@click.pass_context
@click.argument('command', required=True)
def docker_run(ctx: click.Context, command: Any) -> None:
    """Execute sudo docker * command"""
    os.system('sudo docker ' + command)


@cli.command()
@click.pass_context
@click.argument('command', required=True)
def docker_exec(ctx: click.Context, command: Any) -> None:
    """Execute sudo docker exec * command"""
    os.system('sudo docker exec ' + command)


@cli.command()
@click.pass_context
@click.argument('command', required=True)
def docker_compose(ctx: click.Context, command: Any) -> None:
    """Execute sudo docker-compose * command"""
    os.system('sudo docker-compose ' + command)


@cli.command()
@click.pass_context
@click.argument('service', required=False)
def restart(ctx: click.Context, service: Any) -> None:
    """Restarts all stopped and running services, or the specified services only."""
    if service:
        # https://docs.docker.com/engine/reference/commandline/compose_restart/
        os.system('sudo docker-compose restart ' + service)
    else:
        # https://stackoverflow.com/questions/38221463/command-for-restarting-all-running-docker-containers
        # sudo docker restart $(docker ps -a -q)
        # sudo docker restart $(docker ps -q)
        # Restart all running containers
        os.system('sudo docker-compose restart')


@cli.command()
@click.pass_context
def configure(ctx: click.Context) -> None:
    """Configure local environment, will guide you through creating your .env and docker-compose.yml."""
    os.system('python3 install/configurator.py')


@cli.command()
@click.pass_context
@click.option('--env', default='magento_244',
              type=click.Choice(list_env_names(install_dir)),
              help="Build the development environment based on the specified configuration.")
def build(ctx: click.Context, env: Any) -> None:
    """Build local development environment with your configuration"""
    os.system('bash builder.sh ' + env)


@cli.command()
@click.pass_context
def start(ctx: click.Context) -> None:
    """Launch docker services"""
    click.echo(click.style(f"Start to launch docker services", fg='green'))
    os.system('bash bin/launch.sh')


@cli.command()
@click.pass_context
def stop(ctx: click.Context) -> None:
    """Stop docker services"""
    click.echo(click.style(f"Start to stop docker services", fg='green'))
    os.system('bash bin/stop.sh')


@cli.command()
@click.pass_context
@click.option('--dbname', required=True,
              help="Specify the database name to export or import.")
@click.option('--backup-sql-file',
              help="Specifies the backup SQL file path, "
                   "which can be used for imported source file and exported target file or directory. "
                   "The default is the specified file in the current directory.")
@click.argument('action', type=click.Choice(['import', 'export']), required=True)
def database(ctx: click.Context, action: Any, dbname: Any, backup_sql_file: Any) -> None:
    """Export or import database"""
    if dbname is None:
        click.echo(click.style(f"ERROR: Invalid database name", fg='red'))
        exit(1)
    if action == 'import':
        if backup_sql_file is None:
            click.echo(click.style(f"ERROR: Invalid source backup SQL file", fg='red'))
            exit(1)
        os.system('bash bin/import_db.sh ' + dbname + ' ' + backup_sql_file + ' ' + current_dir)
    elif action == 'export':
        command = 'bash bin/export_db.sh ' + dbname + ' ' + current_dir
        if backup_sql_file is not None:
            command += ' ' + backup_sql_file
        os.system(command)


@cli.command()
@click.pass_context
@click.argument('service', required=True)
def bash(ctx: click.Context, service: Any) -> None:
    """Bash session for running container"""
    os.system('bash bin/container_bash.sh ' + service)


@cli.command()
@click.pass_context
@click.option('--target-version',
              help="Specify the target version to upgrade. e.g: 1.0.1")
@click.option('--force/--no-force', default=False,
              help="Force or not force restart of services")
def upgrade(ctx: click.Context, target_version: Any, force: Any) -> None:
    """Upgrade Shinetech Docker"""
    command = 'bash bin/upgrade.sh '

    if force:
        command += ' y'
    else:
        command += ' n'

    if target_version is not None:
        command += ' ' + target_version

    os.system(command)

    click.echo(click.style(f"Upgraded successfully.", fg='green'))


@cli.command()
@click.pass_context
@click.option('--directory', default=get_default_workspace(),
              help="Specify the workspace directory. default is " + get_default_workspace())
def workspace(ctx: click.Context, directory: Any) -> None:
    """Initial workspace"""
    if directory is not None:
        os.system('bash bin/workspace.sh ' + directory)
    else:
        os.system('bash bin/workspace.sh')


@cli.command()
@click.pass_context
def about(ctx: click.Context) -> None:
    """Show the local environment and workspace information"""
    working_dir = ctx.obj['WORKING_DIR']
    env_handler = EnvHandler(working_dir=working_dir)
    env_values = env_handler.get_env_values()

    click.echo(click.style(f"Current environment:", fg='green', bold=True))
    click.echo(click.style(f" - {env_values['DEFAULT_ENV']}", fg='cyan'))

    click.echo(click.style(f"Your workspace information:", fg='green', bold=True))
    click.echo(click.style(f" - Workspace: {env_values['WORKSPACE']}", fg='cyan'))
    click.echo(
        click.style(f" - Project Directory: {env_values['DOCUMENT_ROOT']}", fg='cyan'))
    click.echo(click.style(f" - Nginx VHosts: {env_values['NGINX_VHOSTS_DIR']}", fg='cyan'))
    click.echo(click.style(f" - Nginx Log: {env_values['NGINX_LOG_DIR']}", fg='cyan'))
    click.echo(
        click.style(f" - Apache VHosts: {env_values['APACHE_VHOSTS_DIR']}", fg='cyan'))
    click.echo(click.style(f" - Apache Log: {env_values['APACHE_LOG_DIR']}", fg='cyan'))
    click.echo(click.style(f" - SSL CA: {env_values['SSL_CA_DIR']}", fg='cyan'))
    click.echo(click.style(f" - php.ini: {env_values['PHP_INI']}", fg='cyan'))
    click.echo(click.style(f" - Composer auth.json: {env_values['COMPOSER_AUTH_FILE']}", fg='cyan'))
    click.echo(click.style(f" - MySQL Log: {env_values['MYSQL_LOG_DIR']}", fg='cyan'))


@cli.command()
@click.pass_context
def envs(ctx: click.Context) -> None:
    """List all environments"""
    working_dir = ctx.obj['WORKING_DIR']
    env_handler = EnvHandler(working_dir=working_dir)
    env_table = env_handler.list_env_table()
    print(env_table)


@cli.command()
@click.pass_context
@click.option('--project-name', required=True,
              type=click.Choice(projects),
              help="Specify project name.")
@click.option('--db-sql-file', required=True,
              help="SQL backup file for initializing the database.")
@click.option('--vendor-file', required=False,
              help="Composer vendor file, pull from remote by default.")
@click.option('--country', required=False,
              help="Build project by country, such as HP project have multiple independent countries and regions.")
@click.option('--multiple-domain/--no-multiple-domain', default=False,
              help="Use multiple domains for multiple sites, single domain is used by default. "
                   "This option takes effect if --country is not empty. "
                   "e.g: For HP project, If No will use hp.dev.php9.cc for all country sites, "
                   "if Yes will use <country>.hp.dev.php9.cc for different sites.")
def setup_project(ctx: click.Context, project_name: Any, db_sql_file: Any, vendor_file: Any, country: Any, multiple_domain: Any) -> None:
    """Build a existing project based on existing code and database"""
    working_dir = ctx.obj['WORKING_DIR']
    env_handler = EnvHandler(working_dir=working_dir)
    env_values = env_handler.get_env_values()
    workspace_dir = env_values['WORKSPACE']
    current_env_configs = env_handler.get_current_env_configs()
    webserver = current_env_configs['services']['webserver']

    domain = project_name + base_domain
    if multiple_domain and country is not None:
        domain = project_name + '-' + country + base_domain

    project_dir = workspace_dir + '/www/' + domain
    if os.path.exists(project_dir):
        click.echo(click.style(f"WARNING: The project directory {project_dir} already exists.", fg='yellow'))
        click.confirm('Do you confirm to override and create project?', abort=True)

    command = 'bash bin/setup_project.sh ' \
              + current_dir + ' ' + workspace_dir + ' ' + webserver + ' ' + project_name

    if db_sql_file is not None:
        command += ' ' + db_sql_file
    else:
        command += ' ""'

    if vendor_file is not None:
        command += ' ' + vendor_file
    else:
        command += ' ""'

    if country is not None:
        command += ' ' + country
        if multiple_domain:
            command += ' y'
        else:
            command += ' n'

    os.system(command)


@cli.command()
@click.pass_context
@click.option('--platform', required=True, default='generic',
              type=click.Choice(php_platforms),
              help="Specifies the PHP framework used by the project.")
@click.option('--project-name', required=True,
              callback=check_project_name,
              help="Specify project name.")
@click.option('--target-version', required=False,
              help="Specify framework version. e.g: 2.4.5, 2.4.4-p1 for Magento")
def create_php_project(ctx: click.Context, platform: Any, project_name: Any, target_version: Any) -> None:
    """Create a new PHP project based on a base template or framework skeleton"""
    working_dir = ctx.obj['WORKING_DIR']
    env_handler = EnvHandler(working_dir=working_dir)
    env_values = env_handler.get_env_values()
    workspace_dir = env_values['WORKSPACE']
    current_env_configs = env_handler.get_current_env_configs()
    webserver = current_env_configs['services']['webserver']

    domain = project_name + base_domain

    project_dir = workspace_dir + '/www/' + domain
    if os.path.exists(project_dir):
        click.echo(click.style(f"WARNING: The project directory {project_dir} already exists.", fg='yellow'))
        click.confirm('Do you confirm to override and create project?', abort=True)

    command = 'bash bin/create_php_project.sh ' \
              + current_dir + ' ' + workspace_dir + ' ' + webserver + ' ' + platform + ' ' + project_name
    if target_version is not None:
        command += ' ' + target_version

    os.system(command)


@cli.command()
@click.pass_context
@click.option('--platform', required=True,
              type=click.Choice(js_platforms),
              help="Specifies the Javascript framework used by the project.")
@click.option('--project-name', required=True,
              callback=check_project_name,
              help="Specify project name.")
@click.option('--programming-language', required=False, default='javascript',
              type=click.Choice(js_languages),
              help="Specify programming language. e.g: JavaScript or TypeScript")
def create_js_project(ctx: click.Context, platform: Any, project_name: Any, programming_language: Any) -> None:
    """Create a new Javascript project based on a base template or framework skeleton"""
    working_dir = ctx.obj['WORKING_DIR']
    env_handler = EnvHandler(working_dir=working_dir)
    env_values = env_handler.get_env_values()
    workspace_dir = env_values['WORKSPACE']
    current_env_configs = env_handler.get_current_env_configs()
    webserver = current_env_configs['services']['webserver']

    domain = project_name + base_domain

    project_dir = workspace_dir + '/www/' + domain
    if os.path.exists(project_dir):
        click.echo(click.style(f"WARNING: The project directory {project_dir} already exists.", fg='yellow'))
        click.confirm('Do you confirm to override and create project?', abort=True)

    command = 'bash bin/create_js_project.sh ' \
              + current_dir + ' ' + workspace_dir + ' ' + webserver + ' ' + platform + ' ' + project_name
    if programming_language is not None:
        command += ' ' + programming_language

    os.system(command)


@cli.command()
@click.pass_context
@click.option('--target-version', required=True,
              help="Specify Magento version. e.g: 2.4.5, 2.4.4-p1")
@click.option('--source-code-file', required=False,
              help="Specify Magento original source code file. "
                   "If not specified, composer will be used for installation, "
                   "otherwise the specified source code package will be used.")
@click.option('--project-name', required=False,
              callback=check_project_name,
              help="Specify project name.")
def create_magento_project(ctx: click.Context, target_version: Any, source_code_file: Any, project_name: Any) -> None:
    """Create a new Magento project based on the source code or composer"""
    working_dir = ctx.obj['WORKING_DIR']
    env_handler = EnvHandler(working_dir=working_dir)
    env_values = env_handler.get_env_values()
    workspace_dir = env_values['WORKSPACE']
    current_env_configs = env_handler.get_current_env_configs()
    webserver = current_env_configs['services']['webserver']

    if target_version is not None:
        # 2.4.5 > 245
        version = convert_version(target_version)
        project_name = 'm' + version  # e.g: m245

    project_domain = project_name + base_domain

    project_dir = workspace_dir + '/www/' + project_domain
    if os.path.exists(project_dir):
        click.echo(click.style(f"WARNING: The project directory {project_dir} already exists.", fg='yellow'))
        click.confirm('Do you confirm to override and create project?', abort=True)

    command = 'bash bin/create_magento_project.sh ' \
              + current_dir + ' ' + workspace_dir + ' ' + webserver + ' ' + project_name + ' ' + target_version
    if source_code_file is not None:
        command += ' ' + source_code_file

    os.system(command)


@cli.command()
@click.pass_context
def status(ctx: click.Context) -> None:
    """List all running containers"""
    os.system('sudo docker-compose ps')


@cli.command()
@click.pass_context
@click.argument('service', required=True)
@click.option('--network-mode', required=False, default="bridge",
              type=click.Choice(network_modes),
              help="The type of network a container uses.")
def switch_network(ctx: click.Context, service: Any, network_mode: Any) -> None:
    """Switch network mode for a container"""
    os.system('bash bin/switch_network.sh ' + service + ' ' + network_mode)


@cli.command()
@click.pass_context
@click.option('--edit-mode/--no-edit-mode', default=False,
              help="Edit or show configuration of docker-compose.yml")
def editor(ctx: click.Context, edit_mode: Any) -> None:
    """Edit or show configuration of docker-compose.yml"""
    if edit_mode:
        os.system('vim docker-compose.yml')
    else:
        os.system('cat docker-compose.yml')


def main():
    cli()


if __name__ == '__main__':
    main()
