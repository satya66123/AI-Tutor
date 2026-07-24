class TransactionManager:

    def __init__(self, connection):

        self.connection = connection

    def begin(self):

        self.connection.start_transaction()

    def commit(self):

        self.connection.commit()

    def rollback(self):

        self.connection.rollback()

    def close(self):

        self.connection.close()