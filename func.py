from easygui import *
import auth


def add(connection):
    count = 0
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT nameExhibit FROM exhibit;""")
        check = cursor.fetchall()
    while True:
        insert_info = multenterbox("Введите данные нового экспоната:", "Add", ["Название:", "Год:", "Описание:"])
        for i in check:
            if i.get('nameExhibit') != insert_info[0]:
                count += 1
        if count == len(check):
            criterion = choicebox("Выберите критерий экспоната:", "Add", ["До нашей эры", "Наша эра"])
            if buttonbox(f"""Все ли верно?\n\nНазвание: {insert_info[0]}\nГод: {insert_info[1]}\nОписание: {insert_info[2]}\nКритерий {criterion}""") == "Добавить":
                with connection.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO exhibit (nameExhibit, year, description, criterion) VALUES ('{insert_info[0].title()}', {insert_info[1]}, '{insert_info[2]}', '{criterion.lower()}');""")
                    cursor.execute(f"""INSERT INTO userex (loginPerson, nameExhibit) VALUES ('{auth.login}', '{insert_info[0]}');""")
                    connection.commit()
                return True
            else:
                return False
        else:
            return msgbox("Данный экспонат уже есть в списке")

def show_exhibit(connection):
    enter = enterbox("Введите название экспоната")
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT * FROM exhibit WHERE = '{enter.title()}';""")
        result = cursor.fetchone()
    if result:
        return msgbox(f"№ {result.get('idEx')}\nНазвание: {result.get('nameExhibit')}\nГод: {result.get('year')}\nОписание: {result.get('description')}\nКритерий: {result.get('criterion')}")
    else:
        return False


def showAll(connection):
    with connection.cursor() as cursor:
        cursor.execute(f"select * from `exhibit`;")
        result = cursor.fetchall()
    generated_list = []
    for i in result:
        generated_list.append(f"№{i.get('idEx')}\nName: {i.get('nameExhibit')}\nYear: {i.get('year')}\n"
                              f"{i.get('criterion')}\nDescription - {i.get('description')}\n\n")
    return msgbox("\n".join(generated_list))


def delete_ex(connection):
    slash_n = "\n"
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT loginPerson, nameExhibit FROM userex WHERE loginPerson = '{auth.login}';")
        result = cursor.fetchall()
    if result:
        allexhibit = []
        for i in result:
            allexhibit.append(i.get('nameExhibit'))
        nameEx = enterbox(f"""Ваші експонати:\n\n{slash_n.join(allexhibit)}\n\nВведіть назву експонату для видалення""")  # Вивід назв експонатів, щоб користувач бачив що вводити
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM exhibit WHERE nameExhibit = '{nameEx.title()}';""")
            result = cursor.fetchone()
        if buttonbox(f"""Название: {result.get('nameExhibit')}\nГод: {result.get('year')}\nОписание: {result.get('description')}\nКритерий: {result.get('criterion')}""", "delete", ["Удалить", "Отмена"]) == "Удалить":
            with connection.cursor() as cursor:
                cursor.execute(f"""DELETE FROM userex WHERE loginPerson = '{auth.login}' AND nameExhibit = '{nameEx}';""")
                cursor.execute(f"""DELETE FROM exhibit WHERE nameExhibit = '{nameEx}';""")
                connection.commit()
            return True
        else:
            return False
    else:
        return msgbox("У Вас нет экспонатов")


def show_by_criterion(connection):                      # Вивід експонатів за критерієм на вибір
    choose_criterion = buttonbox("Choose criterion", "Choose criterion", ["Наша эра", "До нашей эры"])
    if choose_criterion == "Наша эра":
        with connection.cursor() as cursor:
            select_ad = "select * from exhibit where criterion = 'наша эра'"
            cursor.execute(select_ad)
            result = cursor.fetchall()
    elif choose_criterion == "До нашей эры":
        with connection.cursor() as cursor:
            select_bc = "select * from exhibit where criterion = 'до нашей эры'"
            cursor.execute(select_bc)
            result = cursor.fetchall()
    generated_list = []
    for i in result:
        generated_list.append(f"№{i.get('idEx')}\nName: {i.get('nameExhibit')}\nYear: {i.get('year')}\n"
                              f"{i.get('criterion')}\nDescription - {i.get('description')}\n\n")
    return msgbox("\n".join(generated_list))


def show_users_exp(connection):                        # Вивід всіх експонатів прив'язаних до одного певного користувача
    person = enterbox("Login", "Search person")
    with connection.cursor() as cursor:
        select_exhibit_names = f"select nameExhibit from userex where loginPerson = '{person.lower()}'"
        cursor.execute(select_exhibit_names)
        result = cursor.fetchall()
    exh_names = []
    for i in result:
        exh_names.append(f"{i.get('nameExhibit')}")
    end_exhibits = []
    with connection.cursor() as cursor:
        for i in exh_names:
            select_exhibits = f"select * from exhibit where nameExhibit = '{i}'"
            cursor.execute(select_exhibits)
            result = cursor.fetchone()
            end_exhibits.append(result)
    generated_list = []
    for i in end_exhibits:
        generated_list.append(f"№{i.get('idEx')}\nName: {i.get('nameExhibit')}\nYear: {i.get('year')}\n"
                              f"{i.get('criterion')}\nDescription - {i.get('description')}\n\n")
    return msgbox("\n".join(generated_list))
