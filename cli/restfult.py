import os
import sys
import click
import getpass
import requests
import pprint

pp = pprint.PrettyPrinter(
    indent=2, compact=True, width=51)


def _get_pass() -> str:
    env_pass = os.getenv('API_PASSWORD', None)
    if env_pass is None:
        return getpass.getpass(prompt='password >> ')
    return env_pass


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


@click.group()
def cli():
    pass


@click.command(name='login')
@click.argument('user', default=None, type=str)
def login(user):
    passwd = _get_pass()
    pp.pprint(_login(user, passwd))


@click.command(name='get-user')
@click.argument('user', default=None, type=str)
@click.argument('userid', default=None, type=str)
def get_user(user, userid):
    passwd = _get_pass()
    pp.pprint(_get_user(user, passwd, userid))


cli.add_command(login)
cli.add_command(get_user)

if __name__ == '__main__':
    cli()