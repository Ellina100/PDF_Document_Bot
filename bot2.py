import telebot
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
@bot.message_handler(commands=["start"])
def start(message):
    bot2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Начать игру")
    btn2 = telebot.types.KeyboardButton("Правила игры")
    bot2.add(btn1,btn2)
    bot.send_message(message.chat.id,"Привет,готов сыграть?",reply_markup= bot2)
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
        bot.send_message(message.chat.id, f"Вы Маг,у вас здоровья {wizard.hp},у вас урон {wizard.dmg}")
    if message.text == elf.type:
        bot.send_message(message.chat.id, f"Вы Эльф,у вас здоровья {elf.hp},у вас урон {elf.dmg}")
    if message.text == puple.type:
        bot.send_message(message.chat.id, f"Вы Человек,у вас здоровья {puple.hp},у вас урон {puple.dmg}")
bot.polling(non_stop = True)