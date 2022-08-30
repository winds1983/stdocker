import os
import sys
import re
from typing import Any, Dict, List
from .core import get_env_values, list_envs, get_default_workspace, convert_version

try:
    import click
except ImportError:
    sys.stderr.write('It seems stdocker is not installed with cli option. \n'
                     'Run pip3 install "stdocker[cli]" to fix this.')
    sys.exit(1)

from .version import __version__

install_dir = '/opt/shinetech/stdocker'
current_dir = os.getcwd()


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
@click.version_option(version=__version__)
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
def run(ctx: click.Context, command: Any) -> None:
    """Execute sudo docker * command"""
    os.system('sudo docker ' + command)


@cli.command()
@click.pass_context
@click.argument('command', required=True)
def exec(ctx: click.Context, command: Any) -> None:
    """Execute sudo docker exec * command"""
    os.system('sudo docker exec ' + command)


@cli.command()
@click.pass_context
@click.argument('command', required=True)
def compose(ctx: click.Context, command: Any) -> None:
    """Execute sudo docker-compose * command"""
    os.system('sudo docker-compose ' + command)


@cli.command()
@click.pass_context
@click.argument('service', required=True)
def restart(ctx: click.Context, service: Any) -> None:
    """Restart specified docker service"""
    os.system('sudo docker-compose restart ' + service)


@cli.command()
@click.pass_context
def configure(ctx: click.Context) -> None:
    """Configure local environment, will guide you through creating your .env and docker-compose.yml."""
    os.system('python3 install/configurator.py')


@cli.command()
@click.pass_context
@click.option('--env', default='magento_244',
              type=click.Choice(list_envs(install_dir)),
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
        click.echo(click.style(f"Invalid database name", fg='red'))
        exit(1)
    if action == 'import':
        if backup_sql_file is None:
            click.echo(click.style(f"Invalid source backup SQL file", fg='red'))
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
    env_values = get_env_values(working_dir)

    click.echo(click.style(f"Current environment:", fg='yellow', bold=True))
    click.echo(click.style(f" - {env_values['DEFAULT_ENV']}", fg='cyan'))

    click.echo(click.style(f"Your workspace information:", fg='yellow', bold=True))
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
    click.echo(click.style(f" - MySQL Log: {env_values['MYSQL_LOG_DIR']}", fg='cyan'))


@cli.command()
@click.pass_context
@click.option('--platform', required=True, default='magento',
              type=click.Choice(['magento', 'symfony', 'laravel', 'yii', 'wordpress']),
              help="Specifies the framework used by the project.")
@click.option('--name', required=True,
              callback=check_project_name,
              help="Specify project name.")
@click.option('--db-sql-file', required=False,
              help="SQL backup file for initializing the database.")
@click.option('--country', required=False,
              help="Build project by country, such as HP project have multiple independent countries and regions.")
@click.option('--multiple-domain/--no-multiple-domain', default=False,
              help="Use multiple domains for multiple sites, single domain is used by default. "
                   "This option takes effect if --country is not empty. "
                   "e.g: For HP project, If No will use hp.dev.php9.cc for all country sites, "
                   "if Yes will use <country>.hp.dev.php9.cc for different sites.")
def init_project(ctx: click.Context, platform: Any, name: Any, db_sql_file: Any, country: Any, multiple_domain: Any) -> None:
    """Create a project based on a base template or existing code"""
    working_dir = ctx.obj['WORKING_DIR']
    env_values = get_env_values(working_dir)
    workspace_dir = env_values['WORKSPACE']

    domain = name + '.dev.php9.cc'
    if multiple_domain and country is not None:
        domain = name + '-' + country + '.dev.php9.cc'

    project_dir = workspace_dir + '/www/' + domain
    if os.path.exists(project_dir):
        click.echo(click.style(f"NOTE: The project directory {project_dir} already exists.", fg='cyan'))
        click.confirm('Do you confirm to override and create project?', abort=True)

    command = 'bash bin/init_project.sh ' + current_dir + ' ' + workspace_dir + ' ' + platform + ' ' + name

    if db_sql_file is not None:
        command += ' ' + db_sql_file
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
@click.option('--magento-version', required=True,
              help="Specifies Magento version.")
@click.option('--source-code-file', required=True,
              help="Specify Magento original source code file.")
@click.option('--project-name', required=False,
              callback=check_project_name,
              help="Specify project name.")
def init_magento(ctx: click.Context, magento_version: Any, source_code_file: Any, project_name: Any) -> None:
    """Create a project based on the original Magento code"""
    working_dir = ctx.obj['WORKING_DIR']
    env_values = get_env_values(working_dir)
    workspace_dir = env_values['WORKSPACE']

    if project_name is None:
        # 2.4.5 > 245
        version = convert_version(magento_version)
        project_name = 'm' + version  # e.g: m245

    project_domain = project_name + '.dev.php9.cc'

    project_dir = workspace_dir + '/www/' + project_domain
    if os.path.exists(project_dir):
        click.echo(click.style(f"NOTE: The Magento project {project_dir} already exists.", fg='cyan'))
        click.confirm('Do you confirm to override and create project?', abort=True)

    command = 'bash bin/init_magento.sh ' + current_dir + ' ' \
              + workspace_dir + ' ' + project_name + ' ' + source_code_file
    os.system(command)


def main():
    cli()


if __name__ == '__main__':
    main()
