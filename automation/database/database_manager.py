from mysql.connector.pooling import MySQLConnectionPool

from automation.database.database_config import DatabaseConfig


class DatabaseManager:

    def __init__(self, config: DatabaseConfig):

        self.pool = MySQLConnectionPool(

            pool_name="automation_pool",

            pool_size=config.pool_size,

            host=config.host,

            port=config.port,

            user=config.user,

            password=config.password,

            database=config.database

        )

    def get_connection(self):

        return self.pool.get_connection()