# this project is about telegram assistant chatbot of a certain groups of the IT college

import telebot
import logging
from telebot import types

# Токен бота
API_TOKEN = '7865938795:AAHWUVC-ToZ3Qx23BSyc05XENPqcSGrJHwA'
bot = telebot.TeleBot(API_TOKEN)

logging.basicConfig(level=logging.INFO)

# Основное меню групп
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    # Кнопки для всех групп
    groups = ['CS21', 'CS22', 'CS23', 'CS24', 'CS25']
    for group in groups:
        markup.add(types.InlineKeyboardButton(text=group, callback_data=f"group_{group}"))
    bot.send_message(message.chat.id, "Выберите группу:", reply_markup=markup)

# Обработчик выбора группы
@bot.callback_query_handler(func=lambda call: call.data.startswith("group_"))
def group_selection(call):
    group = call.data.split("_")[1]
    if group == "CS25":
        # Показать меню для группы CS25
        show_cs25_menu(call.message)
    else:
        bot.answer_callback_query(call.id, "Эта группа пока не поддерживается.")

# Меню для группы CS25
def show_cs25_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    # Кнопки для действий группы CS25
    markup.add(
        types.InlineKeyboardButton("Список учащихся", callback_data="students_list"),
        types.InlineKeyboardButton("Добавить домашнее задание", callback_data="add_homework"),
        types.InlineKeyboardButton("Расписание", url="https://docs.google.com/spreadsheets/d/1SZxYMnyEgPgMIyFvcisNarYN0pZjZxQ4/edit?hl=ru&pli=1&gid=331563060#gid=331563060"),
        types.InlineKeyboardButton("Уведомить всех", callback_data="notify_all")
    )
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

# Обработчики для действий группы CS25
@bot.callback_query_handler(func=lambda call: call.data == "students_list")
def students_list(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Список учащихся группы CS25:\n- Апиев Билал\n- Бекназаров Ильяз\n- Акеев Белек")

@bot.callback_query_handler(func=lambda call: call.data == "add_homework")
def add_homework(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Введите домашнее задание для группы CS25:")

@bot.callback_query_handler(func=lambda call: call.data == "notify_all")
def notify_all(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Уведомления отправлены всем учащимся группы CS25.")

# Запуск бота
bot.polling()
