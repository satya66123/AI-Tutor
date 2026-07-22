"""
Enterprise Document Manager Service
"""

from services.mysql_service import MySQLService
from services.index_manager import IndexManager


class DocumentManagerService:

    @staticmethod
    def get_documents():
        """
        Return all indexed documents.
        """
        return MySQLService.get_documents()

    @staticmethod
    def delete_document(document_id):
        """
        Delete a document from the database.
        """

        MySQLService.delete_document(document_id)

    @staticmethod
    def rebuild_index():
        """
        Rebuild the FAISS index.
        """

        IndexManager.rebuild()

    @staticmethod
    def get_statistics():
        """
        Return index statistics.
        """

        return IndexManager.statistics()