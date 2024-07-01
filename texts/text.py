class Text:
    def start_text(self, message) -> str:
        return f"👋 Привет, {message.from_user.first_name}. Это Echo Bot!\n\n🧡 Отправь мне любой другой текст и я повторю его!"

    def echo_text(self, message) -> str:
        return message.text # Возвращает текст который набрал пользователь.
    
    def bot_is_working(self) -> str:
        return "---Регистрация хендлеров закончена, бот запущен.---"
    
message = Text() # Экземпляр класса, используется для получения текста.
