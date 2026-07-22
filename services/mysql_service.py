"""
Enterprise MySQL Service
"""

from database.db_manager import DBManager
import json


class MySQLService:

    # ==========================================================
    # Generic Database Methods
    # ==========================================================

    @staticmethod
    def execute(sql, params=None):
        """
        Execute INSERT, UPDATE, DELETE.
        """
        return DBManager.execute(sql, params)

    @staticmethod
    def fetch_all(sql, params=None):
        """
        Fetch multiple records.
        """
        return DBManager.fetch_all(sql, params)

    @staticmethod
    def fetch_one(sql, params=None):
        """
        Fetch one record.
        """
        return DBManager.fetch_one(sql, params)

    # ==========================================================
    # Documents
    # ==========================================================

    @staticmethod
    def save_document(
            file_name,
            file_type,
            file_size=0
    ):
        """
        Save uploaded document.
        """

        sql = """
        INSERT INTO documents
        (
            file_name,
            file_type,
            file_size
        )
        VALUES
        (
            %s,
            %s,
            %s
        )
        """

        return DBManager.execute(
            sql,
            (
                file_name,
                file_type,
                file_size
            )
        )

    @staticmethod
    def get_documents():
        """
        Return all indexed documents.
        """

        sql = """
        SELECT
            id,
            file_name,
            file_type,
            file_size,
            uploaded_at
        FROM documents
        ORDER BY uploaded_at DESC
        """

        return DBManager.fetch_all(sql)

    @staticmethod
    def delete_document(document_id):
        """
        Delete document.
        """

        sql = """
        DELETE FROM documents
        WHERE id=%s
        """

        return DBManager.execute(
            sql,
            (
                document_id,
            )
        )

    # ==========================================================
    # Chunks
    # ==========================================================

    @staticmethod
    def save_chunk(
            document_id,
            chunk_index,
            chunk_text
    ):
        """
        Save document chunk.
        """

        sql = """
        INSERT INTO document_chunks
        (
            document_id,
            chunk_index,
            chunk_text
        )
        VALUES
        (
            %s,
            %s,
            %s
        )
        """

        return DBManager.execute(
            sql,
            (
                document_id,
                chunk_index,
                chunk_text
            )
        )

    @staticmethod
    def get_chunks(document_id):
        """
        Get chunks for a document.
        """

        sql = """
        SELECT
            *
        FROM document_chunks
        WHERE document_id=%s
        ORDER BY chunk_index
        """

        return DBManager.fetch_all(
            sql,
            (
                document_id,
            )
        )

    # ==========================================================
    # Retrieval History
    # ==========================================================

    @staticmethod
    def save_retrieval(
            query,
            response_time=0,
            provider="",
            model=""
    ):
        """
        Save retrieval history.
        """

        sql = """
        INSERT INTO retrieval_history
        (
            query,
            response_time,
            provider,
            model
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s
        )
        """

        return DBManager.execute(
            sql,
            (
                query,
                response_time,
                provider,
                model
            )
        )

    @staticmethod
    def get_history(limit=50):
        """
        Get recent retrieval history.
        """

        sql = """
        SELECT
            *
        FROM retrieval_history
        ORDER BY created_at DESC
        LIMIT %s
        """

        return DBManager.fetch_all(
            sql,
            (
                limit,
            )
        )

    # ==========================================================
    # RAG Cache
    # ==========================================================


    @staticmethod
    def save_cache(
            question_hash,
            question,
            result,
            provider,
            model
    ):
        sql = """
        INSERT INTO rag_cache
        (
            question_hash,
            question,
            answer,
            result_json,
            provider,
            model
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
        ON DUPLICATE KEY UPDATE

            answer=VALUES(answer),
            result_json=VALUES(result_json),
            provider=VALUES(provider),
            model=VALUES(model),
            hits=hits+1,
            created_at=CURRENT_TIMESTAMP
        """

        DBManager.execute(

            sql,

            (

                question_hash,

                question,

                result["answer"],

                json.dumps(result),

                provider,

                model

            )

        )


    @staticmethod
    def get_cache(question_hash):
        sql = """
        SELECT result_json
        FROM rag_cache
        WHERE question_hash=%s
        """

        row = DBManager.fetch_one(

            sql,

            (

                question_hash,

            )

        )

        if row is None:
            return None

        return json.loads(row["result_json"])

    # ==========================================================
    # Search History
    # ==========================================================

    @staticmethod
    def save_search(

            question,

            answer,

            total_results,

            response_time,

            provider,

            model,

            search_type

    ):
        sql = """
        INSERT INTO search_history
        (

            question,

            answer,

            total_results,

            response_time,

            provider,

            model,

            search_type

        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
        """

        return DBManager.execute(

            sql,

            (

                question,

                answer,

                total_results,

                response_time,

                provider,

                model,

                search_type

            )

        )

    @staticmethod
    def get_search_history(limit=20):
        sql = """
        SELECT
            *
        FROM search_history
        ORDER BY created_at DESC
        LIMIT %s
        """

        return DBManager.fetch_all(

            sql,

            (

                limit,

            )

        )