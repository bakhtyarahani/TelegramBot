from hazm import *
normalizer = Normalizer()
tagger = POSTagger(model='resources/postagger.model')
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import telegram
from telegram import *
from telegram.__main__ import main as tmain
from telegram.ext import *
from telegram.error import *
import logging
import uuid

List=[]
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text="شما با وارد کردن یک جمله می توانید بخش گفتار آن، تعداد کلمات و تعداد جملات آن را بگیرید. این ربات برای زبان فارسی ساخته شده است.")
    bot.sendMessage(update.message.chat_id, text="لطفا یک متن وارد کنید")
def getCm(bot, update):
    List.append([update.message.chat_id,1])
    strnor1 = normalizer.normalize(update.message.text[3:])
    word=word_tokenize(strnor1)
    sentences = sent_tokenize(strnor1)
    tags1='◀️ تعداد کلمات : ' + str(len(word))+'\n'+'\n'
    tags1 =tags1+ '◀️ تعداد جمله : ' + str(len(sentences)) + '\n'+'\n'

    for i in range(len(sentences)):
        tags1 = tags1+'⏪ جمله ' + str(i+1) +' :'+ str(tagger.tag(word_tokenize(sentences[i])))+'\n'+'\n'
    bot.sendMessage(update.message.chat_id, text=str(tags1)+'\n'+'\n'+'💢نوشته شده توسط بختیار آهنی')
    bot.sendMessage(update.message.chat_id, text="اگر میخواهید دوباره استفاده کنید لطفا یک متن دیگر ارسال نمایید")


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token='token you')
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

cm_handler = MessageHandler([Filters.text], getCm)
dispatcher.add_handler(cm_handler)

updater.start_polling()
updater.idle()
updater.stop()