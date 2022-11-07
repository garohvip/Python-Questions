def add(insert_info, connection):                       # Через інтерфейс(multenterbox) отримуємо всю інфу списком
    with connection.cursor() as cursor:
        data = "insert into `exhibit` (nameExhibit, year, description) values " \
                             f"('{insert_info[0]}', '{insert_info[1]}', '{insert_info[2]}')"
        cursor.execute(data)
        connection.commit()

def delete_ex(nameExhibit, connection):

    with connection.cursor() as cursor:
        create_table = f"DELETE FROM `exhibit` WHERE nameExhibit = {nameExhibit};"
        cursor.execute(create_table)
        connection.commit()