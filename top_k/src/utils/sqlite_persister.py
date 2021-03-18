import logging

import setting
from utils.data_persisters import DataPersister
import sqlite3
from sqlite3 import Error

log = logging.getLogger(__name__)


class SqlLitePersister(DataPersister):

    def validate_target(self):
        if setting.SQLITE_OUTPUT_ACTIVE:
            return self.create_connection(setting.SQLITE_OUTPUT_FILE)

        return False

    def create_connection(self, db_file) -> bool:
        """ create a database connection to a SQLite database """
        valid = False
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            valid = True
        except Error as e:
            log.exception(e)
            valid = False
        finally:
            if conn:
                conn.close()

        return valid

    def create_table(self, table_name: str):
        create_table_sql = f"""
        -- 
        CREATE TABLE IF NOT EXISTS {table_name} (
            word text NOT NULL,
            count int
        );
        """
        conn = None
        try:
            conn = sqlite3.connect(setting.SQLITE_OUTPUT_FILE)

            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            log.exception(e)
            raise e
        finally:
            if conn:
                conn.close()


def persist(self, dict1: dict, project_name):
    pass
