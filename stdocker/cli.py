import json
import os
import shlex
import sys
from subprocess import Popen
from typing import Any, Dict, List
from core import get_env_values

try:
    import click
except ImportError:
    sys.stderr.write('It seems stdocker is not installed with cli option. \n'
                     'Run pip install "stdocker[cli]" to fix this.')
    sys.exit(1)

# from .main import dotenv_values, get_key, set_key, unset_key
# from .version import __version__
__version__ = '1.0.0'


@click.group()
@click.option('-d', '--working-dir', default='/opt/shinetech/stdocker',
              type=click.Path(dir_okay=True),
              help="Location of the installation directory, defaults to /opt/shinetech/stdocker.")
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx: click.Context, working_dir: Any) -> None:
    """Shinetech Docker CLI"""
    ctx.obj = {}
    ctx.obj['WORKING_DIR'] = working_dir
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
    """Restart docker service"""
    os.system('sudo docker-compose restart ' + service)


@cli.command()
@click.pass_context
@click.argument('env', required=True)
def configure(ctx: click.Context, env: Any) -> None:
    """Configure local environment, will guide you through creating your .env and docker-compose.yml."""
    os.system('python3 install/configurator.py')


@cli.command()
@click.pass_context
@click.option('--env', default='magento_244',
              type=click.Choice(['magento_244', 'json', 'shell', 'export']),
              help="The format in which to display the list. Default format is simple, "
                   "which displays name=value without quotes.")
def build(ctx: click.Context, env: Any) -> None:
    """Build local environment."""
    os.system('sh builder.sh ' + env)


@cli.command()
@click.pass_context
def launch(ctx: click.Context) -> None:
    """Launch docker services"""
    click.echo(click.style(f"Start to launch docker services", fg='cyan'))
    os.system('sh bin/launch.sh')


@cli.command()
@click.pass_context
def stop(ctx: click.Context) -> None:
    """Stop docker services"""
    click.echo(click.style(f"Start to stop docker services", fg='cyan'))
    os.system('sh bin/stop.sh')


@cli.command()
@click.pass_context
@click.option('--dbname', required=True,
              help="Specify the database name to export or import.")
@click.option('--backup_sql_file',
              help="Specifies the SQL file path for database backup, "
                   "which is placed in the var directory of docker by default.")
@click.argument('action', type=click.Choice(['import', 'export']), required=True)
def database(ctx: click.Context, action: Any, dbname: Any, backup_sql_file: Any) -> None:
    """Export or import database"""
    if dbname is None:
        click.echo(click.style(f"Invalid database name", fg='red'))
        exit(1)
    if action == 'import':
        if backup_sql_file is None:
            click.echo(click.style(f"Invalid backup SQL file", fg='red'))
            exit(1)
        os.system('sh bin/import_db.sh ' + dbname + ' ' + backup_sql_file)
    elif action == 'export':
        os.system('sh bin/export_db.sh ' + dbname)


@cli.command()
@click.pass_context
@click.argument('service', required=True)
def ssh(ctx: click.Context, service: Any) -> None:
    """SSH login to the specified server"""
    os.system('sh bin/ssh.sh ' + service)


@cli.command()
@click.pass_context
def upgrade(ctx: click.Context) -> None:
    """Upgrade Shinetech Docker"""
    os.system('sh bin/upgrade.sh')


@cli.command()
@click.pass_context
def about(ctx: click.Context) -> None:
    """Show the local env and workspace information"""
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
@click.option('--platform', required=True, default='magento2',
              type=click.Choice(['magento2', 'symfony', 'laravel', 'yii', 'wordpress']),
              help="Specify the database name to export or import.")
@click.option('--name', required=True,
              help="Specifies the SQL file path for database backup, "
                   "which is placed in the var directory of docker by default.")
def init_project(ctx: click.Context, platform: Any, name: Any) -> None:
    """Export or import database"""
    os.system('sh bin/init_project.sh ' + platform + ' ' + name)


if __name__ == '__main__':
    cli()
