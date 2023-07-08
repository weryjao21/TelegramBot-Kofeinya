import telebot
# https://t.me/Probnik11111bot
bot = telebot.TeleBot("6081314090:AAG2J9m3vYIVR1ax8voGKNSWq2YOyMtlEV0", parse_mode=None)
money_bank=[100]

@bot.message_handler(content_types=["text"])
def send_welcome(message):
    money = message.text
    if money == '1':
        if (money_bank[0]>0)
            money_bank[0] = money_bank[0]-1
            print("Осталось денег: " + str(money_bank[0]))
            bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}, заберите Ваш чай")
        else:
            bot.send_message(message.chat.id, "Нету денег!!!")
    elif money == '2':
        if (money_bank[0] > 0)
            money_bank[0] = money_bank[0] - 2
            print("Осталось денег: " + str(money_bank[0]))
            bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}, заберите Ваш Американо")
        else:
            bot.send_message(message.chat.id, "Нету денег!!!")
    elif money == '3':
        if (money_bank[0] > 0)
            money_bank[0] = money_bank[0] - 3
            print("Осталось денег: " + str(money_bank[0]))
            bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}, заберите Ваш Латте")
        else:
            bot.send_message(message.chat.id, "Нету денег!!!")
    else:
        print("Осталось денег: " + str(money_bank[0]))
        bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}, Вы ввели ерунду")

bot.infinity_polling()



