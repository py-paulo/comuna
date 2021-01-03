import psycopg3

from peewee import *

from datetime import datetime

pg_db = PostgresqlDatabase(
    'comuna',
    user='',
    password='',
    host='localhost',
    port=5432)


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
