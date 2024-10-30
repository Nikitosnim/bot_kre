import telebot
from telebot import types
import config

token='7534253356:AAENDyCcDsF_9_0H1Ea68ZNWL2Ov8PvUy2A'
bot = telebot.TeleBot(token)

new='''


'''
new1='''Приветствую вас!

В танцевальном мире меня знают как Кремушку, расскажу про себя поподробнее.

✨ Исполнитель, педагог-хореограф танцевального направления tribal fusion с мировым именем
✨ Ролики с моим участием собрали более 100 млн. просмотров на различных платформах
✨ Преподавала певице Шакире
✨ Провожу мастер-классы по всему миру
✨ Участница ТВ проектов Танцы на ТНТ и Танцуй на Первом
✨ Выступала в Дубае (ОАЭ) и Ченнаи (Индия) в коллаборации с обладателем оскара за лучший саундтрек к фильму A. R. Rahman
✨ Выступала в Москве в коллаборации с популярной австралийской певицей Перукуа
'''
ofline="""Информация о занятиях

На текущий момент проводятся только индивидуальные занятия.

• Онлайн - 6 000 ₽ / 60 мин.
• Офлайн - 7 000 ₽ / 60 мин.

Место проведения
Москва, пр. Вернадского, д. 29, ТЦ «Лето», 5 этаж, школа танцев «Максимум».

Понедельник - зал «Магистраль»
Среда - зал «Дуэт»
Пятница - зал «Магистраль»

Оплата производится ДО занятия путём перевода на одну из карт

💳 Райффайзенбанк: 4476246127687735
💳 Сбербанк:
5336690153111259

❗️Скрин об оплате индивидуальных занятий присылается на 
на номер WhatsApp, Telegram +79165085511

По вопросам сотрудничества

WhatsApp, Telegram +79777665110
kremushka.classes@gmail.com
@kremushkaclasses
"""
present="""
Прекрасный подарок для любой женщины - индивидуальное занятие с Кремушкой!

После произведения оплаты вы получите подарочный сертификат. 

Пожалуйста, ознакомьтесь с информацией о занятиях ниже.
"""
soob1="""
С удовольствием приглашаю вас к себе в канал, где мы

✨ наслаждаемся танцами

🐚 общаемся на различные темы

💫 учимся лучше владеть собственным телом, накапливая женскую энергии

Всегда рада новым участницам!

"""
play="""Вы хотели бы получить музыкальное сокровище, что Кремушка копила годами?

Особенно полезно для танцующих трайбл
"""

q="""
Спасибо за уделённое время! Пожалуйста, пройдите по ссылке для вступления в сообщество

((Добавим ссылку после))
"""

z="""
Информация о занятиях

• Онлайн - 6 000 ₽ / 60 мин.
• Офлайн - 7 000 ₽ / 60 мин.

Место проведения
Москва, пр. Вернадского, д. 29, ТЦ «Лето», 5 этаж, школа танцев «Максимум».

Понедельник - зал «Магистраль»
Среда - зал «Дуэт»
Пятница - зал «Магистраль»

Оплата производится ДО занятия путём перевода на одну из карт

💳 Райффайзенбанк: 4476246127687735
💳 Сбербанк:
5336690153111259

❗️Скрин об оплате индивидуальных занятий присылается на 
на номер WhatsApp, Telegram +79154381775

Остались вопросы - пишите

@kremushkaclasses
@krema_support
"""

@bot.message_handler(commands=['start'])
def handle_start(message):

  # Создание меню
  keyboard = types.ReplyKeyboardMarkup(row_width=2)
  button1 = types.KeyboardButton('Офлайн-занятие')
  button2 = types.KeyboardButton('Онлайн-обучение')
  button3 = types.KeyboardButton('Занятие в подарок')
  button4 = types.KeyboardButton('Женское сообщество')
  button5 = types.KeyboardButton('Плейлист для танцев')
  keyboard.add(button1, button2, button3,button4,button5)

  # Отправка сообщения с клавиатурой
  photo = open('./nach.jpg', 'rb')
  photo1=open('photo1.mp4','rb')
  bot.send_photo(message.chat.id,photo,caption=new1)
  bot.send_video(message.chat.id,photo1,caption='Через танец мы транслируем женственность в мир',reply_markup=keyboard)
@bot.message_handler(func=lambda message: True)

