from easygui import *
login = ''
password = ''
def authorization(connection):
    global login
    global password
    with connection.cursor() as cursor:
        show_all = "SELECT login, password FROM `users`"
        cursor.execute(show_all)
        result = cursor.fetchall()
    while True:
        author = multpasswordbox('Введіть данні для авторизації', 'authorizaton', ['Login', 'Password'])
        if result:
            for i in result:
                if author[0].lower() == i.get('login') and author[1] == i.get('password'):
                    msgbox('Авторизація успішна')
                    login = author[0].lower()
                    password = author[1].lower()
                    return True
                else:
                    msgbox("Авторизація не успішна, спробуйте ще.")
                    return False
        else:
            return False


def registration(connection):
    global login
    global password
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT login FROM `users`')
        result = cursor.fetchall()
    while True:
        info = multpasswordbox('Введіть данні для реєстрації', 'registration', ['Name', 'Login', 'Password'])
        if result:
            for e in result:
                if info[1].lower() == e.get('login'):
                    msgbox('Такий логін вже існує вигадайте інший.')
                else:
                    login = info[1].lower()
                    with connection.cursor() as cursor:
                        cursor.execute(f"INSERT INTO `users` (name, login, password) VALUES ('{info[0]}', '{info[1].lower()}', '{info[2]}');")
                        connection.commit()
                    return True
        else:
            login = info[1].lower()
            with connection.cursor() as cursor:
                cursor.execute(f"INSERT INTO `users` (name, login, password) VALUES ('{info[0]}', '{info[1].lower()}', '{info[2]}');")
                connection.commit()
            return True
