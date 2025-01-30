import telebot
from func import *
from config import TOKENTG
from wb import main_parse

bot = telebot.TeleBot(TOKENTG)


@bot.message_handler(commands=['help'], func=lambda message: message.chat.type in ['group', 'supergroup'])
def help(message):
    txt = """
/dog - случайное фото собаки
/fox - случайное фото лисы
/duck - случайное фото утки
/curs количество bun - курс белорусского рубля
/weather город - погода
/gpt content -  чат гпт
/gpt_img content - генератор картинок

"""
#wb - плюсы/минусы товара на WB по артикулу
    bot.send_message(message.chat.id, txt)



#? рандом дог, фокс, дак
@bot.message_handler(commands=['dog'], func=lambda message: message.chat.type in ['group', 'supergroup'])
def dog(message):
    bot.send_photo(message.chat.id, random_dog())
@bot.message_handler(commands=['fox'], func=lambda message: message.chat.type in ['group', 'supergroup'])
def fox(message):
    bot.send_photo(message.chat.id, random_fox())
@bot.message_handler(commands=['duck'], func=lambda message: message.chat.type in ['group', 'supergroup'])
def duck(message):
    bot.send_photo(message.chat.id, random_duck())



@bot.message_handler(commands=['curs'], func=lambda message: message.chat.type in ['group', 'supergroup'])
def curs(message):
    args = message.text.split()[1:]

    if len(args)!= 1:
        bot.send_message(message.chat.id, "Использование: /curs количество bun")
        return
    
    try:
        grivn, usd, euro, zlotix, uen, uani, rub, kzt = cours() 
        count = float(args[0])

        txt = f"""
        {count} bun в
--------------------------------------------
{count / grivn:.2f} гривен,
{count / usd:.2f} долларов США,
{count / euro:.2f} евро,
{count / zlotix:.2f} злотых,
{count / uen:.2f} йен,
{count / uani:.2f} юаней,
{count / rub:.2f} рублей,
{count / kzt:.2f} тенге.
Национальный банк Республики Беларусь
        """
        bot.send_message(message.chat.id, txt)

    except ValueError:
       bot.reply_to(message, "Пожалуйста, введите данные\n(Использование: /curs количество bun")    

@bot.message_handler(commands=['weather'], func=lambda message: message.chat.type in ['group', 'supergroup'])
def weather(message):
    #print(message)
    args = message.text.split()[1:]
    #print(f"args - {args}")

    if len(args)!= 1:
        bot.send_message(message.chat.id, "Использование: /wether город")
        return
    city = args[0]
    txt = g_weather(city)
    #print(txt)

    bot.send_message(message.chat.id, txt)


@bot.message_handler(commands=['gpt'], func=lambda message: message.chat.type in ['group', 'supergroup'])
def gpt(message):
    args = ' '.join(message.text.split()[1:])
    print(args)
    if len(args) == 0:
        bot.send_message(message.chat.id, "Использование: /gpt content")
        return

    wait_message = bot.send_message(message.chat.id, "Подождите, пока ChatGPT завершит обработку информации. Это может занять некоторое время в зависимости от сложности запроса и объема данных. После завершения вы получите ответ.\nСпасибо за ваше терпение!")
    txt = GPTFree(args)
    if txt == "Привет! Как я могу помочь тебе сегодня? Если у тебя есть вопросы или нужна информация, просто дай знать!":
        bot.send_message(message.chat.id, "Проблема с запросом. Пожалуйста, попробуйте позже.")
    else:
        bot.send_message(message.chat.id, txt)
    bot.delete_message(message.chat.id, wait_message.message_id)


@bot.message_handler(commands=['gpt_img'], func=lambda message: message.chat.type in ['group', 'supergroup'])
def gpt_img(message):
    args = ' '.join(message.text.split()[1:])
    if len(args) == 0:
        bot.send_message(message.chat.id, "Использование: /gpt_img content")
        return
    img_url = GPTFree_img(args)

    bot.send_photo(message.chat.id, img_url)
    

@bot.message_handler(commands=['tg_spam'], func=lambda message: message.chat.type in ['group', 'supergroup'])
def tg_spam(message):
    args = ''.join(message.text.split()[1:])
    print(args)
    if len(args) == 0:
        bot.send_message(message.chat.id, "Использование: /tg_spam +number")
        return
    try:
        ans = telegram_spam(int(args))
        if ans == "None":
            bot.send_message(message.chat.id, "ERROR(наверное не правильный номер телефона)")
            bot.send_message(message.chat.id, "Использование: /tg_spam +1234567890")
        else:
            bot.send_message(message.chat.id, f"Спам был успешно отправлен на номер {args}.")
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите данные\n(Использование: /tg_spam +1234567890")


@bot.message_handler(commands=['wb'], func=lambda message: message.chat.type in ['group', 'supergroup'])
def wb(message):
    args = ''.join(message.text.split()[1:])
    if len(args) == 0:
        bot.send_message(message.chat.id, "Использование: /wb артикул")
        return
    try:
        ans = main_parse(args)
        if ans == "None":
            bot.send_message(message.chat.id, "ОШИБКА!\nВозможно товар не найден")
        else:
            bot.send_message(message.chat.id, f"{ans}")
    except Exception as e:
        bot.send_message(message.chat.id, f"ОШИБКА!")
        #print(e)

print("Бот запущен, нажмите Ctrl+C для остановки")
bot.polling(none_stop=True)