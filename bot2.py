import telebot
import  random
bot = telebot.TeleBot("5638281823:AAHXL72Sq4vvVAFbozn3-uyx4aeUQrbVrwk")
class Player:
    def __init__(self,hp,dmg):
        self.hp = hp
        self.dmg = dmg
class Wisard(Player):
    def __init__(self,hp = 100,dmg = 50):
        super().__init__(hp,dmg)
        self.type = "Маг"
wizard = Wisard()
class Elf(Player):
    def __init__(self,hp = 90,dmg = 55):
        super().__init__(hp,dmg)
        self.type = "Эльф"
elf = Elf()
class Puple(Player):
    def __init__(self,hp = 110,dmg = 52):
        super().__init__(hp,dmg)
        self.type = "Человек"
puple = Puple()
global exp,level
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
global monster_hp,monster_dmg,user_dmg,user_hp
@bot.message_handler(content_types=["text"])
def answer(message):
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
    if message.text == elf.type:
        bot2 = buttons()
        bot.send_message(message.chat.id, f"Вы Эльф,у вас здоровья {elf.hp},у вас урон {elf.dmg}", reply_markup=bot2)
        user_hp = elf.hp
        user_dmg = elf.dmg
    if message.text == puple.type:
        bot2 = buttons()
        bot.send_message(message.chat.id, f"Вы Человек,у вас здоровья {puple.hp},у вас урон {puple.dmg}", reply_markup=bot2)
        user_hp = puple.hp
        user_dmg = puple.dmg
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

            monster_hp = random.randint(70, 140)
            monster_dmg = random.randint(50, 120)
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
        else:
            '''btn1 = telebot.types.KeyboardButton("Нанести удар")
            btn2 = telebot.types.KeyboardButton("Бежать")'''
            bot.send_message(message.chat.id,f"У монстра осталось {monster_hp},у вас осталось здоровья {user_hp},монстр на вас нападает,что будете делать?")
            user_hp -= monster_dmg
            if user_hp <= 0:
                btn2 = telebot.types.KeyboardButton("Главное меню")
                bot2.add(btn2)
                bot.send_message(message.chat.id,"Персонаж погиб",reply_markup=bot2)
            else:
                btn1 = telebot.types.KeyboardButton("Атаковать")
                btn2 = telebot.types.KeyboardButton("Убежать")
                bot2.add(btn1,btn2)
                bot.send_message(message.chat.id, f"У вас осталось здоровья:{user_hp},что хотите сделать?",reply_markup=bot2)
bot.polling(non_stop = True)