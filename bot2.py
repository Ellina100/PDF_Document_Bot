import telebot
import  random
bot = telebot.TeleBot("5638281823:AAHXL72Sq4vvVAFbozn3-uyx4aeUQrbVrwk")
class Player:
    def __init__(self,hp,dmg):
        self.hp = hp
        self.dmg = dmg
class Wisard(Player):
    def __init__(self,hp = 140,dmg = 60):
        super().__init__(hp,dmg)
        self.type = "Маг"
        self.health_item = "зелье"
wizard = Wisard()
class Elf(Player):
    def __init__(self,hp = 150,dmg = 55):
        super().__init__(hp,dmg)
        self.type = "Эльф"
        self.health_item = "Волшебная жидкость"
elf = Elf()
class Puple(Player):
    def __init__(self,hp = 200,dmg = 52):
        super().__init__(hp,dmg)
        self.type = "Человек"
        self.health_item = "Броня"
puple = Puple()
global monster_hp,monster_dmg,user_dmg,user_hp,health_item,level,exp,wearpon
wearpon = {"Легендарное":30,"Мифическое":15,"Обычное":5,}
wearpon_types = ["Легендарное","Мифическое","Обычное"]
wearpon_pictures = {"Легендарное":'https://i.pinimg.com/originals/ea/d1/70/ead170da8bb328c1d30dec387c324688.png',"Мифическое":'https://ae04.alicdn.com/kf/Ha575bf63856843828a7fde5ec54441beW/Genshin.jpg',"Обычное":'https://media.hitekno.com/thumbs/2021/01/01/57117-genshin-impact-debate-club/730x480-img-57117-genshin-impact-debate-club.jpg'}
boxes_items = ["Оружие","Пусто","Неудача"]
exp = 0
level = 1
@bot.message_handler(commands=["start"])
def start(message):
    bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Начать игру")
    btn2 = telebot.types.KeyboardButton("Правила игры")
    bot2.add(btn1,btn2)
    bot.send_message(message.chat.id,"Привет,готов сыграть?",reply_markup= bot2)
def buttons():
    bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("В путь")
    btn2 = telebot.types.KeyboardButton("Главное меню")
    bot2.add(btn1, btn2)
    return bot2

