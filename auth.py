def __init__(self,login,password):
    self.login = login
    self.password = password

def authorization(self,connection):

    try:
        with connection.cursor() as cursor:
            show_all = "SELECT login, password FROM `users`"
            cursor.execute(show_all)
            result = cursor.fetchall()

        valid = False
        while not valid:
            author = multpasswordbox('Введіть данні для авторизації', 'authorizaton', ['Login', 'Password'])
            for i in result:

                if author[0].lower == i.get('login') and author[1].lower == i.get('password'):
                    msgbox('Авторизація успішна')
                    self.login = author[0].lower       #Для того щоб брати цю інфу в файлі func
                    self.password = author[1].lower
                    valid = True

                else:
                    msgbox("Авторизація не успішна, спробуйте ще.")
                    valid = False
                    return True

    finally:
        return True

def registration(self,connection):

    try:
        with connection.cursor() as cursor:
            show_all = 'SELECT login FROM `users`'
            cursor.execute(show_all)
            result = cursor.fetchall()
        valid = False
        while not valid:
            info = multpasswordbox('Введіть данні для реєстрації', 'registration', ['Name','Login', 'Password'])
            for e in result:

                if info[1] == e.get('login'):
                    msgbox('Такий логін вже існує вигадайте інший.')
                    valid = False
                    continue

                else:
                    self.login = info[1].lower
                    self.password = info[2].lower
                    with connection.cursor() as cursor:
                        f"INSERT `users` (name, login, password) values ({info[0].lower},{info[1].lower},{info[2].lower}):
                        connection.commit()
                        valid = True
                        return True

    finally:
        return True

