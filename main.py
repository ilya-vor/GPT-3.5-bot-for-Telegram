from openai import OpenAI
from telegram import Update
from telegram.ext import Application, Updater, CommandHandler, MessageHandler, filters, ContextTypes
import os
import logging

os.environ["OPENAI_API_KEY"] = '' #Insert the OpenAI API key, you can get it on the official website :https://platform.openai.com/api-keys"
client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY")) 
TOKEN = '' #Insert the TOKEN of your telegram bot
bot = Application.builder().token(TOKEN).build()
messages = {}
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.message.from_user.first_name
    user_id = update.message.from_user.id
    await update.message.reply_text(f"Привет {username}! Этот бот предназначен для \
генерирования ответов с помощью использования ChatGPT. Просто отправь \
мне текст и я отправлю его в GPT. Самое главное - бесплатно и без рекламы! :) \
(для создания нового чата наберите команду /start).")
    messages[user_id] = [{"role": "system", "content" : "You're a useful assistant."}]
    
    
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    timestamp = update.message.date
    readable_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Получено сообщение в {readable_time}")
    try:
        user_id = update.message.from_user.id
        username = update.message.from_user.first_name
        message = update.message.text
        try:
            response = generate_response(message,messages[user_id])
        except:
            messages[user_id] = [{"role": "system", "content" : "You're a useful assistant."}]
            response = generate_response(message,messages[user_id])
        await update.message.reply_text(response)
        print(f"Отпрален ответ в {readable_time}")
        savelogs(readable_time,username,message,timestamp,response)
    except Exception as e:
        print(f"Произошла ошибка {str(e)}")
        await update.message.reply_text(f"Произошла ошибка: {str(e)[0:100]}")

def generate_response(message,messages):
    content = message
    messages.append({"role": "user", "content": content})
    
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    chat_response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": chat_response})
    return chat_response

def savelogs(readable_time,username,message,timestamp,response):
    string = f"{readable_time}\n{username}: {message}\nGPT: {response}\n"
    with open(f"{username} history.txt", "a") as file:
        for i in string:
            try:
                file.write(i)
            except:
                file.write("")
        
start_handler = CommandHandler('start', start)
text_message_handler = MessageHandler(filters.TEXT, text_handler)

bot.add_handler(start_handler)
bot.add_handler(text_message_handler)

bot.run_polling(allowed_updates=Update.ALL_TYPES)
