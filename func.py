from easygui import *
import auth


def add(insert_info, connection):                       # Через інтерфейс(multenterbox) отримуємо всю інфу списком
    with connection.cursor() as cursor:
        data = "insert into `exhibit` (nameExhibit, year, description) values " \
                             f"('{insert_info[0]}', '{insert_info[1]}', '{insert_info[2]}')"
        cursor.execute(data)
        connection.commit()


def showAll(connection):
    choice = buttonbox("Choice what", "Enter", ["All", "By ID"])
    if choice == "All":
        with connection.cursor() as cursor:
            select_all = cursor.execute(f"select * from 'exhibit';")
            cursor.execute(select_all)
            result = cursor.fetchall()
            msgbox(result)
    elif choice == "By ID":
        choice = int(enterbox("Enter id:"))
        with connection.cursor() as cursor:
            select_all = cursor.execute(f"select * from 'exhibit' where id = {choice};")
            cursor.execute(select_all)
            result = cursor.fetchall()
            msgbox(result)


def insertExp(connection):
    with connection.cursor() as cursor:
        cursor.execute(f"select * from 'exhibit';")
        output = cursor.fetchall()
    ins = choicebox("Choice", "Here", ["some", "someone"])
    inp = multenterbox()


def delete_ex(nameExhibit, connection):

    with connection.cursor() as cursor:
        create_table = f"SELECT loginPerson, nameExhibit FROM `userex` WHERE loginPerson = '{auth.login}';"             #ми беремо логін і ім'я користувача
        cursor.execute(create_table)
        result = cursor.fetchall()
        usersExhibit = []                                                                                               # Ліст для назв експонатів, авторизованого користувача
        for e in result:                                                                                                # Цикл для поповнення ліста
            usersExhibit.append(e.get('nameExhibit'))
            break

    valid = False
    while valid:                                                                                                        #цикл щоб у користувача було декілька спроб ввести вірно
        nameEx = enterbox(f"Ваші експонати: '{usersExhibit}'\nВведіть назву експонату для видалення")                   #Вивід назв експонатів, щоб користувач бачив що вводити
        if nameEx not in usersExhibit:                                                                                  #Перевірка на правильність вводу
                msgbox('Данного експонату не знайдено')
                valid = False
                continue
        else:
            with connection.cursor() as cursor:
                show_info = f"SELECT * FROM `exhibit` WHERE nameExhibit = '{nameEx}';"                                  #Якшо все ок, запит на бд для виведення всього про експонат
                cursor.execute(show_info)
                result = cursor.fetchall()
                for e in result:
                    after_del = buttonbox(f"{e.get('nameExhibit')} - Назва експонату\n{e.get('year')} - Рік експонату\n"#розпарсили данні з дікта
                                          f"{e.get('description')} - Опис експонату", 'DELETE', ['Видалити', 'Відміна'])#запит на видалення, дві кнопки

                    if after_del == 'Видалити':                                                                         #Якшо +, то видаляємо із бази exhibit та userex
                        with connection.cursor() as cursor:
                            create_table = f"DELETE FROM `exhibit` WHERE nameExhibit = '{nameEx}';"
                            cursor.execute(create_table)
                            connection.commit()
                        with connection.cursor() as cursor:
                            create_table = f"DELETE FROM `userex` WHERE nameExhibit = '{nameEx}';"
                            cursor.execute(create_table)
                            connection.commit()
                            return True
                    else:                                                                                               #Якшо ні, то закінчуємо функцію
                        valid = True
                        return True


def showUserex(connection):
    with connection.cursor() as cursor:
        select_result = cursor.execute(f"select * from 'userex';")
        cursor.execute(select_result)
        result = cursor.fetchall()
    result_return = []
    for e in result:
        result_return.append(f"'{e.get('loginPerson')}' > '{e.get('nameExhibit')}'")
    return

