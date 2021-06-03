"""
	Created by Vici83 as a open source code idea
	A friends said that want to see how something like this works,
so I decided to try make it.
		
	It's just get some musics and creates a playlist, kinda simple.
"""
from os import getenv
API_TOKEN = getenv('token')

from typing import Union, List, Tuple
from logging import basicConfig, getLogger, INFO

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, CallbackQueryHandler, Filters

from language import BR, EN, AVALAIBLE_LEN

class ViciGroove:
	def __init__(self):
		self.updater = Updater(API_TOKEN)
		self.dispacher = self.updater.dispatcher
		self.bot = self.updater.bot

		self.createLogger()
		
		self.langs = [EN, BR]
		self.lang = EN
		self.__building__()
	
	def createLogger(self):
		basicConfig(
			format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=INFO
			)
		self.log = getLogger(__name__)
	
	def __building__(self):
		self.log.info("Starting me")
		self.dispacher.add_handler(CommandHandler('start', self.starting))
		self.dispacher.add_handler(CallbackQueryHandler(self.setLanguage))
		
		self.dispacher.add_handler(MessageHandler(
			Filters.regex('^({})$'.format('|'.join(self.__menuOptions__()))),
			self.responseMenu))
	
	def starting(self, update : Update, _ : CallbackContext):
		self.log.info('User {} started a conversetion with me'.format(update.message.from_user.name))
		
		buttons = [[InlineKeyboardButton(text=text, callback_data=text[:5])] for text in AVALAIBLE_LEN]
		update.message.reply_text(
			text='Choose a language:', 
			reply_markup=InlineKeyboardMarkup(buttons)
			)
				
	def setLanguage(self, update : Update, context : CallbackContext):
		query = update.callback_query
		query.answer()
		lan = query.data
		
		self.log.info('User {} set language to {}'.format(query.from_user.name, lan))
		if('pt-BR' in lan):
			self.lang = BR
		else: self.lang = EN
		
		query.edit_message_text(
			text=self.lang['greeting'])
		
		self.__initMenu__(enviar=context.bot.send_message, chat_id=update.effective_chat.id)
	
	def __initMenu__(self, enviar, chat_id=None):
		if(chat_id):
			enviar(
				chat_id=chat_id,
				text=self.lang['menu']['text'],
				reply_markup= self.createKeyboardMark(self.lang['menu']['options'])
			)

		else:
			enviar(
				text=self.lang['menu']['text'],
				reply_markup= self.createKeyboardMark(self.lang['menu']['options'])
			)
	
	def __menuOptions__(self):
		opt = []
		for lang in self.langs:
			for infos in lang['menu']['options']:
				for info in infos['text']: opt.append(info)
		return opt
		
	def responseMenu(self, update : Update, _ : CallbackContext):
		self.log.info('User {} choose the menu option: {}'.format(update.message.from_user.name, update.message.text))
		update.message.reply_text(
			text='Você entrou no menu: {}'.format(update.message.text), 
			reply_markup=ReplyKeyboardRemove()
		)
		
	def createKeyboardMark(self, infos: List[dict]):
		options = [info['text'] for info in infos]
		return ReplyKeyboardMarkup(keyboard=options, one_time_keyboard=True)
	
	def createButtons(self, infos: List[dict]):
		buttons = []
		for info in infos:
			buttons.append([InlineKeyboardButton(text=text, callback_data=callback) for text, callback in zip(info['text'], info['callback'])])
		
		return InlineKeyboardMarkup(buttons)

def Main():
	groove = ViciGroove()
	groove.updater.start_polling()

def teste():
	import testing
	testing.main(API_TOKEN)

#teste()
if( __name__ == '__main__'): Main()