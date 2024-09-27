from telethon import TelegramClient

# إدخال المعلومات الخاصة بحسابك
api_id = '25253974'        # استبدل بـ API ID الخاص بحسابك
api_hash = '327b7ffeacb2458578d9dc1a45098cea'    # استبدل بـ API Hash الخاص بحسابك
bot_username = '@NactiviBot'  # اسم المستخدم للبوت الذي تريد إرسال الرسائل له
message_text = 'هذه رسالة من حسابي الشخصي إلى البوت.'

# إنشاء جلسة عميل
client = TelegramClient('session_name', api_id, api_hash)

async def send_message():
    # تسجيل الدخول
    await client.start()

    # إرسال الرسالة إلى البوت
    await client.send_message(bot_username, message_text)

    print("تم إرسال الرسالة!")

# تشغيل السكربت
with client:
    client.loop.run_until_complete(send_message())
# الخادم
from flask import Flask, request, jsonify
from telethon import TelegramClient

app = Flask(__name__)

api_id = '25253974'
api_hash = '327b7ffeacb2458578d9dc1a45098cea'
bot_username = '@NactiviBot'

client = TelegramClient('session_name', api_id, api_hash)

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message', 'رسالة افتراضية')

    async def send_telegram_message():
        await client.start()
        await client.send_message(bot_username, message)
    
    with client:
        client.loop.run_until_complete(send_telegram_message())

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)