import psycopg2
import datetime

host = "localHost"
port = 5432

connection = psycopg2.connect(
        dbname = "Student_Management", 
        user = "postgres", 
        password= "Veeran$05", 
        host = host, 
        port = port
    )

def getAllStudents(connection):
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM students")
    except psycopg2.Error as e:
        print("Error occurred: "+e)
        return


    for item in cursor.fetchall():
        print(item[0], item[1], item[2], item[3], item[4])

    return cursor.fetchall()

def addStudent(first_name, last_name, email, enrollment_date, connection):
    enrollment_date = (datetime.datetime.strptime(enrollment_date, "%Y-%m-%d"))

    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES(%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
        connection.commit()
        return True
    except psycopg2.Error as e:
        print("Error occurred: ", e)
        return False
    

def updateStudentEmail(student_id, new_email, connection):
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE students SET email = (%s) WHERE student_id = (%s)", (new_email, student_id))
        connection.commit()
        return True
    except psycopg2.Error as e:
        connection.rollback()
        print("Error occurred: ", e)
        return False

def deleteStudent(student_id, connection):
    cursor = connection.cursor()
    try:
        cursor.execute(f"DELETE from students WHERE student_id = {student_id}")
        connection.commit()
        return True
    except psycopg2.Error as e:
        print("Error Occurred: ", e)
        return False

    

# print(addStudent("James", "Johnson", "jj@gmail.com", "2023-09-08", connection))
# getAllStudents(connection)
# updateStudentEmail(8, "james@gmail.com", connection)

# deleteStudent(8, connection)
# getAllStudents(connection)

