from telebot import *
Token='8412955907:AAHrjt-NBgvNxqBHqR6FeJ89wa9_X1NGG7s'
bot=TeleBot(Token)

@bot.message_handler(commands=['star'])
def show__message(message):
    bot.reply_to(message,'welcome to the my bots')

bot.polling()