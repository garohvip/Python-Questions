import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="sasukeuchiha",
        database="itstep",
        cursorclass=pymysql.cursors.DictCursor
)
    print("Connected to DB")
    try:
        #Create table
        with connection.cursor() as cursor:
            create_table = "CREATE TABLE `people` (id int AUTO_INCREMENT," \
                            "Name varchar(30)," \
                            "Surname varchar(30),"\
                            "City varchar(30)," \
                            "Country varchar(30)," \
                            "Date_of_birth date, PRIMARY KEY (id));"
            cursor.execute(create_table)
            print("Table created")

    finally:
        connection.close()
except:
    print("Error")