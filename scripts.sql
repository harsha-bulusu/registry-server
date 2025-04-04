# create table

CREATE TABLE container_info (
    container_id VARCHAR PRIMARY KEY,
    container_name VARCHAR NOT NULL UNIQUE,
    created_by VARCHAR NOT NULL,
    app_name VARCHAR NOT NULL,
    container_alive BOOLEAN DEFAULT true NOT NULL,
    last_heartbeat TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);


# SET TIMEZONE
ALTER DATABASE your_db_name SET TIMEZONE TO 'UTC';

# GET TIMEZONE

SHOW TIMEZONE