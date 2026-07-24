class BaseRepository:

    def __init__(self, connection):

        self.connection = connection

        self.cursor = connection.cursor(dictionary=True)

    def execute(self, sql, params=None):

        self.cursor.execute(sql, params or ())

        self.connection.commit()

    def fetchone(self, sql, params=None):

        self.cursor.execute(sql, params or ())

        return self.cursor.fetchone()

    def fetchall(self, sql, params=None):

        self.cursor.execute(sql, params or ())

        return self.cursor.fetchall()

    def close(self):

        self.cursor.close()