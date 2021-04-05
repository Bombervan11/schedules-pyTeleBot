import telebot
import config
import random
import threading

from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Понеділок󠀠")
    item2 = types.KeyboardButton("Вівторок󠀠")
    item3 = types.KeyboardButton("Середа󠀠")
    item4 = types.KeyboardButton("Четвер󠀠")
    item5 = types.KeyboardButton("П'ятниця󠀠")
    item6 = types.KeyboardButton("🗓️Розклад дзвінків")

    markup1.add(item1, item2, item3, item4, item5)
    markup1.add(item6)

    bot.send_message(message.chat.id,"Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы ""показывать расписание.".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup1)


@bot.message_handler(content_types=['text'])
def lalala(message):
    # if message.chat.type == 'private':
        if message.text == 'Понеділок󠀠':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("1             ", callback_data='1')
            item2 = types.InlineKeyboardButton("Осн.інжен.ПЗ", callback_data='PZ')
            item3 = types.InlineKeyboardButton(text='Meet', url='https://meet.google.com/lookup/fm4xzjus75?authuser=2&hs=179')
            item4 = types.InlineKeyboardButton("2             ", callback_data='2')
            item5 = types.InlineKeyboardButton("Осн.інжен.ПЗ", callback_data='PZ')
            item6 = types.InlineKeyboardButton(text='Meet', url='https://meet.google.com/lookup/fm4xzjus75?authuser=2&hs=179')
            item7 = types.InlineKeyboardButton("3             ", callback_data='3')
            item8 = types.InlineKeyboardButton("Мат. аналіз", callback_data='matan')
            item9 = types.InlineKeyboardButton(text='Meet', url='https://meet.google.com/lookup/fm4xzjus75?authuser=2&hs=179')
            item10 = types.InlineKeyboardButton("4             ", callback_data='4')
            item11 = types.InlineKeyboardButton("Математика", callback_data='mat')
            item12 = types.InlineKeyboardButton("-", callback_data='bad')
           
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)

            bot.send_message(message.chat.id, 'Розклад на понеділок:', reply_markup=markup)
            # threading.Timer(30, target=bot.delete_message, args=(message.chat.id, message.message_id)).start()
        elif message.text == 'Вівторок󠀠':

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("1             ", callback_data='1')
            item2 = types.InlineKeyboardButton("Лін. Алгебра", callback_data='linalg')
            item3 = types.InlineKeyboardButton(text='Meet', url='https://meet.google.com/lookup/fwg46qyriw?authuser=2&hs=179')
            item4 = types.InlineKeyboardButton("2             ", callback_data='2')
            item5 = types.InlineKeyboardButton("Лін. Алгбр/ ОП. та АМ. ", callback_data='bad')
            item6 = types.InlineKeyboardButton("-",callback_data='bad')
            item7 = types.InlineKeyboardButton("3             ", callback_data='3')
            item8 = types.InlineKeyboardButton("ОП. та АМ.", callback_data='op&am')
            item9 = types.InlineKeyboardButton(text='Meet', url='https://meet.google.com/lookup/fraq6fp3ic?authuser=2&hs=179')
            item10 = types.InlineKeyboardButton("4             ", callback_data='4')
            item11 = types.InlineKeyboardButton("Фіз-ра", callback_data='fizra')
            item12 = types.InlineKeyboardButton("-", callback_data='bad')

            markup.add(item1, item2, item3, item4, item5, item6,item7, item8, item9, item10, item11, item12)
            bot.send_message(message.chat.id, 'Розклад на вівторок:', reply_markup=markup)    

        
        elif message.text == 'Середа󠀠':

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("1             ", callback_data='1')
            item2 = types.InlineKeyboardButton("Укр.Літ", callback_data='lit')
            item3 = types.InlineKeyboardButton(text='Meet', url='https://meet.google.com/lookup/cxvyd2ycgr?authuser=2&hs=179')
            item4 = types.InlineKeyboardButton("2             ", callback_data='2')
            item5 = types.InlineKeyboardButton("Соціологія", callback_data='soci')
            item6 = types.InlineKeyboardButton("-", callback_data='bad')
            item7 = types.InlineKeyboardButton("3             ", callback_data='3')
            item8 = types.InlineKeyboardButton("Право", callback_data='pravo')
            item9 = types.InlineKeyboardButton(text='Meet', url='https://meet.google.com/lookup/ellzuv5c3t?authuser=2&hs=179')
            item10 = types.InlineKeyboardButton("4             ", callback_data='4')
            item11 = types.InlineKeyboardButton("Мат. Аналіз", callback_data='matan')
            item12 = types.InlineKeyboardButton(text='Meet', url='https://meet.google.com/lookup/epvvrpika2?authuser=2&hs=179')

            markup.add(item1, item2, item3, item4, item5, item6,item7, item8, item9, item10, item11, item12)
            bot.send_message(message.chat.id, 'Розклад на середу:', reply_markup=markup)   
        
        elif message.text == 'Четвер󠀠':

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("1             ", callback_data='1')
            item2 = types.InlineKeyboardButton("БЖД", callback_data='BZD')
            item3 = types.InlineKeyboardButton(text='Meet', url='https://meet.google.com/lookup/bixoqk2lcc?authuser=0&hs=179')
            item4 = types.InlineKeyboardButton("2             ", callback_data='2')
            item5 = types.InlineKeyboardButton("Арх. Комп", callback_data='arch.comp')
            item6 = types.InlineKeyboardButton(text='Meet', url='https://meet.google.com/lookup/gyb2qhu7s2?authuser=2&hs=179')
            item7 = types.InlineKeyboardButton("3             ", callback_data='3')
            item8 = types.InlineKeyboardButton("Арх. Комп/ Фізика", callback_data='bad')
            item9 = types.InlineKeyboardButton("-", callback_data='bad')
            item10 = types.InlineKeyboardButton("4             ", callback_data='4')
            item11 = types.InlineKeyboardButton("Фізика", callback_data='fizika')
            item12 = types.InlineKeyboardButton(text='Meet', url='https://meet.google.com/vbi-sovd-gcn')

            markup.add(item1, item2, item3, item4, item5, item6,item7, item8, item9, item10, item11, item12)
            bot.send_message(message.chat.id, 'Розклад на четвер:', reply_markup=markup)

        elif message.text == "П'ятниця󠀠":

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("1             ", callback_data='1')
            item2 = types.InlineKeyboardButton("Англ.Мова", callback_data='angl')
            item3 = types.InlineKeyboardButton("-", callback_data='bad')
            item4 = types.InlineKeyboardButton("2             ", callback_data='2')
            item5 = types.InlineKeyboardButton("Укр.Мова", callback_data='mova')
            item6 = types.InlineKeyboardButton(text='Meet', url='https://meet.google.com/lookup/ggwrg5pegw?authuser=2&hs=179')
            # item7 = types.InlineKeyboardButton("3             ", callback_data='3')
            # item8 = types.InlineKeyboardButton("Захист Віт.", callback_data='bad')
            # item9 = types.InlineKeyboardButton("            №6", callback_data='bad')

            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, "Розклад на п'ятницю:", reply_markup=markup)      

        elif message.text == '🗓️Розклад дзвінків':
        	bot.send_message(message.chat.id, "I пара:  8:30—9:50\nII пара:  10:00—11:20\nIII пара:  11:50—13:10\nIV пара:  13:20—14:40\nV пара:  14:50—16:10\nVI пара:  16:20—17:40\nVII пара:  17:50—19:10", parse_mode = 'HTML')
       

        # else:
        #     bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == '1':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='I пара:  8:30—9:50')
            elif call.data == '2':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='II пара:  10:00—11:20')
            elif call.data == '3':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='III пара:  11:50—13:10')
            elif call.data == '4':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='IV пара:  13:20—14:40')  
            elif call.data == '5':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='V пара:  14:50—16:10')
            elif call.data == '6':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='VI пара:  16:20—17:40')              
            elif call.data == '7':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='VII пара:  17:50—19:10')
            
            elif call.data == 'PZ':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='==========Осн.інжен.ПЗ===========\nВчитель: Апенько Наталія Вікторівна')
            elif call.data == 'matan':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='===========Мат. Аналіз===========\nВчитель: Таращенко Людмила Анатоліївна')
            elif call.data == 'linalg':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='===========Лін. Алгебра==========\nВчитель: Таращенко Людмила Анатоліївна')                                
            elif call.data == 'matan':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='===========Мат. Аналіз===========\nВчитель: Таращенко Людмила Анатоліївна')
            elif call.data == 'linalg':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='===========Лін. Алгебра==========\nВчитель: Таращенко Людмила Анатоліївна') 
            elif call.data == 'mat':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='===========Математика===========\nВчитель: Шкарін Олександр Олександрович')
            elif call.data == 'lit':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='=============Укр.Літ============\nВчитель: Роман Ткаченко Петрович')
            elif call.data == 'mova':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='============Укр.Мова============\nВчитель: Максимчук Віра Борисівна')
            elif call.data == 'soci':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='===========Соціологія===========\nВчитель: Кривчиков Олег Володимирович')
            elif call.data == 'pravo':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='==============Право=============\nВчитель: Писарчук Валентина')
            elif call.data == 'BZD':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='===============БЖД==============\nВчитель: Ковальчук Наталія')
            elif call.data == 'arch.comp':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='============Арх.Комп============\nВчитель: Нечипурук Олена Володимирівна')
            elif call.data == 'fizika':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='=============Фізика=============\nВчитель: Кушнірова Марія Дмитрівна ')
            elif call.data == 'angl':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='============Англ.Мова===========\nВчитель1: Миголь Валентина Миколаївна\n\nВчитель2: Горобець Людмила')                
            elif call.data == 'fizra':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='==============Фіз-ра============\nВчитель: Ірина Бистріцька')
            elif call.data == 'op&am':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='===========Оп. та Ам.===========\nВчитель: Краліна Ганна ')                      


            elif call.data == 'bad':
            	bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=" ")
            	
    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
