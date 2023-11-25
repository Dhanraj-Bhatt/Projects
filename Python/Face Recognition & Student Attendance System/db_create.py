import mysql.connector

def create_db():
    con = mysql.connector.connect(host="localhost",username="root",password="root",database=r'face_recognition')
    my_cursor=con.cursor()

    my_cursor.execute("CREATE TABLE IF NOT EXISTS  `csv_data` (`id` int NOT NULL AUTO_INCREMENT,`Name` varchar(255) DEFAULT NULL,`Enroll` varchar(255) DEFAULT NULL,`Date` varchar(255) DEFAULT NULL,`Time` varchar(255) DEFAULT NULL,`Attendace` varchar(255) DEFAULT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;")
    con.commit()

    my_cursor.execute("CREATE TABLE IF NOT EXISTS student (Student_ID INTEGER PRIMARY KEY NOT NULL,Name varchar(45),Roll_No varchar(15),Division varchar(45),Semester varchar(45),Department varchar(45),Year varchar(45),Gender varchar(45),DOB varchar(45),Mobile_No varchar(45),Address varchar(45),Email varchar(45),PhotoSample varchar(45)")
    con.commit()

create_db()

