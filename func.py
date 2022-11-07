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
        create_table = f"DELETE FROM `exhibit` WHERE nameExhibit = {nameExhibit};"
        cursor.execute(create_table)
        connection.commit()

def showUserex(connection):
    with connection.cursor() as cursor:
        select_result = cursor.execute(f"select * from 'userex';")
        cursor.execute(select_result)
        result = cursor.fetchall()
    result_return = []
    for e in result:
        result_return.append(f"{e.get('loginPerson')} > {e.get('nameExhibit')}")
    return