import telebot
import sys
import os
import json
import urllib
import requests

reload(sys)
from telebot import types
#from telebot import *
sys.setdefaultencoding("utf-8")

TOKEN = '210858938:AAFwgaSWfrwQP7IfRm0zG1smc81RrgVg0Do'
bot = telebot.TeleBot(TOKEN)
#'237118620:AAG5rk4rn-vX6dgoFhs51VTjOlKgBAp6KVw'

@bot.message_handler(func=lambda message: True)
def m(m):
	if m.text == '/start' or m.text == '/help':  #  start processing when user types 'start' or 'help'
		markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
		
		key_a = types.KeyboardButton('Option A \xE2\x98\x95\xEF\xB8\x8F')  #  defining what is to be printed on keys
		key_b = types.KeyboardButton('Option B \xE2\x98\x95\xEF\xB8\x8F')
		key_c = types.KeyboardButton('Option C \xE2\x98\x95\xEF\xB8\x8F')
		key_d = types.KeyboardButton('Option D \xE2\x98\x95\xEF\xB8\x8F')
		key_e = types.KeyboardButton('Option E \xE2\x98\x95\xEF\xB8\x8F')

		#key_loc = types.Location(lat, long)
		
		markup.add(key_a, key_b, key_c, key_d, key_e)  #  designing keyboard(keys present on it)
		#markup.add(key_a, key_b, key_c, key_d, key_e, key_loc)
		
		bot.send_chat_action(m.chat.id, 'typing')
		bot.reply_to(m, "Hi {}".format(m.from_user.first_name))
		bot.send_message(m.chat.id, 'This is a Gate_Cse bot', reply_markup=markup)
		
		print 'command help'
		print '{}'.format(m.from_user.first_name)
		print '{}'.format(m.from_user.username)
		return
	print "Samaksh"

	if m.text == 'Option A \xE2\x98\x95\xEF\xB8\x8F':
		bot.send_message(m.chat.id, 'You selected Option A')
		print 'command A'
		print '{}'.format(m.from_user.first_name)
		print '{}'.format(m.from_user.username)

	if m.text == 'Option B \xE2\x98\x95\xEF\xB8\x8F':
		bot.send_message(m.chat.id, 'You selected Option B')
		print 'command B'
		print '{}'.format(m.from_user.first_name)
		print '{}'.format(m.from_user.username)

	if m.text == 'Option C \xE2\x98\x95\xEF\xB8\x8F':
		bot.send_message(m.chat.id, 'You selected Option C')
		print 'command C'
		print '{}'.format(m.from_user.first_name)
		print '{}'.format(m.from_user.username)

	if m.text == 'Option D \xE2\x98\x95\xEF\xB8\x8F':
		bot.send_message(m.chat.id, 'You selected Option D')
		print 'command D'
		print '{}'.format(m.from_user.first_name)
		print '{}'.format(m.from_user.username)

	if m.text == 'Option E \xE2\x98\x95\xEF\xB8\x8F':
		bot.send_message(m.chat.id, 'You selected Option E')
		print 'command E'
		print '{}'.format(m.from_user.first_name)
		print '{}'.format(m.from_user.username)
	
	if m.text == '/leave':
		bot.leave_chat(m.chat.id)
		print 'command leave'
		print '{}'.format(m.from_user.first_name)
		print '{}'.format(m.from_user.username)


#bot.polling(none_stop=True, timeout=30)