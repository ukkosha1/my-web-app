from flask import Flask, render_template, request
import os
from telegram import Bot

app = Flask(__name__)

# Telegram bot tokenini va TRC20 manzilini shu yerga qo‘ying
TELEGRAM_BOT_TOKEN = '7229132781:AAGyUp37qQgcaETbIfx098c_ZJ83TZFgrDs'
TRC20_ADDRESS = 'YOUR_TRC20_ADDRESS'

bot = Bot(token=TELEGRAM_BOT_TOKEN)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_address', methods=['POST'])
def send_address():
    user_id = request.form.get('user_id')
    if user_id:
        bot.send_message(chat_id=user_id, text=f"TRC20 Manzilingiz: {TRC20_ADDRESS}")
    return "Address sent!"

if __name__ == '__main__':
    app.run(debug=True)
