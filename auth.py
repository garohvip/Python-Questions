def authorization(connection):

    try:
        with connection.cursor() as cursor:
            show_all = "SELECT login, password FROM `users`"
            cursor.execute(show_all)
            result = cursor.fetchall()

        valid = False
        while valid:
            author = multpasswordbox('Введіть данні для авторизації', 'authorizaton', ['Login', 'Password'])
            for i in result:

                if author[0].lower == i.get('login') and author[1].lower == i.get('password'):
                    msgbox('Авторизація успішна')
                    valid = True

                else:
                    msgbox("Авторизація не успішна, спробуйте ще.")
                    valid = False
                    return True

    finally:
        return True

def registration(connection):

    try:
        with connection.cursor() as cursor:
            show_all = 'SELECT login FROM `users`'
            cursor.execute(show_all)
            result = cursor.fetchall()
        valid = False
        while valid:
            info = multpasswordbox('Введіть данні для реєстрації', 'registration', ['Name','Login', 'Password'])
            for e in result:

                if info[0] == e.get('login'):
                    msgbox('Такий логін вже існує вигадайте інший.')
                    valid = False

                else:
                    with connection.cursor() as cursor:
                        f"INSERT `users` (name, login, password) values ({info[0].lower},{info[1].lower},{info[2].lower}):
                        connection.commit()
                        valid = True
                        return True

    finally:
        return True