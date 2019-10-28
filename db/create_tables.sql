CREATE TABLE video_details (
    ref_id INTEGER PRIMARY KEY,
    video_link TEXT NOT NULL,
    video_filename TEXT NOT NULL,
    test_type TEXT,
    amplitude_level INTEGER,
    face TEXT,
    num_nystagmus_events INTEGER,
    hgn_max_side TEXT
);