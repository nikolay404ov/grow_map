CREATE SCHEMA IF NOT EXISTS grow_map;

CREATE TABLE IF NOT EXISTS grow_map.person (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    description TEXT,
    created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    modified TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS grow_map.card (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    person_id uuid NOT NULL,
    skill TEXT NOT NULL,
    progress TEXT,
    comment TEXT,
    created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    modified TIMESTAMPTZ NOT NULL DEFAULT NOW()
);


INSERT INTO grow_map.person (id, name, description) VALUES ('3d825f60-9fff-4dfe-b294-1a45fa1e115d', 'Stas', 'project manager');
INSERT INTO grow_map.person (id, name, description) VALUES ('0312ed51-8833-413f-bff5-0e139c11264a', 'Nikolay', 'data engineer');

INSERT INTO grow_map.card (person_id, skill, progress) VALUES ('3d825f60-9fff-4dfe-b294-1a45fa1e115d', 'Managing', 'awesome');
INSERT INTO grow_map.card (person_id, skill, progress) VALUES ('3d825f60-9fff-4dfe-b294-1a45fa1e115d', 'Frontend', 'good');

INSERT INTO grow_map.card (person_id, skill, progress) VALUES ('0312ed51-8833-413f-bff5-0e139c11264a', 'Backend', 'good');
INSERT INTO grow_map.card (person_id, skill, progress) VALUES ('0312ed51-8833-413f-bff5-0e139c11264a', 'SQL', 'good');
INSERT INTO grow_map.card (person_id, skill, progress) VALUES ('0312ed51-8833-413f-bff5-0e139c11264a', 'Memes', 'awesome');
INSERT INTO grow_map.card (person_id, skill, progress) VALUES ('0312ed51-8833-413f-bff5-0e139c11264a', 'Frontend', 'bad');
