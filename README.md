# COMP3005A3Q1
Assignment 3 for COMP3005

## Runtime Instructions
### SQL Database and Table creation
1. Create the Student_Management database and the students table in postgres SQL using the first 2 commands found in "student_table.sql"
2. Populate the students table with the "INSERT INTO" command found in "student_table.sql"

### app.py run instructions
1. Open an environment able to run python scripts
2. Install the psycopg2 package if it is not installed already using the command "pip install psycopg2" in the terminal
3. Run app.py
4. Enter the postgres information required to get the application running 
4a. Note: it is possible to run the application without entering the postgres information directly into the terminal through modification of the script: more information can be found within "app.py"
5. Select which function you would like to run, and enter required information when necessary!

## Functions:
1. getAllStudents()- Returns all students present in the students table
2. addStudent(first_name, last_name, email, enrollment_date)- Adds a student with the information to the students table
3. updateStudentEmail(student_id, new_email)- Updates the email of the student with the given student id present in the students table
4. deleteStudent(student_id)- Deletes the student with the provided student id in the students table

## Video Demonstration
Link to youtube video can be found here: https://youtu.be/FJ8zIz1KrHo