@bot.message_handler(content_types=["text"])
def answer(message):
    global monster_hp, monster_dmg, user_dmg, user_hp,health_item,level,exp
    if message.text == "Начать игру":
        bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = puple.type
        btn2 = wizard.type
        btn3 = elf.type
        bot2.add(btn1, btn2,btn3)
        bot.send_message(message.chat.id, "Выберите расу", reply_markup=bot2)
    if message.text == wizard.type:
        bot2 = buttons()
        bot.send_message(message.chat.id, f"Вы Маг,у вас здоровья {wizard.hp},у вас урон {wizard.dmg}",reply_markup=bot2)
        user_hp = wizard.hp
        user_dmg = wizard.dmg
        health_item = wizard.health_item
    if message.text == elf.type:
        bot2 = buttons()
        bot.send_message(message.chat.id, f"Вы Эльф,у вас здоровья {elf.hp},у вас урон {elf.dmg}", reply_markup=bot2)
        user_hp = elf.hp
        user_dmg = elf.dmg
        health_item = elf.health_item
    if message.text == puple.type:
        bot2 = buttons()
        bot.send_message(message.chat.id, f"Вы Человек,у вас здоровья {puple.hp},у вас урон {puple.dmg}", reply_markup=bot2)
        user_hp = puple.hp
        user_dmg = puple.dmg
        health_item = puple.health_item
    if message.text == "Правила игры":
        bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton("Начать игру")
        btn2 = telebot.types.KeyboardButton("Главное меню")
        bot2.add(btn1, btn2)
        bot.send_message(message.chat.id, "Привет путешественник,в этой игре тебе надо будет сражаться с монстрами,ну что приступим?<З?", reply_markup=bot2)

    if message.text == "Главное меню":
        bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton("Начать игру")
        btn2 = telebot.types.KeyboardButton("Правила игры")
        bot2.add(btn1, btn2)
        bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=bot2)
    if message.text == "В путь":
        ivent = random.randint(0,1)
        if not ivent:
            bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = telebot.types.KeyboardButton("В путь")
            btn2 = telebot.types.KeyboardButton("Главное меню")
            bot2.add(btn1, btn2)
            bot.send_message(message.chat.id, "Вам никто не встретился,продолжайте путешествие", reply_markup=bot2)
        else:
            bot.send_message(message.chat.id, "Вам встретился монстр")

            monster_hp = random.randint(70, 150) * level
            monster_dmg = random.randint(50,150) * level
            bot2=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = telebot.types.KeyboardButton("Атаковать")
            btn2 = telebot.types.KeyboardButton("Убежать")
            btn3 = telebot.types.KeyboardButton("Главное меню")
            bot2.add(btn1, btn2,btn3)
            bot.send_message(message.chat.id,f"Вам встретился монстр,у него очков здоровья:{monster_hp},у него урон:{monster_dmg}", reply_markup=bot2)
    if message.text == "Атаковать":
        bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton("Нанести удар")
        btn2 = telebot.types.KeyboardButton("Главное меню")
        bot2.add(btn1, btn2)
        bot.send_message(message.chat.id, "Вы атаковали", reply_markup=bot2)
    if message.text == "Нанести удар":
        bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        monster_hp -= user_dmg
        if monster_hp <= 0:
            btn1 = telebot.types.KeyboardButton("В путь")
            bot2.add(btn1)
            bot.send_message(message.chat.id,"Монстр повержен", reply_markup=bot2)
            user_hp += random.randint(50,200)
            bot.send_message(message.chat.id, f"Поздравляем это победа!Вот ваша награда:{health_item},ваше здоровье повысилось и составляяет:{user_hp}")
            exp += random.randint(50,250)
            if exp >= 500:
                level += 1
                user_dmg += random.randint(50, 90)
                bot.send_message(message.chat.id,f"У вас повысился уровень поздравляем!Теперь ваш уровень равен:{level},а еще у вас повысился урон:{user_dmg}")
                exp = 0
                bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = "бокс 1"
                btn2 = "бокс 2"
                btn3 = "бокс 3"
                bot2.add(btn1, btn2, btn3)
                print(bot2)
                bot.send_message(message.chat.id, "Вам выпала возможность повысить свой урон!!Выберите бокс ", reply_markup=bot2)
                print("Привет")
            else:
                bot.send_message(message.chat.id,f"У вас повысился опыт поздравляем!Теперь ваш опыт равен:{exp}")


        else:
            bot.send_message(message.chat.id,f"У монстра осталось {monster_hp},у вас осталось здоровья {user_hp},монстр на вас нападает")
            user_hp -= monster_dmg
            if user_hp <= 0:
                btn2 = telebot.types.KeyboardButton("Главное меню")
                bot2.add(btn2)
                bot.send_message(message.chat.id,"Персонаж погиб",reply_markup=bot2)
            else:
                btn1 = telebot.types.KeyboardButton("Атаковать")
                btn2 = telebot.types.KeyboardButton("Убежать")
                bot2.add(btn1,btn2)
                bot.send_message(message.chat.id, f"У вас осталось здоровья:{user_hp},что хотите сделать?", reply_markup=bot2)
    if message.text == "бокс 1" or message.text == "бокс 2" or message.text == "бокс 3":
        items = boxes_items[random.randint(0,2)]
        if items == boxes_items[0]:
            rarity = wearpon_types[random.randint(0, 2)]
            bot.send_message(message.chat.id,f"Поздравляем вам выпало оружие,редкость:{rarity}")
            bot.send_photo(message.chat.id,wearpon_pictures[rarity])
            user_dmg += wearpon[rarity]
            bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = telebot.types.KeyboardButton("В путь")
            btn2 = telebot.types.KeyboardButton("Главное меню")
            bot2.add(btn1, btn2)
            bot.send_message(message.chat.id,f"К урону добавилось:{wearpon[rarity]},теперь ваш урон составляет:{user_dmg}",reply_markup=bot2)
        elif items == boxes_items[1]:
            bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = telebot.types.KeyboardButton("В путь")
            btn2 = telebot.types.KeyboardButton("Главное меню")
            bot2.add(btn1, btn2)
            bot.send_message(message.chat.id,"Вам выпал пустой бокс :_(",reply_markup=bot2)
        else:
            user_dmg -= random.randint(10,50)
            bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = telebot.types.KeyboardButton("В путь")
            btn2 = telebot.types.KeyboardButton("Главное меню")
            bot2.add(btn1, btn2)
            bot.send_message(message.chat.id,f"О нееет!Это неудача! У вас понизился урон,теперь он составляет:{user_dmg}",reply_markup=bot2)

    if message.text == "Убежать":
        ran = random.randint(0,1)
        if ran:
            bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = telebot.types.KeyboardButton("В путь")
            bot2.add(btn1)
            bot.send_message(message.chat.id, "Вам удалось сбежать,поздравляем!", reply_markup=bot2)
        else:
            bot.send_message(message.chat.id,"Упс! Вам не удалось сбежать,на вас снова нападают.")
            user_hp -= monster_dmg
            bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            if user_hp <=0:
                btn2 = telebot.types.KeyboardButton("Главное меню")
                bot2.add(btn2)
                bot.send_message(message.chat.id, "Персонаж погиб", reply_markup=bot2)
            else:
                btn1 = telebot.types.KeyboardButton("Атаковать")
                btn2 = telebot.types.KeyboardButton("Убежать")
                bot2.add(btn1, btn2)
                bot.send_message(message.chat.id, f"У вас осталось здоровья:{user_hp},что хотите сделать?",reply_markup=bot2)

bot.polling(non_stop = True)