from automation.database.database_manager import DatabaseManager
from automation.database.repository_factory import RepositoryFactory


class PersistenceService:

    def __init__(self, config):

        self.database = DatabaseManager(config)

    def repositories(self):

        connection = self.database.get_connection()

        return RepositoryFactory(connection)

    @staticmethod
    def close(repository):

        repository.connection.close()