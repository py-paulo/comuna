import psycopg3

from typing import Tuple, List


class Pgpy:

    conn = None

    def __init__(
            self,
            user: str,
            password: str,
            dbname: str,
            host: str = 'localhost',
            port: int = 5432,
            connect_timeout: int = 10) -> None:
        self.conn = Pgpy.create_connection(
            user, password, dbname, host, port, connect_timeout)

    @classmethod
    def create_connection(
            cls, user, password, dbname, host, port, connect_timeout) -> psycopg3.Connection:
        return psycopg3.connect("host=%s port=%s dbname=%s connect_timeout=%s user=%s password=%s" % (
            host, port, dbname, connect_timeout, user, password
        ))

    @classmethod
    def __asset_connection(cls) -> bool:
        pass
    
    @staticmethod
    def __create_table_users(conn) -> Tuple[bool, int, str]:
        table = ("""
            CREATE TABLE users (
                id serial PRIMARY KEY,
                username text,
                password text)
            """)
    
    @classmethod
    def __create_table_articles(cls, conn) -> Tuple[bool, int, str]:
        table = ("""
            CREATE TABLE articles (
                id serial PRIMARY KEY,
                title text,
                content text)
            """)
    
    @classmethod
    def create_table_users(cls, conn: psycopg3.Connection) -> Tuple[bool, str]:
        istrue, code, msg = Pgpy.__create_table_users(conn)

        return istrue, 'users'

    @classmethod
    def create_table_articles(cls, conn: psycopg3.Connection) -> Tuple[bool, str]:
        istrue, code, msg = Pgpy.__create_table_articles(conn)

        return istrue, 'articles'

    @classmethod
    def create_tables(cls) -> List[Tuple[bool, str]]:
        tables = [
            cls.create_table_users,
            cls.create_table_users
        ]
