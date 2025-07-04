
from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

configs_bp = Blueprint('configs', __name__)
DB_PATH = 'db/gptpnl.db'

@configs_bp.route('/configs')
def list_configs():
    with sqlite3.connect(DB_PATH) as conn:
        configs = conn.execute('SELECT * FROM configs').fetchall()
    return render_template('configs/list.html', configs=configs)

@configs_bp.route('/add_config', methods=['GET', 'POST'])
def add_config():
    if request.method == 'POST':
        name = request.form['name']
        protocol = request.form['protocol']
        config_json = request.form['config_json']
        tags = request.form['tags']
        created_at = datetime.utcnow().isoformat()

        with sqlite3.connect(DB_PATH) as conn:
            conn.execute('''
                INSERT INTO configs (name, protocol, config_json, tags, created_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, protocol, config_json, tags, created_at))
        return redirect(url_for('configs.list_configs'))

    return render_template('configs/add.html')
