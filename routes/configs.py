from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

configs_bp = Blueprint('configs', __name__)
DB_PATH = 'db/gptpnl.db'

@configs_bp.route('/configs')
def list_configs():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        configs = conn.execute('SELECT * FROM configs').fetchall()
    return render_template('configs/list.html', configs=configs)

@configs_bp.route('/add_config', methods=['GET', 'POST'])
def add_config():
    if request.method == 'POST':
        name = request.form['name']
        protocol = request.form['protocol']
        config_json = request.form['config_json']
        tags = request.form.get('tags', '')
        created_at = datetime.utcnow().isoformat()

        with sqlite3.connect(DB_PATH) as conn:
            conn.execute('''
                INSERT INTO configs (name, protocol, config_json, tags, created_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, protocol, config_json, tags, created_at))
        return redirect(url_for('configs.list_configs'))

    return render_template('configs/add.html')

@configs_bp.route('/delete_config/<int:config_id>')
def delete_config(config_id):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('DELETE FROM configs WHERE id = ?', (config_id,))
    return redirect(url_for('configs.list_configs'))

@configs_bp.route('/edit_config/<int:config_id>', methods=['GET', 'POST'])
def edit_config(config_id):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        config = conn.execute('SELECT * FROM configs WHERE id = ?', (config_id,)).fetchone()

    if request.method == 'POST':
        name = request.form['name']
        protocol = request.form['protocol']
        config_json = request.form['config_json']
        tags = request.form.get('tags', '')

        with sqlite3.connect(DB_PATH) as conn:
            conn.execute('''
                UPDATE configs
                SET name = ?, protocol = ?, config_json = ?, tags = ?
                WHERE id = ?
            ''', (name, protocol, config_json, tags, config_id))
        return redirect(url_for('configs.list_configs'))

    return render_template('configs/edit.html', config=config)
