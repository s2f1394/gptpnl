from flask import Blueprint, render_template, request
import openai
import os

gpt_bp = Blueprint('gpt', __name__)

openai.api_key = os.getenv("GPT_API_KEY")

@gpt_bp.route('/gpt', methods=['GET', 'POST'])
def chat_with_gpt():
    response = ""
    if request.method == 'POST':
        prompt = request.form['prompt']
        try:
            result = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150
            )
            response = result['choices'][0]['message']['content']
        except Exception as e:
            response = f"خطا: {e}"
    return render_template('gpt.html', response=response)
