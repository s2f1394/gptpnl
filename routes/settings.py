from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3
import os

settings_bp = Blueprint('settings', __name__)
DB_PATH = 'db/gptpnl.db'

# ایجاد جدول تنظیمات اگر وجود نداشته باشد
def init_settings_table():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        ''')

init_settings_table()

@settings_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        data = request.form.to_dict()
        with sqlite3.connect(DB_PATH) as conn:
            for key, value in data.items():
                conn.execute('''
                    INSERT INTO settings (key, value)
                    VALUES (?, ?)
                    ON CONFLICT(key) DO UPDATE SET value=excluded.value
                ''', (key, value))
        return redirect(url_for('settings.settings'))

    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute('SELECT key, value FROM settings').fetchall()
        current_settings = {row[0]: row[1] for row in rows}
    return render_template('settings.html', settings=current_settings)
