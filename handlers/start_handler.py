from config import config
from texts import text


class StartHandler:
    def start(self, message) -> None: # Start Handler, метод отправляет пользователю приветственный текст.
        config.BOT.send_message(chat_id=message.chat.id, text=text.message.start_text(message=message))
        return

handler = StartHandler() # Экземпляр класса, используется для передачи метода класса start в main.py.