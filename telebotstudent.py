import telebot as tb
import configparser as cp

bot = tb.TeleBot('YOUR_TOKEN')


@bot.message_handler(commands=['start'])
def menu(message):
    start_menu = tb.types.ReplyKeyboardMarkup(True, True)
    start_menu.row('Months')
    bot.send_message(message.chat.id, 'Hello sun ^_^ click a button to continue.', reply_markup=start_menu)


@bot.message_handler(func=lambda message: True)
def months(message):

    if message.text == 'Months':
        keyboard = tb.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('September', 'October', 'November')
        keyboard.row('December', 'Journey', 'February')
        keyboard.row('March', 'April', 'May')
        keyboard.row('Cancel')
        send = bot.send_message(message.chat.id, 'Choose', reply_markup=keyboard)
        bot.register_next_step_handler(send, days)
    elif message.text == 'Cancel':
        menu(message)

def days(message):

        if message.text == 'September':
            keyboard = tb.types.ReplyKeyboardMarkup(True, True)
            keyboard.row('1', '2', '3', '4', '5')
            keyboard.row('6', '7', '8', '9', '10')
            keyboard.row('11', '12', '13', '14', '16')
            keyboard.row('17', '18', '19', '20', '21')
            keyboard.row('22', '23', '24', '25', '26')
            keyboard.row('27', '28', '29', '30')
            keyboard.row('Cancel')
            with open('September.png', "rb") as file:
                data = file.read()
            bot.send_photo(message.from_user.id, photo=data)
            send = bot.send_message(message.chat.id, 'Choose some day', reply_markup=keyboard)
            bot.register_next_step_handler(send, typee)

        if message.text == 'October':
            keyboard = tb.types.ReplyKeyboardMarkup(True, False)
            keyboard.row('1', '2', '3', '4', '5')
            keyboard.row('6', '7', '8', '9', '10')
            keyboard.row('11', '12', '13', '14', '16')
            keyboard.row('17', '18', '19', '20', '21')
            keyboard.row('22', '23', '24', '25', '26')
            keyboard.row('27', '28', '29', '30', '31')
            keyboard.row('Cancel')
            with open('October.png', "rb") as file:
                data = file.read()
            bot.send_photo(message.from_user.id, photo=data)
            send = bot.send_message(message.chat.id, 'Choose some day', reply_markup=keyboard)
            bot.register_next_step_handler(send, typee)

        if message.text == 'November':
            keyboard = tb.types.ReplyKeyboardMarkup(True, False)
            keyboard.row('1', '2', '3', '4', '5')
            keyboard.row('6', '7', '8', '9', '10')
            keyboard.row('11', '12', '13', '14', '16')
            keyboard.row('17', '18', '19', '20', '21')
            keyboard.row('22', '23', '24', '25', '26')
            keyboard.row('27', '28', '29', '30')
            keyboard.row('Cancel')
            with open('November.png', "rb") as file:
                data = file.read()
            bot.send_photo(message.from_user.id, photo=data)
            send = bot.send_message(message.chat.id, 'Choose some day', reply_markup=keyboard)
            bot.register_next_step_handler(send, typee)

        if message.text == 'December':
            keyboard = tb.types.ReplyKeyboardMarkup(True, False)
            keyboard.row('1', '2', '3', '4', '5')
            keyboard.row('6', '7', '8', '9', '10')
            keyboard.row('11', '12', '13', '14', '16')
            keyboard.row('17', '18', '19', '20', '21')
            keyboard.row('22', '23', '24', '25', '26')
            keyboard.row('27', '28', '29', '30', '31')
            keyboard.row('Cancel')
            with open('December.png', "rb") as file:
                data = file.read()
            bot.send_photo(message.from_user.id, photo=data)
            send = bot.send_message(message.chat.id, 'Choose some day', reply_markup=keyboard)
            bot.register_next_step_handler(send, typee)

        if message.text == 'Journey':
            keyboard = tb.types.ReplyKeyboardMarkup(True, False)
            keyboard.row('1', '2', '3', '4', '5')
            keyboard.row('6', '7', '8', '9', '10')
            keyboard.row('11', '12', '13', '14', '16')
            keyboard.row('17', '18', '19', '20', '21')
            keyboard.row('22', '23', '24', '25', '26')
            keyboard.row('27', '28', '29', '30', '31')
            keyboard.row('Cancel')
            with open('Journey.png', "rb") as file:
                data = file.read()
            bot.send_photo(message.from_user.id, photo=data)
            send = bot.send_message(message.chat.id, 'Choose some day', reply_markup=keyboard)
            bot.register_next_step_handler(send, typee)

        if message.text == 'February':
            keyboard = tb.types.ReplyKeyboardMarkup(True, False)
            keyboard.row('1', '2', '3', '4', '5')
            keyboard.row('6', '7', '8', '9', '10')
            keyboard.row('11', '12', '13', '14', '16')
            keyboard.row('17', '18', '19', '20', '21')
            keyboard.row('22', '23', '24', '25', '26')
            keyboard.row('27', '28')
            keyboard.row('Cancel')
            with open('February.png', "rb") as file:
                data = file.read()
            bot.send_photo(message.from_user.id, photo=data)
            send = bot.send_message(message.chat.id, 'Choose some day', reply_markup=keyboard)
            bot.register_next_step_handler(send, typee)
        if message.text == 'March':
            keyboard = tb.types.ReplyKeyboardMarkup(True, False)
            keyboard.row('1', '2', '3', '4', '5')
            keyboard.row('6', '7', '8', '9', '10')
            keyboard.row('11', '12', '13', '14', '16')
            keyboard.row('17', '18', '19', '20', '21')
            keyboard.row('22', '23', '24', '25', '26')
            keyboard.row('27', '28', '29', '30', '31')
            keyboard.row('Cancel')
            with open('March.png', "rb") as file:
                data = file.read()
            bot.send_photo(message.from_user.id, photo=data)
            send = bot.send_message(message.chat.id, 'Choose some day', reply_markup=keyboard)
            bot.register_next_step_handler(send, typee)
        if message.text == 'April':
            keyboard = tb.types.ReplyKeyboardMarkup(True, False)
            keyboard.row('1', '2', '3', '4', '5')
            keyboard.row('6', '7', '8', '9', '10')
            keyboard.row('11', '12', '13', '14', '16')
            keyboard.row('17', '18', '19', '20', '21')
            keyboard.row('22', '23', '24', '25', '26')
            keyboard.row('27', '28', '29', '30')
            keyboard.row('Cancel')
            with open('April.png', "rb") as file:
                data = file.read()
            bot.send_photo(message.from_user.id, photo=data)
            send = bot.send_message(message.chat.id, 'Choose some day', reply_markup=keyboard)
            bot.register_next_step_handler(send, typee)
        if message.text == 'May':
            keyboard = tb.types.ReplyKeyboardMarkup(True, False)
            keyboard.row('1', '2', '3', '4', '5')
            keyboard.row('6', '7', '8', '9', '10')
            keyboard.row('11', '12', '13', '14', '16')
            keyboard.row('17', '18', '19', '20', '21')
            keyboard.row('22', '23', '24', '25', '26')
            keyboard.row('27', '28', '29', '30', '31')
            keyboard.row('Cancel')
            with open('May.png', "rb") as file:
                data = file.read()
            bot.send_photo(message.from_user.id, photo=data)
            send = bot.send_message(message.chat.id, 'Choose some day', reply_markup=keyboard)
            bot.register_next_step_handler(send, typee)

        elif message.text == 'Cancel':
            menu(message)