def handle_message(message):

  if message.text == 'Офлайн-занятие':
      # Действия при нажатии на кнопку Офлайн занятие
      bot.reply_to(message, ofline)

  elif message.text == 'Онлайн-обучение':
      # Действия при нажатии на кнопку Онлайн-обучение
      keyboard2 = types.ReplyKeyboardMarkup(row_width=1)
      but1=types.KeyboardButton('Обучающий ролик')
      but2=types.KeyboardButton('Записи с интенсива')
      but3=types.KeyboardButton('Хочу онлайн-курс')
      but4 = types.KeyboardButton('Домой')
      keyboard2.add(but1,but2,but3,but4)
      bot.reply_to(message,'Онлайн-обучение',reply_markup=keyboard2)
  elif message.text == 'Обучающий ролик':
      video = open('video.mp4', 'rb')
      bot.send_video(message.chat.id,video)
  elif message.text == 'Записи с интенсива':
      video1=open('video1.mp4','rb')
      bot.send_video(message.chat.id, video1)
      video2=open('video2.mp4','rb')
      bot.send_video(message.chat.id, video2)
      video3=open('video3.mp4','rb')
      bot.send_video(message.chat.id, video3)
  elif message.text == 'Хочу онлайн-курс':

      markup = types.InlineKeyboardMarkup()
      button1 = types.InlineKeyboardButton('Oнлайн-курс',url='https://kremushka.com/okunis-v-moj-mir-tanca')
      markup.add(button1)
      bot.send_message(message.chat.id,'Oнлайн-курс', reply_markup=markup)



  elif message.text == 'Занятие в подарок':
      # Действия при нажатии на кнопку Занятие в подарок
      keyboard1 = types.ReplyKeyboardMarkup(row_width=1)
      button = types.KeyboardButton('Да')
      back = types.KeyboardButton("Домой")
      keyboard1.add(button,back)
        #выводит
      photo11=open('photo11.jpg','rb')
      bot.send_photo(message.chat.id,photo11,caption=present)
      bot.reply_to(message,z)
      bot.reply_to(message,'Произвели оплату и отправили скрин?',reply_markup=keyboard1)

  elif message.text=='Да':

      keyboard = types.ReplyKeyboardMarkup(row_width=2)
      button1 = types.KeyboardButton('Офлайн-занятие')
      button2 = types.KeyboardButton('Онлайн-обучение')
      button3 = types.KeyboardButton('Занятие в подарок')
      button4 = types.KeyboardButton('Женское сообщество')
      button5 = types.KeyboardButton('Плейлист для танцев')
      keyboard.add(button1, button2, button3, button4, button5)

      photo=open('./present.jpg','rb')
      bot.send_photo(message.chat.id,photo,reply_markup=keyboard)

  elif message.text=="Домой":

      keyboard = types.ReplyKeyboardMarkup(row_width=2)
      button1 = types.KeyboardButton('Офлайн-занятие')
      button2 = types.KeyboardButton('Онлайн-обучение')
      button3 = types.KeyboardButton('Занятие в подарок')
      button4 = types.KeyboardButton('Женское сообщество')
      button5 = types.KeyboardButton('Плейлист для танцев')
      keyboard.add(button1, button2, button3, button4, button5)

      bot.reply_to(message,'Дом, милый дом',reply_markup=keyboard,disable_notification=True)


  elif message.text == 'Женское сообщество':
      # Действия при нажатии на кнопку Женское сообщество

      keyboard1 = types.ReplyKeyboardMarkup()
      button = types.KeyboardButton('Подать заявку на вступление')
      keyboard1.add(button)
      photo=open('./soob.jpg','rb')
      bot.send_photo(message.chat.id,photo,caption=soob1,reply_markup=keyboard1)
  elif message.text == 'Подать заявку на вступление':
      bot.reply_to(message, 'Опишите себя пятью словами:')



  elif message.text == 'Плейлист для танцев':
      # Действия при нажатии на кнопку Плейлист для танцев
      keyboard1 = types.ReplyKeyboardMarkup(row_width=1)
      button = types.KeyboardButton('Очень хочу!!!')
      button1=types.KeyboardButton('Домой')
      keyboard1.add(button,button1)
      bot.reply_to(message,play,reply_markup=keyboard1)
  elif message.text == 'Очень хочу!!!':
      markup = types.InlineKeyboardMarkup()
      button1 = types.InlineKeyboardButton('Кнопка "Слушать плейлист"', url='https://music.yandex.ru/users/yanakrem/playlists/3?utm_medium=copy_link')
      markup.add(button1)
      bot.send_message(message.chat.id, 'Слушать плейлист', reply_markup=markup)
  else:
      keyboard = types.ReplyKeyboardMarkup(row_width=2)
      button1 = types.KeyboardButton('Офлайн-занятие')
      button2 = types.KeyboardButton('Онлайн-обучение')
      button3 = types.KeyboardButton('Занятие в подарок')
      button4 = types.KeyboardButton('Женское сообщество')
      button5 = types.KeyboardButton('Плейлист для танцев')
      keyboard.add(button1, button2, button3, button4, button5)
      bot.send_message(message.chat.id, q, reply_markup=keyboard)



bot.polling(none_stop=True,interval=0)