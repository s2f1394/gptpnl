from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime, timedelta
import random
import string
import os

users_bp = Blueprint('users', __name__)
DB_PATH = 'db/gptpnl.db'

# لیست کاربران
@users_bp.route('/users')
def list_users():
    with sqlite3.connect(DB_PATH) as conn:
        users = conn.execute('SELECT * FROM users').fetchall()
    return render_template('users/list.html', users=users)

# افزودن کاربر
@users_bp.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name') or 'user_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        plan = request.form.get('plan')
        traffic = int(request.form.get('traffic'))
        max_devices = int(request.form.get('max_devices'))
        single_device = 1 if request.form.get('single_device') == 'on' else 0
        start_date = datetime.utcnow()
        end_date = start_date + timedelta(days=30)

        with sqlite3.connect(DB_PATH) as conn:
            conn.execute('''
                INSERT INTO users (name, plan, traffic, max_devices, start_date, end_date, status, single_device)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, plan, traffic, max_devices, start_date.isoformat(), end_date.isoformat(), 'active', single_device))

        return redirect(url_for('users.list_users'))

    return render_template('users/add.html')
