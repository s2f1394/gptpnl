from flask import Blueprint, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # بارگذاری .env برای API Key

gpt_bp = Blueprint('gpt', __name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@gpt_bp.route('/gpt', methods=['GET', 'POST'])
def gpt_chat():
    response = ''
    if request.method == 'POST':
        prompt = request.form['prompt']
        try:
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            response = res['choices'][0]['message']['content']
        except Exception as e:
            response = f"❌ خطا: {str(e)}"
    return render_template('gpt.html', response=response)
