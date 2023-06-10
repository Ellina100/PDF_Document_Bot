import telebot
bot = telebot.TeleBot("6155555985:AAH85PszoN2763YrbI2u1u1uhppMjhvYD4Q")
wearpon_pictures = [
     ['https://ibb.co/tzd7cPq',"007",2100],
     ['https://ibb.co/1MzSYmf',"013",2600],
     ['https://ibb.co/Pzvm6vp',"001",3500],
]

jacket_pictures = [
    ['https://ibb.co/rZHZ5jR',"005",5800],
    ['https://ibb.co/MhK85Qb',"006",6000],
    ['https://ibb.co/S5WCTQH',"008",4900],
    ['https://ibb.co/mTC6v4H',"009",6300],
]

skirts_pictures = [
    ['https://ibb.co/jV2sLnF',"015",1800],
    ['https://ibb.co/QDQmtvZ',"010",1900],
]

shirts_pictures = [
    ['https://ibb.co/ZJh7v1V',"011",1500],
    ['https://ibb.co/Pc63ndS',"012",2400],
    ['https://ibb.co/x3T42zK',"004",2300],
    ['https://ibb.co/F51RKfj',"003",1800],
]

trousers_pictures = [
    ['https://ibb.co/Q7WM1hv',"002",2400],
    ['https://ibb.co/3rzZykZ',"014",1600],
]

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"Этот бот поможет вам выбрать нужную вещь среди всего ассортимента бренда YoungTEA")
    bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Обувь")
    btn2 = telebot.types.KeyboardButton("Юбки/Платья")
    btn3 = telebot.types.KeyboardButton("Рубашки/Свитера")
    btn4 = telebot.types.KeyboardButton("Брюки")
    btn5 = telebot.types.KeyboardButton("Пиджаки")
    bot2.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, "Выбери категорию", reply_markup=bot2)


@bot.message_handler(commands=["info"])
def info(message):
    bot.send_message(message.chat.id, """Бренд YoungTEA основан в 2017 году в городе
                                      Санкт-Петербург.Наша миссия — показать, что
                                       гардероб молодежи может состоять не только из худи
                                        и кроссовок.Все модели бренда передают эстетику
                                         тихого осеннего вечера с чашкой чая и книгой в руках.""")

@bot.message_handler(content_types=["text"])
def answer(message):
    if message.text == "Обувь":
        for x in range(len(wearpon_pictures)):
            bot.send_photo(message.chat.id,wearpon_pictures[x][0])
            bot.send_message(message.chat.id, f"Артикул:{wearpon_pictures[x][1]}")
            bot.send_message(message.chat.id, f"Цена:{wearpon_pictures[x][2]}")

    elif message.text == "Юбки/Платья":
        for x in range(len(skirts_pictures)):
            bot.send_photo(message.chat.id,skirts_pictures[x][0])
            bot.send_message(message.chat.id,f"Артикул:{skirts_pictures[x][1]}")
            bot.send_message(message.chat.id,f"Цена:{skirts_pictures[x][2]}")

    elif message.text == "Рубашки/Свитера":
        for x in range(len(shirts_pictures)):
            bot.send_photo(message.chat.id,shirts_pictures[x][0])
            bot.send_message(message.chat.id, f"Артикул:{shirts_pictures[x][1]}")
            bot.send_message(message.chat.id, f"Цена:{shirts_pictures[x][2]}")

    elif message.text == "Пиджаки":
         for x in range(len(jacket_pictures)):
             bot.send_photo(message.chat.id, jacket_pictures[x][0])
             bot.send_message(message.chat.id, f"Артикул:{jacket_pictures[x][1]}")
             bot.send_message(message.chat.id, f"Цена:{jacket_pictures[x][2]}")

    elif message.text == "Брюки":
        for x in range(len(trousers_pictures)):
            bot.send_photo(message.chat.id, trousers_pictures[x][0])
            bot.send_message(message.chat.id, f"Артикул:{trousers_pictures[x][1]}")
            bot.send_message(message.chat.id, f"Цена:{trousers_pictures[x][2]}")





bot.polling(non_stop = True)