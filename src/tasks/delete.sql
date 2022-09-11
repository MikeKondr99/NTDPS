
PRAGMA foreign_keys=off;
BEGIN TRANSACTION;

ALTER TABLE client RENAME TO _client_old;

CREATE TABLE client
(
    first_name TEXT,
    last_name  TEXT
);

INSERT INTO client SELECT first_name, last_name FROM _client_old;
DROP TABLE _client_old;

COMMIT;
PRAGMA foreign_keys=on;