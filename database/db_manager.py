"""
Enterprise Database Manager
"""

from database.db_connection import DBConnection


class DBManager:

    # ==========================================================
    # Execute INSERT / UPDATE / DELETE
    # ==========================================================

    @staticmethod
    def execute(query, params=None):

        connection = None
        cursor = None

        try:

            connection = DBConnection.get_connection()

            cursor = connection.cursor()

            cursor.execute(query, params or ())

            connection.commit()

            return cursor.lastrowid

        except Exception as e:

            if connection:
                connection.rollback()

            raise e

        finally:

            if cursor:
                cursor.close()

            if connection and connection.is_connected():
                connection.close()

    # ==========================================================
    # Fetch Single Record
    # ==========================================================

    @staticmethod
    def fetch_one(query, params=None):

        connection = None
        cursor = None

        try:

            connection = DBConnection.get_connection()

            cursor = connection.cursor(dictionary=True)

            cursor.execute(query, params or ())

            return cursor.fetchone()

        finally:

            if cursor:
                cursor.close()

            if connection and connection.is_connected():
                connection.close()

    # ==========================================================
    # Fetch Multiple Records
    # ==========================================================

    @staticmethod
    def fetch_all(query, params=None):

        connection = None
        cursor = None

        try:

            connection = DBConnection.get_connection()

            cursor = connection.cursor(dictionary=True)

            cursor.execute(query, params or ())

            return cursor.fetchall()

        finally:

            if cursor:
                cursor.close()

            if connection and connection.is_connected():
                connection.close()

    # ==========================================================
    # Fetch Scalar Value
    # ==========================================================

    @staticmethod
    def fetch_value(query, params=None):

        row = DBManager.fetch_one(query, params)

        if row:

            return next(iter(row.values()))

        return None

    # ==========================================================
    # Record Exists
    # ==========================================================

    @staticmethod
    def exists(query, params=None):

        return DBManager.fetch_one(query, params) is not None

    # ==========================================================
    # Execute Many
    # ==========================================================

    @staticmethod
    def execute_many(query, values):

        connection = None
        cursor = None

        try:

            connection = DBConnection.get_connection()

            cursor = connection.cursor()

            cursor.executemany(query, values)

            connection.commit()

            return cursor.rowcount

        except Exception as e:

            if connection:
                connection.rollback()

            raise e

        finally:

            if cursor:
                cursor.close()

            if connection and connection.is_connected():
                connection.close()

    # ==========================================================
    # Execute Transaction
    # ==========================================================

    @staticmethod
    def execute_transaction(queries):

        """
        queries = [
            (sql1, params1),
            (sql2, params2),
            ...
        ]
        """

        connection = None
        cursor = None

        try:

            connection = DBConnection.get_connection()

            cursor = connection.cursor()

            for sql, params in queries:

                cursor.execute(sql, params or ())

            connection.commit()

            return True

        except Exception as e:

            if connection:
                connection.rollback()

            raise e

        finally:

            if cursor:
                cursor.close()

            if connection and connection.is_connected():
                connection.close()