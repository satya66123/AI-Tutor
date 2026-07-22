"""
Enterprise Document Index Service
"""

from services.document_service import DocumentService
from services.chunk_service import ChunkService
from services.embedding_service import EmbeddingService
from services.faiss_service import FAISSService
from services.metadata_service import MetadataService
from services.mysql_service import MySQLService


class DocumentIndexService:

    @staticmethod
    def index_documents(
        uploaded_files,
        chunk_strategy="Fixed",
        chunk_size=512,
        overlap=100
    ):

        faiss = FAISSService()

        total_documents = 0
        total_chunks = 0

        for file in uploaded_files:

            text = DocumentService.read(file)

            chunks = ChunkService.create_chunks(
                text=text,
                strategy=chunk_strategy,
                chunk_size=chunk_size,
                overlap=overlap
            )

            embeddings = EmbeddingService.generate_batch(
                chunks
            )

            metadata = []

            for index, chunk in enumerate(chunks):

                metadata.append(

                    MetadataService.create(
                        document=file.name,
                        chunk_id=index,
                        page=1,
                        chapter="",
                        topic="",
                        text=chunk
                    )

                )

            faiss.add(
                embeddings,
                metadata
            )

            document_id = MySQLService.save_document(
                file_name=file.name,
                file_type=file.name.split(".")[-1],
                file_size=getattr(file, "size", 0)
            )

            for index, chunk in enumerate(chunks):
                chunk_id = MySQLService.save_chunk(
                    document_id=document_id,
                    chunk_index=index,
                    chunk_text=chunk
                )

                MySQLService.execute(
                    """
                    INSERT INTO embeddings
                    (
                        chunk_id,
                        embedding
                    )
                    VALUES
                    (
                        %s,
                        %s
                    )
                    """,
                    (
                        chunk_id,
                        str(embeddings[index])
                    )
                )

            total_documents += 1
            total_chunks += len(chunks)

        faiss.save()

        return {

            "documents": total_documents,
            "chunks": total_chunks

        }