from config import config
from texts import text


class EchoHandler:
    def echo(self, message) -> None: # Echo Handler, метод отправляет пользователю его текст. Исключение: /start
        config.BOT.send_message(chat_id=message.chat.id, text=text.message.echo_text(message=message))
        return
    
handler = EchoHandler() # Экземпляр класса, используется для передачи метода класса echo в main.py.