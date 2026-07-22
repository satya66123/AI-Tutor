CREATE DATABASE IF NOT EXISTS ai_tutor;

USE ai_tutor;

-- ==========================================
-- Documents
-- ==========================================

CREATE TABLE documents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    file_size BIGINT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- Document Chunks
-- ==========================================

CREATE TABLE document_chunks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    document_id INT NOT NULL,
    chunk_number INT NOT NULL,
    chunk_text LONGTEXT NOT NULL,
    chunk_size INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (document_id)
        REFERENCES documents(id)
        ON DELETE CASCADE
);

-- ==========================================
-- Embedding Metadata
-- ==========================================

CREATE TABLE embedding_metadata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    document_id INT NOT NULL,
    chunk_id INT NOT NULL,
    embedding_model VARCHAR(100),
    vector_dimension INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (document_id)
        REFERENCES documents(id)
        ON DELETE CASCADE,
    FOREIGN KEY (chunk_id)
        REFERENCES document_chunks(id)
        ON DELETE CASCADE
);

-- ==========================================
-- Retrieval History
-- ==========================================

CREATE TABLE retrieval_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    query TEXT NOT NULL,
    total_results INT DEFAULT 0,
    search_type VARCHAR(50),
    response_time_ms INT,
    searched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- RAG Sessions
-- ==========================================

CREATE TABLE rag_sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    session_id VARCHAR(100),
    user_question LONGTEXT,
    ai_answer LONGTEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- Citations
-- ==========================================

CREATE TABLE citations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT NOT NULL,
    document_id INT NOT NULL,
    chunk_id INT NOT NULL,
    score FLOAT,
    FOREIGN KEY (session_id)
        REFERENCES rag_sessions(id)
        ON DELETE CASCADE,
    FOREIGN KEY (document_id)
        REFERENCES documents(id)
        ON DELETE CASCADE,
    FOREIGN KEY (chunk_id)
        REFERENCES document_chunks(id)
        ON DELETE CASCADE
);

-- ==========================================
-- Search Logs
-- ==========================================

CREATE TABLE search_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    query TEXT,
    provider VARCHAR(50),
    model VARCHAR(100),
    top_k INT,
    search_strategy VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);