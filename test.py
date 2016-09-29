import telebot

bot = telebot.TeleBot('261118195:AAGhnJKmOzum6wJRX2Zo3Hx8pxdMgdzMvrg')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "kya kar sakta hu aapke liye?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "Samajh mai nai aaya")

@bot.message_handler(commands=['me'])
def mem(m):
	text=bot.get_chat_member(m.chat.id,m.from_user.id)
	bot.send_message(m.from_user.id,me.user.id)