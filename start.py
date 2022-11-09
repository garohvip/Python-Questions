import pymysql

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
    with connection.cursor() as cursor:
        cursor.execute("""SHOW TABLES FROM `musei` LIKE 'users';""")
        check = cursor.fetchone()
        if check:
            pass
        else:
            create_table = "CREATE TABLE `users` (idUser INT AUTO_INCREMENT, name varchar(30), login varchar(30) UNIQUE, password varchar(30), PRIMARY KEY (idUser));"
            cursor.execute(create_table)
            create_table = "CREATE TABLE `exhibit` (idEx INT AUTO_INCREMENT, nameExhibit varchar(30) UNIQUE, year INT, criterion ENUM ('до нашей эры', 'наша эра'), description varchar(255), PRIMARY KEY (idEx));"
            cursor.execute(create_table)
            create_table = "CREATE TABLE `userex` (idPer INT AUTO_INCREMENT, loginPerson varchar(30), " \
                           "nameExhibit varchar(30), PRIMARY KEY (idPer), " \
                           "FOREIGN KEY (nameExhibit) REFERENCES exhibit(nameExhibit), " \
                           "FOREIGN KEY (loginPerson) REFERENCES users(login));"
            cursor.execute(create_table)

except Exception as ex:
    print(ex)