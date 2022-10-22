from typing import List
from language import *
    
def createKeyboardMark(infos: List[dict]):
    from telegram import ReplyKeyboardMarkup
    
    options = [info['text'] for info in infos]
    return ReplyKeyboardMarkup(keyboard=options, one_time_keyboard=True)


def createButtons(infos: List[dict]):
    from telegram import  InlineKeyboardMarkup, InlineKeyboardButton
    
    buttons = []
    for info in infos:
        buttons.append([InlineKeyboardButton(text=text, callback_data=callback) for text, callback in zip(info['text'], info['callback'])])
    
    return InlineKeyboardMarkup(buttons)


def createLogger():
    from logging import basicConfig, getLogger, INFO
    
    basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=INFO
        )
    return getLogger(__name__)


def __initLang__(enviar, lang=EN, chat_id=None):
    from telegram import InlineKeyboardMarkup, InlineKeyboardButton
    
    #This "AVALAIBLE_LEN" are all the languages already supported from te bot
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


def __initMenu__(enviar, lang=EN, chat_id=None):
    if(chat_id):
        enviar(
            chat_id=chat_id,
            text=lang['menu']['text'],
            reply_markup= createButtons(lang['menu']['options'])
        )

    else:
        enviar(
            text=lang['menu']['text'],
            reply_markup= createButtons(lang['menu']['options'])
        )
        