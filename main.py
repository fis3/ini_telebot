#!/usr/bin/env python
# -*-coding:utf-8 -*
import sys

try:
	import telebot
except:
	print ">> Debe instalar la libreria de telegram bot.\n>> CMD: pip install telebot"

TOKEN="" #Ponemos nuestro TOKEN generado con el @BotFather

def enviar_bot(cid, respuesta):
    bot.send_message(parse_mode='HTML', chat_id=cid, text=respuesta)
    
def main(messages):
	for menssage in messages:
		cid = menssage.chat.id
		chat = menssage.text
		enviar_bot(cid, "<code>{0}</code>".format(chat))

while True:
	try:
		bot = telebot.TeleBot(TOKEN)
		bot.set_update_listener(main)
		bot.polling(none_stop=True)
	except:
		print ">> ERROR - {0}\n>> Reiniciando el sistema.\n".format(sys.exc_info()[0])