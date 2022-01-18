import botconfig 
import telebot
import perceptron_script
# from telebot import apihelper
# apihelper.proxy = {'https':'https://telegg.ru/SmetanaEchoBot'}

bot = telebot.TeleBot(botconfig.token)

@bot.message_handler(content_types=["text"])
def text_messages(message): # Название функции не играет никакой роли, в принципе
    # pred = perceptron_script.predforbot()
    bot.send_message(message.chat.id, "text")

@bot.message_handler(content_types=["photo"])
def photo_messages(message): # Название функции не играет никакой роли, в принципе
    # pred = perceptron_script.predforbot()
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    # photo = open(file_info.file_path, 'rb')
    # bot.send_photo(message.chat_id, photo)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    
    pred = perceptron_script.predforbot("image.jpg")
    bot.send_message(message.chat.id, pred)
    # photo = open(file_info.file_path, 'rb')
    # bot.send_photo(message[-1].chat_id, "image.jpg")
    # bot.send_message(message.chat.id, "это фото")

if __name__ == "__main__":
    bot.polling(none_stop=True)