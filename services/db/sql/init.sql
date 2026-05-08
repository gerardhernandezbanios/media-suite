CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE photos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    path TEXT NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE photo_hashes (
    photo_id UUID NOT NULL REFERENCES photos(id) ON DELETE CASCADE,
    phash TEXT,
    ahash TEXT,
    dhash TEXT,
    PRIMARY KEY (photo_id)
);

CREATE TABLE photo_tags (
    photo_id UUID NOT NULL REFERENCES photos(id) ON DELETE CASCADE,
    tag TEXT NOT NULL,
    PRIMARY KEY (photo_id, tag)
);