def typee(message):
    if message.text == 'English':
        keyboard = tb.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('homework', 'classwork')
        send = bot.send_message(message.chat.id, 'Choose type', reply_markup=keyboard)
        bot.register_next_step_handler(send, exercise)
    elif message.text == 'Cancel':
        menu(message)


def exercise(message):
    if message.text == 'homework':
        parser = cp.ConfigParser()
        parser.read('example.ini')
        msg = parser.get('1', 'homework')
        home = 'Your homework↓'
        keyboard = tb.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('Replay')
        send = bot.send_message(message.chat.id, home, reply_markup=keyboard)
        bot.send_message(message.from_user.id, text=msg)
        bot.register_next_step_handler(send, menu)
    elif message.text == 'Cancel':
        menu(message)


'''keyboard = tp.types.ReplyKeyboardMarkup(True, True)
keyboard.row('Monday', 'Tuesday')
keyboard.row('Wednesday', 'Thursday')
keyboard.row('Friday', 'Saturday','Sunday')
keyboard.row('Cancel')
        with open('September.png', "rb") as file:
            data =file.read()
        bot.send_photo(message.from_user.id, photo=data)'''

bot.polling(none_stop=True, interval=0)
bot.load_next_step_handlers()
bot.enable_save_next_step_handlers(delay=0)
