# Delete date
def delete_ex(nameExhibit, connection):

    with connection.cursor() as cursor:
        create_table = f"DELETE FROM `exhibit` WHERE nameExhibit = {nameExhibit};"
        cursor.execute(create_table)
        connection.commit()























# import pymysql
#
# try:
#     connection = pymysql.connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         password="sasukeuchiha",
#         database="itstep",
#         cursorclass=pymysql.cursors.DictCursor
# )
#     print("OK")
#     try:
#         # Create table
#         # with connection.cursor() as cursor:
#         #     create_table = "CREATE TABLE `students` (id int AUTO_INCREMENT," \
#         #                     "name varchar(30)," \
#         #                     "password varchar(30), PRIMARY KEY (id));"
#         #     cursor.execute(create_table)
#         #     print("Done")
#
#         # with connection.cursor() as cursor:
#         #     insert = "INSERT INTO `students` (name, password) VALUES ('Roman', '12345')"
#         #     cursor.execute(insert)
#         #     connection.commit()
#
#         # Drop table
#     # with connection.cursor() as cursor:
#     #     create_table = "DROP TABLE `students`"
#     #     cursor.execute(create_table)
#
#     # Delete date
#     #     with connection.cursor() as cursor:
#     #         create_table = "DELETE FROM `students` WHERE id=1;"
#     #         cursor.execute(create_table)
#     #         connection.commit()
#
#     # Update data
#     #     with connection.cursor() as cursor:
#     #         create_table = "UPDATE `students` SET password = 'qwerty' WHERE id = 2"
#     #         cursor.execute(create_table)
#     #         connection.commit()
#
#     # SELECT DATA
#     #     with connection.cursor() as cursor:
#     #         create_table = "SELECT * FROM `students`"
#     #         cursor.execute(create_table)
#     #         result = cursor.fetchall()
#     #         print(result)
#     #         for row in result:
#     #             print(row)
#
#     finally:
#         connection.close()
#
# except:
#     print("Error")