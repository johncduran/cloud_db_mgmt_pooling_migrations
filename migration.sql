CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 406f916ce18d

ALTER TABLE patients ADD COLUMN is_alive VARCHAR(50) NOT NULL;

ALTER TABLE patients MODIFY contact_number VARCHAR(100) NULL;

INSERT INTO alembic_version (version_num) VALUES ('406f916ce18d');

-- Running upgrade 406f916ce18d -> 4dbd1a64242c

ALTER TABLE patients ADD COLUMN is_breathing VARCHAR(50) NOT NULL;

UPDATE alembic_version SET version_num='4dbd1a64242c' WHERE alembic_version.version_num = '406f916ce18d';

