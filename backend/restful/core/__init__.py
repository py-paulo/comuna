import psycopg3
import logging

from typing import Tuple, List, Any

logger = logging.getLogger(__name__)


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
        if self.conn is None:
            raise Exception("Could not connect to the database, please check log for more details.")

    @classmethod
    def create_connection(
            cls, user, password, dbname, host, port, connect_timeout) -> psycopg3.Connection:
        try:
            return psycopg3.connect("host=%s port=%s dbname=%s connect_timeout=%s user=%s password=%s" % (
                host, port, dbname, connect_timeout, user, password))
        except psycopg3.errors.OperationalError:
            logger.critical('connection failed: password authentication failed for user "%s"' % user)
            return None

    def __asset_connection(self) -> bool:
        pass

    def __create_table(self, table: str, throw: bool = False) -> Tuple[bool, int, str]:
        with self.conn.cursor() as cur:
            try:
                cur.execute(table)
            except psycopg3.errors.DuplicateTable:
                cur.execute("rollback")
                if throw:
                    raise Exception('psycopg3.errors.DuplicateTable: relation already exists')
                return False, 1, 'relation already exists'
            else:
                self.conn.commit()

            return True, 0, 'sucessful'

    def __create_table_users(self, throw: bool = False) -> Tuple[bool, int, str]:
        table = ("""
                CREATE TABLE users (
                    id serial PRIMARY KEY,
                    username text,
                    password text)
                """)
        return self.__create_table(table, throw=throw)
    
    def __create_table_articles(self, throw: bool = False) -> Tuple[bool, int, str]:
        table = ("""
            CREATE TABLE articles (
                id serial PRIMARY KEY,
                title text,
                content text)
            """)
        return self.__create_table(table, throw=throw)
    
    def create_table_users(self, throw: bool = False) -> Tuple[bool, str]:
        istrue, _, _ = self.__create_table_users()
        return istrue, 'users'

    def create_table_articles(self, throw: bool = False) -> Tuple[bool, str]:
        istrue, _, _ = self.__create_table_articles()
        return istrue, 'articles'

    def select(self, table: str) -> List[Any]:
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM %s" % table)

            return cur.fetchall()

    def create_tables(self, throw: bool = False) -> List[Tuple[bool, str]]:
        tables = [
            self.create_table_users,
            self.create_table_articles
        ]
        return [t(throw=throw) for t in tables]

    def insert(self, table: str, **kwargs):
        pass