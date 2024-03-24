DROP TABLE IF EXISTS local;
DROP TABLE IF EXISTS local_data;

CREATE TABLE IF NOT EXISTS local (
    id SERIAL PRIMARY KEY,
    email TEXT NOT NULL,
    data DATE NOT NULL
);

INSERT INTO local (email, data) VALUES ("teste@teste.com", "14/03/2024");
INSERT INTO local (email, data) VALUES ("teste@teste.com", "14/03/2024");
