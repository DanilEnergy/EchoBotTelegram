from config import config
from texts import text
from handlers import echo_handler, start_handler


class Main:
    def __init__(self) -> None:
        config.BOT.register_message_handler(start_handler.handler.start, commands=["start"]) # Регистрация Start Handler.
        config.BOT.register_message_handler(echo_handler.handler.echo) # Регистрация Echo Handler.
        print(text.message.bot_is_working())
        config.BOT.infinity_polling() # Запуск полинга.

if __name__ == "__main__": # Точка входа.
    Main()