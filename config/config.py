import telebot


API_TOKEN = "" # Вставить токен бота между двойных кавычек. Подробнее: https://www.youtube.com/watch?v=fyISLEvzIec&ab_channel=Parsemachine
BOT = telebot.TeleBot(API_TOKEN, threaded=False, skip_pending=True) # Экземпляр бота.