from flask import Flask,render_template_string, request, jsonify, abort
from google import genai
from dotenv import load_dotenv
import os
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

load_dotenv()
app = Flask(__name__)
client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))
line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))

@app.route("/")
def index():
    html = '''
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <title>Gemini 小助手 Chatbot</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f5f5f5; }
            .container { max-width: 900px; margin: 40px auto; background: #fff; padding: 40px; border-radius: 10px; box-shadow: 0 2px 8px #ccc; }
            h1 { text-align: center; }
            #result { min-height: 120px; background: #f0f0f0; margin-top: 20px; padding: 18px; border-radius: 5px; }
            .btn { padding: 12px 28px; margin: 6px; border: none; border-radius: 5px; cursor: pointer; font-size: 18px; }
            .btn-start { background: #4CAF50; color: #fff; }
            .btn-clear { background: #f44336; color: #fff; }
            #question { width: 100%; padding: 12px; border-radius: 5px; border: 1px solid #ccc; font-size: 16px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Gemini 小助手 Chatbot</h1>
            <input type="text" id="question" placeholder="請輸入您的問題..." />
            <div>
                <button class="btn btn-start" onclick="startChat()">開始</button>
                <button class="btn btn-clear" onclick="clearAll()">清除</button>
            </div>
            <div id="result"></div>
        </div>
        <script>
            function startChat() {
                const q = document.getElementById('question').value.trim();
                if (!q) { alert('請輸入問題'); return; }
                document.getElementById('result').innerHTML = '請稍候...';
                fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ question: q })
                })
                .then(res => res.json())
                .then(data => {
                    document.getElementById('result').innerHTML = data.html || data.text || '無回應';
                })
                .catch(() => {
                    document.getElementById('result').innerHTML = '發生錯誤，請稍後再試';
                });
            }
            function clearAll() {
                document.getElementById('question').value = '';
                document.getElementById('result').innerHTML = '';
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get('question', '').strip()
    if not question:
        return jsonify({'error': '未輸入問題'}), 400
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=f"{question},回應請輸出成為html格式,請記得您的名字是`賽巴斯汀執事`"
        )
        html_format = response.text.replace("```html","").replace("```","")
        return jsonify({'html': html_format})
    except Exception as e:
        return jsonify({'error': str(e)}), 500