import start
import pymysql
from func import *
from auth import *
import os

os.system('start.py')

try:
    with open("pass.txt", "r") as file:
        psw = file.read()
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user='root',
        password=psw,  # вставить свой пароль
        database='musei',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        while True:
            zapros = buttonbox("Войдите в аккаунт или же зарегестрируйтесь:", "Sign", ["Авторизация", "Регистрация", "Выход"])
            if zapros == "Авторизация":
                if authorization(connection):
                    while True:
                        enter_action = buttonbox("Выберите действие", "Menu",
                                                 ["Посмотреть экспонаты", "Добавить экспонат", "Удалить экспонат",
                                                  "Изменить экспонат", "Выход"])
                        if enter_action == "Посмотреть экспонаты":
                            what_check = buttonbox("По какому критерию хотите посмотреть?", "Check", ["Посмотреть все", "Инфо по определенному экспонату", "Экспонаты других людей", "По критерию"])
                            if what_check == "Посмотреть все":
                                pass
                            elif what_check == "Инфо по определенному экспонату":
                                if not show_exhibit(connection):
                                    msgbox("Данного экспоната не найдено")
                            elif what_check == "Экспонаты других людей":
                                show_users_exp(connection)
                            elif what_check == "По критерию":
                                show_by_criterion(connection)
                        elif enter_action == "Добавить экспонат":
                            if add(connection):
                                msgbox("Данные успешно добавлены")
                            else:
                                msgbox("Операция отменена")
                        elif enter_action == "Удалить экспонат":
                            if delete_ex(connection):
                                msgbox("Данные успешно удалены")
                            else:
                                msgbox("Операция отменена")
                        elif enter_action == "Изменить экспонат":
                            pass
                            # msgbox(checkCart(connection, auto_enter[0].lower()))
                        else:
                            break
                else:
                    msgbox("Неверный логин или пароль")

            elif zapros == "Регистрация":
                if registration(connection):
                    msgbox("Успешная регистрация")
            else:
                break
    finally:
        connection.close()
except Exception as ex:
    print(ex)