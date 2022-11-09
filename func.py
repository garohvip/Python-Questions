from easygui import *
import auth


def add(connection):
    insert_info = multenterbox("Add exhibit", "Add", ["Name", "Year", "Criterion[до нашей эры/наша эра]", "Description"])
    with connection.cursor() as cursor:
        data = "insert into `exhibit` (nameExhibit, year, criterion, description) values " \
                             f"('{insert_info[0]}', '{insert_info[1]}', '{insert_info[2]}', '{insert_info[3]}')"
        cursor.execute(data)
        connection.commit()


def showAll(connection):
    choice = buttonbox("Choice what", "Enter", ["All", "Single"])
    with connection.cursor() as cursor:
        select_all = cursor.execute(f"select * from `exhibit`;")
        cursor.execute(select_all)
        result = cursor.fetchall()
    if choice == "All":
        msgbox([e for e in result if result not [] f"{e.get('nameExhibit')} - Назва\n {e.get('year')} - рік\n{e.get('description')} - Опис\n"])
    elif choice == "Single":
        choose = enterbox("Enter name")
        msgbox([e for e in result if choose in e.get('nameExhibit') f"{e.get('nameExhibit')} - Назва\n {e.get('year')} - рік\n{e.get('description')} - Опис\n"])
    return True




def insertExp(connection):
    with connection.cursor() as cursor:
        cursor.execute(f"select * from `exhibit`;")
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
        select_result = cursor.execute(f"select * from `userex`;")
        cursor.execute(select_result)
        result = cursor.fetchall()
    result_return = []
    for e in result:
        result_return.append(f"'{e.get('loginPerson')}' > '{e.get('nameExhibit')}'")
    return


def show_users_exp(connection):                        # Вивід всіх експонатів прив'язаних до одного певного користувача
    person = enterbox("Login", "Search person")
    with connection.cursor() as cursor:
        select_exhibit_names = f"select nameExhibit from `userex` where loginPerson = '{person}'"
        cursor.execute(select_exhibit_names)
        result = cursor.fetchall()
        exh_names = []
        for i in result:
            exh_names.append(f"{i.get('nameExhibit')}")
        end_exhibits = []
        for i in exh_names:
            select_exhibits = f"select * from `exhibit` where nameExhibit = '{i}'"
            cursor.execute(select_exhibits)
            result = cursor.fetchone()
            end_exhibits.append(result)
        generated_list = []
        for i in end_exhibits:
            generated_list.append(f"№{i.get('idEx')} | Name: {i.get('nameExhibit')}, Year: {i.get('year')}"
                                  f" {i.get('criterion')}, Description - {i.get('description')}")
        msgbox("\n".join(generated_list))


def show_by_criterion(connection):                      # Вивід експонатів за критерієм на вибір
    choose_criterion = buttonbox("Choose criterion", "Choose criterion", ["Наша эра", "До нашей эры"])
    if choose_criterion == "Наша эра":
        with connection.cursor() as cursor:
            select_ad = "select * from `exhibit` where criterion = 'наша эра'"
            cursor.execute(select_ad)
            result = cursor.fetchall()
    elif choose_criterion == "До нашей эры":
        with connection.cursor() as cursor:
            select_bc = "select * from `exhibit` where criterion = 'до нашей эры'"
            cursor.execute(select_bc)
            result = cursor.fetchall()
    generated_list = []
    for i in result:
        generated_list.append(f"№{i.get('idEx')} | Name: {i.get('nameExhibit')}, Year: {i.get('year')}"
                              f" {i.get('criterion')}, Description - {i.get('description')}")
    msgbox("\n".join(generated_list))

