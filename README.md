# Бот для группы Telegram

### Предварительные требования

- Python (рекомендуется последняя версия)
- Токен Telegram Bot
- токен API от WeatherAPI 

### Шаги для установки

1. **Скачайте и установите Python** с официального сайта, если он еще не установлен:
   - [Скачать Python](https://www.python.org/downloads/)

2. **Клонируйте репозиторий:**<br>
   ```bash<br>
   git clone https://github.com/dgs333/Tgbot<br>
   cd Tgbot<br>
3. **Установите зависимости:**<br>
   ```bash<br>
   pip install -r requirements.txt<br>
4. **Измените значения переменных на свои токены в файле config.py:**<br>
   ```bash<br>
   TOKENTG = "токен Telegram Bot"<br>
   WETHERAPI = "токен WeatherAPI"<br>
5. **Запуск файла main.py:**<br>
   ```bash<br>
   python main.py<br>
