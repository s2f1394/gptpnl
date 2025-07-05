# app.py
from flask import Flask
from routes.users import users_bp
from routes.configs import configs_bp
from routes.gpt import gpt_bp
from routes.settings import settings_bp
import os
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی از .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "defaultsecretkey")

# ثبت بلوپرینت‌ها (ماژول‌ها)
app.register_blueprint(users_bp)
app.register_blueprint(configs_bp)
app.register_blueprint(gpt_bp)
app.register_blueprint(settings_bp)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 8080)), debug=True)
