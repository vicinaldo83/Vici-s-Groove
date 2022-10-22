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
#?==================================================================|  Building |===================================================================
    
    def __init__(self):
        self.updater = Updater(API_TOKEN)
        self.dispacher = self.updater.dispatcher
        self.bot = self.updater.bot

        self.createLogger()

        self.user = {}
        self.__building__()
        

    def __building__(self):
        self.log.info("Starting me")
        self.dispacher.add_handler(CommandHandler('start', self.starting))
        
        self.dispacher.add_handler(
            CallbackQueryHandler(
                self.setLanguage,
                pattern=f"^({'|'.join([x[:5] for x in AVALAIBLE_LEN])})$"
            ))

        self.dispacher.add_handler(
            CallbackQueryHandler(
                self.responseMenu,
                pattern=f"^({'|'.join(['goMusics', 'goSoundtrack', 'goPlaylist'])})$"
            ))
        
        self.dispacher.add_handler(
            CallbackQueryHandler(
                self.returnLeng,
                pattern=f"^(changeLan)$"
            ))

        self.dispacher.add_handler(
            CallbackQueryHandler(
                self.returnMenu,
                pattern=f"^({EN['final'][0]['callback'][0]})$"
            ))


    def starting(self, update : Update, context : CallbackContext):
        self.log.info('User {} started a conversetion with me'.format(update.message.from_user.name))
        self.user.update({
            update.message.from_user.name: {
                'start' : True
            }
        })

        self.__initLang__(update.message.reply_text, )

#?=================================================================|  Utilitários |=================================================================
    
    def createKeyboardMark(self, infos: List[dict]):
        options = [info['text'] for info in infos]
        return ReplyKeyboardMarkup(keyboard=options, one_time_keyboard=True)
    
    
    def createButtons(self, infos: List[dict]):
        buttons = []
        for info in infos:
            buttons.append([InlineKeyboardButton(text=text, callback_data=callback) for text, callback in zip(info['text'], info['callback'])])
        
        return InlineKeyboardMarkup(buttons)
    
    
    def createLogger(self):
        basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=INFO
            )
        self.log = getLogger(__name__)


    def __initLang__(self, enviar, lang=EN, chat_id=None):
        buttons = [[InlineKeyboardButton(text=text, callback_data=text[:5])] for text in AVALAIBLE_LEN]
        if(chat_id):
            enviar(
                text='Choose a language:', 
                reply_markup=InlineKeyboardMarkup(buttons)
            )

        else:
            enviar(
                text='Choose a language:', 
                reply_markup=InlineKeyboardMarkup(buttons)
            )


    def __initMenu__(self, enviar, lang=EN, chat_id=None):
        if(chat_id):
            enviar(
                chat_id=chat_id,
                text=lang['menu']['text'],
                reply_markup= self.createButtons(lang['menu']['options'])
            )

        else:
            enviar(
                text=lang['menu']['text'],
                reply_markup= self.createButtons(lang['menu']['options'])
            )
        
#?====================================================================|  Return |===================================================================
    
    def returnLeng(self, update : Update, _ : CallbackContext):
        query = update.callback_query
        query.answer()
        user = query.from_user.name
        
        self.__initLang__(query.edit_message_text, lang=self.user[user]['lang'])
        
    
    def returnMenu(self, update : Update, _ : CallbackContext):
        query = update.callback_query
        query.answer()
        user = query.from_user.name
        
        self.__initMenu__(query.edit_message_text, lang=self.user[user]['lang'])
    
        
    def changeLanguage(self, update : Update, context : CallbackContext):
        query = update.callback_query
        query.answer()
        
        self.__initLang__(update.message.reply_text)
        
#?===================================================================|  Response |==================================================================

    def setLanguage(self, update : Update, context : CallbackContext):
        query = update.callback_query
        query.answer()
        user = query.from_user.name
        
        lan = query.data
        
        self.log.info('User {} set language to {}'.format(user, lan))
        if('pt-BR' in lan):
            self.user[user].update({'lang' : BR})
        else: self.user[user].update({'lang' : EN})
        
        if(self.user[user]['start']):
            self.user[user]['start'] = False
            query.edit_message_text(
                text=self.user[user]['lang']['greeting'])
            enviar = context.bot.send_message
            chat_id = update.effective_chat.id
        else: enviar, chat_id = (query.edit_message_text, None)
        
        self.__initMenu__(enviar=enviar, lang=self.user[user]['lang'], chat_id=chat_id)
    

    def responseMenu(self, update : Update, _ : CallbackContext):
        query = update.callback_query
        query.answer()
        user = query.from_user.name

        
        options = ['changeLan', 'goMusics', 'goSoundtrack', 'goPlaylist']

        self.log.info('User {} choose the menu option: {}'.format(query.from_user.name, query.data))
        query.edit_message_text(
            text='Você entrou no menu: {}'.format(query.data), 
            reply_markup=self.createButtons(self.user[user]['lang']['final'])
        )


def Main():
    groove = ViciGroove()
    groove.updater.start_polling()

def teste():
    import testing
    testing.main(API_TOKEN)

#teste()
if( __name__ == '__main__'): Main()