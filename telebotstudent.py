import telebot as tp
import configparser as cp

bot = tp.TeleBot('1860813832:AAFCgtuaMuiMeaN2bezNh0Jfb4B_wbZG6Y0')

@bot.message_handler(commands=['start'])
def menu(message):
    start_menu = tp.types.ReplyKeyboardMarkup(True, True)
    start_menu.row('Day of week')
    send = bot.send_message(message.chat.id, 'Hello sun ^_^ click a button to continue.', reply_markup=start_menu)



@bot.message_handler(content_types=['text'])
def week(message):
    if message.text == 'Day of week':
        keyboard = tp.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('Monday', 'Tuesday')
        keyboard.row('Wednesday', 'Thursday')
        keyboard.row('Friday', 'Saturday','Sunday')
        keyboard.row('Cancel')
        send = bot.send_message(message.chat.id, 'Choose some day pls', reply_markup=keyboard)
        bot.register_next_step_handler(send, subject)

    elif message.text == 'Cancel':
        menu(message)

def subject(message):

    if message.text == 'Monday':
        keyboard = tp.types.ReplyKeyboardMarkup(True, False)
        keyboard.row('English', 'Russian')
        keyboard.row('Math', 'Physics')
        keyboard.row('Cancel')
        send = bot.send_message(message.chat.id, 'Choose some subject pls', reply_markup=keyboard)
        bot.register_next_step_handler(send, type)
    elif message.text =='Cancel':
        menu(message)

def type(message):
    if message.text == 'English':
        keyboard = tp.types.ReplyKeyboardMarkup(True,True)
        keyboard.row('homework','classwork')
        send = bot.send_message(message.chat.id,'Choose type', reply_markup=keyboard)
        bot.register_next_step_handler(send, exercise)

def exercise(message):
    if message.text == 'homework':
        parser = cp.ConfigParser()
        parser.read('example.ini')
        msg = parser.get('Wednesday', 'homework')
        home = 'Your homework↓'
        keyboard = tp.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('Replay')
        send = bot.send_message(message.chat.id, home , reply_markup=keyboard)
        bot.send_message(message.from_user.id, text = msg)
        bot.register_next_step_handler(send, menu)


bot.polling(none_stop=True, interval=0)
