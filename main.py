from easygui import *
import os.path
import pymysql
from func import add

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user='root',
        password='DataBase0321',  # вставить свой пароль
        database='musei',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Welcome to the Database!")
    try:
        while True:
            zapros = buttonbox("Выбор:", "Enter", ["Авторизация", "Регистрация", "Выход"])
            if zapros == "Авторизация":
                if os.path.exists("pass.txt"):
                    with open("pass.txt", "r") as file:
                        auto_enter = file.readlines()
                    auto_enter = [i.rstrip() for i in auto_enter]
                    if authorization(auto_enter[0], auto_enter[1], connection):
                        while True:
                            enter_action = buttonbox("Выберите действие", "Menu", ["Посмотреть ассортимент", "Купить продукты", "Посмотреть корзину", "Удалить из корзины", "Очистить корзину", "Выход"])
                            if enter_action == "Посмотреть ассортимент":
                                msgbox(outputProduct(connection))
                            elif enter_action == "Купить продукты":
                                msgbox(insertCart(connection, auto_enter[0].lower()))
                            elif enter_action == "Посмотреть корзину":
                                msgbox(checkCart(connection, auto_enter[0].lower()))
                            elif enter_action == "Удалить из корзины":
                                msgbox(deleteCart(connection, auto_enter[0].lower()))
                            elif enter_action == "Очистить корзину":
                                msgbox(cleanTrash(connection, auto_enter[0].lower()))
                            else:
                                break
                    else:
                        log_pass = multpasswordbox("Enter login and password for authorization:", "Enter", ["Login:", "Pass:"])
                        if authorization(log_pass[0], log_pass[1], connection):
                            with open("pass.txt", "w") as file:
                                file.write(log_pass[0] + "\n" + log_pass[1])
                            while True:
                                enter_action = buttonbox("", "", ["Посмотреть ассортимент", "Купить продукты", "Посмотреть корзину", "Удалить из корзины", "Очистить корзину", "Выход"])
                                if enter_action == "Посмотреть ассортимент":
                                    msgbox(outputProduct(connection))
                                elif enter_action == "Купить продукты":
                                    msgbox(insertCart(connection, log_pass[0].lower()))
                                elif enter_action == "Посмотреть корзину":
                                    msgbox(checkCart(connection, log_pass[0].lower()))
                                elif enter_action == "Удалить из корзины":
                                    msgbox(deleteCart(connection, log_pass[0].lower()))
                                elif enter_action == "Очистить корзину":
                                    msgbox(cleanTrash(connection, log_pass[0].lower()))
                                else:
                                    break
                        else:
                            msgbox("Неверный пароль или данный логин еще не зарегестрирован!")
                else:
                    log_pass = multpasswordbox("Enter login and password for authorization:", "Enter", ["Login:", "Pass:"])
                    if authorization(log_pass[0], log_pass[1], connection):
                        with open("pass.txt", "w") as file:
                            file.write(log_pass[0] + "\n" + log_pass[1])
                        while True:
                            enter_action = buttonbox("", "", ["Посмотреть ассортимент", "Купить продукты", "Посмотреть корзину", "Удалить из корзины", "Очистить корзину", "Выход"])
                            if enter_action == "Посмотреть ассортимент":
                                msgbox(outputProduct(connection))
                            elif enter_action == "Купить продукты":
                                msgbox(insertCart(connection, log_pass[0].lower()))
                            elif enter_action == "Посмотреть корзину":
                                msgbox(checkCart(connection, log_pass[0].lower()))
                            elif enter_action == "Удалить из корзины":
                                msgbox(deleteCart(connection, log_pass[0].lower()))
                            elif enter_action == "Очистить корзину":
                                msgbox(cleanTrash(connection, log_pass[0].lower()))
                            else:
                                break
                    else:
                        msgbox("Неверный пароль или данный логин еще не зарегестрирован!")
            elif zapros == "Регистрация":
                log_pass = multpasswordbox("Enter login and password for registration:", "Enter", ["Name:", "Login:", "Pass:"])
                msgbox(registration(log_pass[1], log_pass[2], log_pass[0], connection))
                with open("pass.txt", "w") as file:
                    file.write(log_pass[0] + "\n" + log_pass[1])
            else:
                break
    finally:
        connection.close()

except Exception as ex:
    print(ex)