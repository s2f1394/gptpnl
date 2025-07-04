-- ساخت جدول کاربران
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

-- ساخت جدول کانفیگ‌ها
CREATE TABLE IF NOT EXISTS configs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    protocol TEXT,
    config_json TEXT,
    tags TEXT,
    created_at TEXT
);

-- ساخت جدول پیام‌ها برای GPT
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT,
    content TEXT,
    timestamp TEXT
);

-- ساخت جدول تنظیمات پنل
CREATE TABLE IF NOT EXISTS settings (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    site_title TEXT,
    admin_email TEXT,
    api_key TEXT,
    telegram_proxy_enabled INTEGER DEFAULT 0,
    created_at TEXT
);
