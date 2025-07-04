-- init.sql

-- جدول کاربران
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    plan TEXT,
    traffic INTEGER,
    max_devices INTEGER,
    start_date TEXT,
    end_date TEXT,
    status TEXT
);

-- جدول کانفیگ‌ها
CREATE TABLE IF NOT EXISTS configs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    protocol TEXT,
    config_json TEXT,
    tags TEXT,
    created_at TEXT
);
