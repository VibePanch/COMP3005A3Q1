import psycopg2
import datetime
import getpass


'''
Note: It is possible to override the entering of username, password, etc. information by commenting out lines 26 to 29 of the code, and instead using the static variables that are defined here.
'''
host = "localHost"
port = 5432
user = "postgres"
password = ""


'''
Function: main()
Use: Calls all other functions (getAllStudents, etc.), and allows user to enter and exit application
Parameters: None to instantiate
Output: Dependent on which function is called
'''
def main():
    # cursor and connection made global to make it more simple to access from other functions (rather than passing in an extra parameter each time)
    global cursor
    global connection
    #prompt user for information related to postgres
    user = str(input("Enter your postgres username: "))
    password = str(getpass.getpass("Enter your postgres password: "))
    host = str(input("Enter your postgres host information: "))
    port = int(input("Enter your postgres port: "))

    #try to establish connection, catch the error if the connection fails
    try:
        connection = psycopg2.connect(
            dbname = "Student_Management", 
            user = user, 
            password= password, 
            host = host, 
            port = port
        )
    except psycopg2.OperationalError as e:
        print("Error: ", e)
        return

    #establish cursor, which allows for direct interaction with postgres
    cursor = connection.cursor()

    #Main loop for user interaction
    while True:
        answer = input("\nChoose your database operation: \n" \
        "1: getAllStudents() \n" \
        "2: addStudent(first_name, last_name, email, enrollment_date) \n" \
        "3: updateStudentEmail(student_id, email) \n" \
        "4: deleteStudent(student_id) \n" \
        "5: exit \n")

        #Cases for the result
        match answer:
            case "1":
                try:
                    getAllStudents()
                except psycopg2.Error as e:
                    print("Error: Failed to get students!", e)
            
            case "2":
                info = input("Enter the student's first name, last name, email, and enrollment date (Year-month-day format, with dashes) separated by commas: ")
                info = info.split(",")
                try:
                    addStudent(info[0].strip(), info[1].strip(), info[2].strip(), info[3].strip())
                except psycopg2.Error as e:
                    print("Error: failed to add student \n", e)
                print("Student successfully added! \n")
            
            case "3":
                new_info = input("Enter the student's id and new email, separated by commas: ")
                new_info = new_info.split(",")
                try:
                    updateStudentEmail(new_info[0], new_info[1])
                except psycopg2.Error as e:
                    print("Error: failed to update student email \n", e)
                print("Student email successfully updated! \n")

            case "4":
                deletion_info = int(input("Enter the student id of the student you would like to remove: "))
                try:
                    deleteStudent(deletion_info)
                except psycopg2.Error as e:
                    print("Error: failed to delete student \n", e)
                    break
                print("Students successfully deleted! \n")

            case "5":
                connection.close()
                return

                
                
'''
Function: getAllStudents()
Use: Used to prompt postgres to get all students from the student table. 
Parameters: None required to instantiate
Output: Prints all students from the student table (specifically ID, First Name, Last Name, Email, and Enrollment date) into the terminal
'''                

def getAllStudents():
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM students")
    except psycopg2.Error as e:
        print("Error occurred: "+e)
        return
    print("Student ID: ", "First Name: ", "Last Name: ", "Email: ", "Enrollment Date: ")
    for item in cursor.fetchall():
        print(item[0], item[1], item[2], item[3], item[4])
    return cursor.fetchall()



'''
Function: addStudent(first_name, last_name, email, enrollment_date)
Use: Used to add a new student to the student table
Parameters: User is prompted for student's first name, last name, email, and the enrollment date
Output: Adds the student to the table, and returns True if the add is successful, and False if not
'''
def addStudent(first_name, last_name, email, enrollment_date):
    # Enrollment date converted from a string to a datetime object
    enrollment_date = (datetime.datetime.strptime(enrollment_date, "%Y-%m-%d"))

    try:
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES(%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
        connection.commit()
        return True
    except psycopg2.Error as e:
        print("Error occurred: ", e)
        return False
    
'''
Function: updateStudentEmail(student_id, new_email)
Use: Used to update the email of an existing student within the student table
Parameters: User is prompted for the student id and the new email of the student
Output: Returns True if the email is successfully updated, and False if not
'''
def updateStudentEmail(student_id, new_email):
    try:
        cursor.execute("UPDATE students SET email = (%s) WHERE student_id = (%s)", (new_email, student_id))
        connection.commit()
        return True
    except psycopg2.Error as e:
        connection.rollback()
        print("Error occurred: ", e)
        return False


'''
Function: deleteStudent(student_id)
Use: Used to delete a student in the table with the given student iD
Parameters: User is prompted for the student id of the student they would like to delete
OUtput: Returns True if the student is successfully deleted, and False if not
'''
def deleteStudent(student_id):
    try:
        cursor.execute(f"DELETE from students WHERE student_id = {student_id}")
        connection.commit()
        return True
    except psycopg2.Error as e:
        print("Error Occurred: ", e)
        return False

    

main()