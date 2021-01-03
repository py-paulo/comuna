import os
import sys
import click
import getpass
import requests
import pprint

pp = pprint.PrettyPrinter(indent=2, compact=True, width=51)

def write_output(msg: str, isexit: bool = True) -> None:
    print(msg)
    if isexit:
        sys.exit(1)

def _login(user, passwd):
    r = requests.post(
        url='http://localhost:8000/auth',
        json={
            'username': user, 'password': passwd
        },
        headers={'Content-Type': 'application/json'})
    return r.json()

def _get_user(user, passwd, userid):
    token = _login(user, passwd).get('access_token')
    r = requests.get(
        url='http://localhost:8000/user/%s' % userid,
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token})
    return r.json()


@click.command()
@click.argument('action', type=click.Choice(['login', 'get-user'], case_sensitive=False))
@click.option('-u', '--user', default=None, type=str, help=('username from login in api.'))
@click.option('-ui', '--user-id', default=None, type=str, help=('user id from get info.'))
def cli(action: str, user, user_id):
    if action.lower().startswith('login'):
        if user is None:
            write_output('[-u, --user] parameter is required for this subcommand')

        os_env_passwd = os.getenv('API_PASSWORD', None)
        passwd = getpass.getpass(prompt='password: ') if not os_env_passwd else os_env_passwd

        pp.pprint(_login(user, passwd))
    if action.lower().startswith('get-user'):
        if user_id is None or user is None:
            write_output('[-iu, --user-id] and [-u, --user] parameter is required for this subcommand')
        
        os_env_passwd = os.getenv('API_PASSWORD', None)
        passwd = getpass.getpass(prompt='password: ') if not os_env_passwd else os_env_passwd
        
        pp.pprint(_get_user(user, passwd, user_id))

if __name__ == "__main__":
    cli()