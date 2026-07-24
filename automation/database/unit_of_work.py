from automation.database.repository_factory import RepositoryFactory


class UnitOfWork:

    def __init__(self, connection):

        self.connection = connection

        self.repositories = RepositoryFactory(connection)

    def __enter__(self):

        return self

    def commit(self):

        self.connection.commit()

    def rollback(self):

        self.connection.rollback()

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type:

            self.rollback()

        else:

            self.commit()

        self.connection.close()