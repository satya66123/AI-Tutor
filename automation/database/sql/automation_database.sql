CREATE DATABASE IF NOT EXISTS ai_tutor;

USE ai_tutor;

-- ======================================================
-- Workflows
-- ======================================================

CREATE TABLE IF NOT EXISTS workflows (

    workflow_id VARCHAR(64) PRIMARY KEY,

    workflow_name VARCHAR(100) NOT NULL,

    description TEXT,

    status VARCHAR(30) NOT NULL,

    created_at DATETIME,

    updated_at DATETIME

);

-- ======================================================
-- Workflow Tasks
-- ======================================================

CREATE TABLE IF NOT EXISTS workflow_tasks (

    task_id VARCHAR(64) PRIMARY KEY,

    workflow_id VARCHAR(64) NOT NULL,

    task_name VARCHAR(100),

    task_type VARCHAR(100),

    status VARCHAR(30),

    retry_count INT DEFAULT 0,

    execution_time DOUBLE,

    started_at DATETIME,

    completed_at DATETIME,

    error TEXT,

    CONSTRAINT fk_task_workflow
        FOREIGN KEY (workflow_id)
        REFERENCES workflows(workflow_id)
        ON DELETE CASCADE

);

-- ======================================================
-- Workflow Executions
-- ======================================================

CREATE TABLE IF NOT EXISTS workflow_execution (

    execution_id VARCHAR(64) PRIMARY KEY,

    workflow_id VARCHAR(64) NOT NULL,

    started_at DATETIME,

    completed_at DATETIME,

    duration DOUBLE,

    status VARCHAR(30),

    CONSTRAINT fk_execution_workflow
        FOREIGN KEY (workflow_id)
        REFERENCES workflows(workflow_id)
        ON DELETE CASCADE

);

-- ======================================================
-- Workflow Schedule
-- ======================================================

CREATE TABLE IF NOT EXISTS workflow_schedule (

    schedule_id VARCHAR(64) PRIMARY KEY,

    workflow_id VARCHAR(64) NOT NULL,

    schedule_type VARCHAR(30),

    cron_expression VARCHAR(100),

    next_run DATETIME,

    last_run DATETIME,

    is_active BOOLEAN DEFAULT TRUE,

    CONSTRAINT fk_schedule_workflow
        FOREIGN KEY (workflow_id)
        REFERENCES workflows(workflow_id)
        ON DELETE CASCADE

);

-- ======================================================
-- Workflow Logs
-- ======================================================

CREATE TABLE IF NOT EXISTS workflow_logs (

    log_id VARCHAR(64) PRIMARY KEY,

    workflow_id VARCHAR(64) NOT NULL,

    task_id VARCHAR(64),

    log_level VARCHAR(20),

    message TEXT,

    created_at DATETIME,

    CONSTRAINT fk_log_workflow
        FOREIGN KEY (workflow_id)
        REFERENCES workflows(workflow_id)
        ON DELETE CASCADE

);

-- ======================================================
-- Indexes
-- ======================================================

CREATE INDEX idx_workflow_status
ON workflows(status);

CREATE INDEX idx_task_workflow
ON workflow_tasks(workflow_id);

CREATE INDEX idx_execution_workflow
ON workflow_execution(workflow_id);

CREATE INDEX idx_schedule_workflow
ON workflow_schedule(workflow_id);

CREATE INDEX idx_log_workflow
ON workflow_logs(workflow_id);

CREATE INDEX idx_log_task
ON workflow_logs(task_id);