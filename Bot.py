import logging
logging.basicConfig(level=logging.INFO)

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
    item7 = types.KeyboardButton("🖼️Фото розкла⁠ду")

    markup1.add(item1, item2, item3, item4, item5)
    markup1.add(item6, item7)

    bot.send_message(message.chat.id,"Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы ""показывать расписание.".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup1)


@bot.message_handler(content_types=['text'])
def lalala(message):
        if message.text == 'Понеділок󠀠':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("1             ", callback_data='1')
            item2 = types.InlineKeyboardButton("Укр.Мова", callback_data='mova')
            item3 = types.InlineKeyboardButton(text='Meet', url='http://example.com/')
            item4 = types.InlineKeyboardButton("2             ", callback_data='2')
            item5 = types.InlineKeyboardButton("Машин. взаєм", callback_data='machin')
            item6 = types.InlineKeyboardButton(text='Meet', url='http://example.com/')
            item7 = types.InlineKeyboardButton("3             ", callback_data='3')
            item8 = types.InlineKeyboardButton("Англ.Мова/ ОП. та АМ.", callback_data='angl/op')
            item9 = types.InlineKeyboardButton("Meet", callback_data='angl/op_meet')
            item10 = types.InlineKeyboardButton("4             ", callback_data='4')
            item11 = types.InlineKeyboardButton("ОП. та АМ.", callback_data='op&am')
            item12 = types.InlineKeyboardButton(text='Meet', url='http://example.com/')
           
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)

            bot.send_message(message.chat.id, 'Розклад на понеділок:', reply_markup=markup)


        elif message.text == 'Вівторок󠀠':

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("1             ", callback_data='1')
            item2 = types.InlineKeyboardButton("Англ.Мова", callback_data='angl')
            item3 = types.InlineKeyboardButton("Meet", callback_data='angl_meet')
            item4 = types.InlineKeyboardButton("2             ", callback_data='2')
            item5 = types.InlineKeyboardButton("Маркетинг", callback_data='market')
            item6 = types.InlineKeyboardButton(text='Meet', url='http://example.com/')

            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, 'Розклад на вівторок:', reply_markup=markup)    

        
        elif message.text == 'Середа󠀠':

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("1             ", callback_data='1')
            item2 = types.InlineKeyboardButton("Пусто/ Комп.схем", callback_data='comp')
            item3 = types.InlineKeyboardButton(text='Meet', url='http://example.com/')
            item4 = types.InlineKeyboardButton("2             ", callback_data='2')
            item5 = types.InlineKeyboardButton("Комп.схем", callback_data='comp')
            item6 = types.InlineKeyboardButton(text='Meet', url='http://example.com/')
            item7 = types.InlineKeyboardButton("3             ", callback_data='3')
            item8 = types.InlineKeyboardButton("ОКМ", callback_data='okm')
            item9 = types.InlineKeyboardButton(text='Meet', url='http://example.com/')
            item10 = types.InlineKeyboardButton("4             ", callback_data='4')
            item11 = types.InlineKeyboardButton("ОКМ", callback_data='okm')
            item12 = types.InlineKeyboardButton(text='Meet', url='http://example.com/')

            markup.add(item1, item2, item3, item4, item5, item6,item7, item8, item9, item10, item11, item12)
            bot.send_message(message.chat.id, 'Розклад на середу:', reply_markup=markup)

        
        elif message.text == 'Четвер󠀠':

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("1             ", callback_data='1')
            item2 = types.InlineKeyboardButton("Пусто", callback_data='bad')
            item3 = types.InlineKeyboardButton("-", callback_data='bad')
            item4 = types.InlineKeyboardButton("2             ", callback_data='2')
            item5 = types.InlineKeyboardButton("Маркетинг", callback_data='market')
            item6 = types.InlineKeyboardButton(text='Meet', url='http://example.com/')
            item7 = types.InlineKeyboardButton("3             ", callback_data='3')
            item8 = types.InlineKeyboardButton("Фіз-ра", callback_data='fizra')
            item9 = types.InlineKeyboardButton(text="Class", url='http://example.com/')
            item10 = types.InlineKeyboardButton("4             ", callback_data='4')
            item11 = types.InlineKeyboardButton("Пусто/ Укр.Мова", callback_data='mova')
            item12 = types.InlineKeyboardButton(text='Meet', url='http://example.com/')

            markup.add(item1, item2, item3, item4, item5, item6,item7, item8, item9, item10, item11, item12)
            bot.send_message(message.chat.id, 'Розклад на четвер:', reply_markup=markup)


        elif message.text == "П'ятниця󠀠":

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("1             ", callback_data='1')
            item2 = types.InlineKeyboardButton("Дискр.математ", callback_data='duskrmat')
            item3 = types.InlineKeyboardButton(text='Meet', url='http://example.com/')
            item4 = types.InlineKeyboardButton("2             ", callback_data='2')
            item5 = types.InlineKeyboardButton("Дискр.математ", callback_data='duskrmat')
            item6 = types.InlineKeyboardButton(text='Meet', url='http://example.com/')

            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, "Розклад на п'ятницю:", reply_markup=markup)      


        elif message.text == '🗓️Розклад дзвінків':
            
            bot.send_message(message.chat.id, "I пара:  8:30—9:50\nII пара:  10:00—11:20\nIII пара:  11:50—13:10\nIV пара:  13:20—14:40\nV пара:  14:50—16:10\nVI пара:  16:20—17:40\nVII пара:  17:50—19:10", parse_mode = 'HTML')

        elif message.text == '🖼️Фото розкла⁠ду':

            img = open('Photo.PNG', 'rb')
            bot.send_photo(message.chat.id, img)
  
       


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
            
            elif call.data == 'machin':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Люд - машин. взаем. \nВчитель: Апенько Наталія Вікторівна')
            elif call.data == 'comp':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Комп. Схемотехніка \nВчитель: Кашкевич І.Ф.')
            elif call.data == 'angl':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Англ.Мова \nВчитель1: Миголь Валентина Миколаївна\n\nВчитель2: Горобець Людмила Миколаївна')                
            elif call.data == 'fizra':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Фіз-ра \nВчитель: Ірина Бистріцька')
            elif call.data == 'op&am':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Оп. та Ам.\nВчитель: Краліна Ганна Сергіївна')
            elif call.data == 'opsis':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Оп.систем \nВчитель: Нечипурук Олена Петрівна') 
            elif call.data == 'duf':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Диф.рівняння \nВчитель: Попов Петро Аркадійович')
            elif call.data == 'filosv':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Філософія \nВчитель: Забродська Анна Олександрівна')
            elif call.data == 'okm':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Орг.комп.мереж. \nВчитель: Кириченко В.С.')
            elif call.data == 'duskrmat':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Дискр.математ. \nВчитель: Попов Петро Аркадійович')                                  
            elif call.data == 'angl/op':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Англ.Мова/ ОП. та АМ. \n\nАнгл.Мова \nВчитель1: Миголь Валентина Миколаївна\nВчитель2: Горобець Людмила Миколаївна\n\nОп. та Ам.\nВчитель: Краліна Ганна Сергіївна')                                  
            elif call.data == 'mova':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Укр.Мова \nВчитель: Ткаченко Роман Петрович')                                  
            elif call.data == 'market':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Осн. менедж.та маркетин. \nВчитель: Шмалько Ілона Артурівна')                                  


            elif call.data == 'angl_meet':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton(text='1-ша группа', url='http://example.com/')
                item2 = types.InlineKeyboardButton(text='2-га группа', url='http://example.com/')
                markup.add(item1, item2)
                bot.send_message(call.message.chat.id, 'Англ.Мова Meet', reply_markup=markup)
                
                
            elif call.data == 'angl/op_meet':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton(text='1-ша группа', url='http://example.com/')
                item2 = types.InlineKeyboardButton(text='2-га группа', url='http://example.com/')
                item3 = types.InlineKeyboardButton(text='ОП. та АМ. Meet', url='http://example.com/')
                markup.add(item1, item2)
                markup.add(item3)
                bot.send_message(call.message.chat.id, 'Англ.Мова/ ОП. та АМ. Meet:', reply_markup=markup)
                
                
            elif call.data == 'bad':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=" ")
                
    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
