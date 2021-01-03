import psycopg3

from datetime import datetime
from peewee import (Model, CharField, TextField, DateTimeField, DateField, ForeignKeyField,
    PostgresqlDatabase)

from .settings import config

db_config = config.get('db', {})

pg_db = PostgresqlDatabase(
    'comuna', user=db_config.get('user'), password=db_config.get('password'),
    host=db_config.get('host'), port=db_config.get('port'))


class User(Model):
    username = CharField(
        max_length=30, null=False, unique=True, verbose_name='Username')
    email = CharField(
        max_length=255, null=True, unique=True, verbose_name='E-Mail')
    password = CharField(
        max_length=64, null=False)
    first_name = CharField(
        max_length=50, null=True)
    last_name = CharField(
        max_length=50, null=True)
    description = TextField(
        null=True, help_text=('Personal description of the user for the profile'))
    icon = CharField(
        max_length=50, null=True, default='default.png')
    birthday = DateField(
        null=True)
    created_at = DateTimeField(
        default=datetime.now, null=False)
    updated_at = DateTimeField(
        default=datetime.now, null=False)

    @property
    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'description': self.description,
            'icon': self.icon,
            'birthday': self.birthday,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }

    class Meta:
        database = pg_db
        table_name = 'users'


class Article(Model):
    user = ForeignKeyField(User, backref='users')
    title = CharField(
        max_length=255, null=False)
    content = TextField(
        null=True)
    created_at = DateTimeField(
        default=datetime.now, null=False)
    updated_at = DateTimeField(
        default=datetime.now, null=False)

    class Meta:
        database = pg_db
        table_name = 'articles'
