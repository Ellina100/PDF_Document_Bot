import telebot
bot = telebot.TeleBot("5638281823:AAHXL72Sq4vvVAFbozn3-uyx4aeUQrbVrwk")
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"Привет")
@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id, "Напишите любое слово и бот повторит за вами")
@bot.message_handler(content_types=["text"])
def repeat(message):
    bot.send_message(message.chat.id,message.text)
@bot.message_handler(content_types=["photo"])
def photoes(message):
    file_id=message.photo[-1].file_id
    print(file_id)
    file_info = bot.get_file(file_id)
    print(file_info)
    file_download = bot.download_file(file_info.file_path)
    with open("image","wb") as new_file:
        new_file.write(file_download)
    photo = open("image","rb")    
    bot.send_photo(message.chat.id,photo)
    photo.close()
   # remove("image")
bot.polling(non_stop = True)
