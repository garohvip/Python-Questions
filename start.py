import pymysql

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
    with connection.cursor() as cursor:
        create_table = "CREATE TABLE `users` (idUser INT AUTO_INCREMENT, name varchar(30), login varchar(30) UNIQUE, password varchar(30), PRIMARY KEY (idUser));"
        cursor.execute(create_table)
        create_table = "CREATE TABLE `exhibit` (idEx INT AUTO_INCREMENT, nameExhibit varchar(30) UNIQUE, year INT, description varchar(30), PRIMARY KEY (idEx));"
        cursor.execute(create_table)
        create_table = "CREATE TABLE `userex` (idPer INT AUTO_INCREMENT, loginPerson varchar(30), " \
                       "nameExhibit varchar(30), PRIMARY KEY (idPer), " \
                       "FOREIGN KEY (nameExhibit) REFERENCES exhibit(nameExhibit), " \
                       "FOREIGN KEY (loginPerson) REFERENCES users(login));"
        cursor.execute(create_table)

except Exception as ex:
    print(ex)