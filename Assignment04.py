# ------------------------------------------------------------------------------------------ #
# Title: Assignment04
# Desc: This assignment demonstrates using data collections and using files
# Change Log: 
#   Walden Marcus, 2/16/25, Created Program
#   Walden Marcus 2/19/25, Realized What Was Wrong With Program And Painstakingly Fixed It
# ------------------------------------------------------------------------------------------ #

#Name Constants
MENU:str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
FILE_NAME:str = "Enrollments.csv"

#Name Variables
student_first_name:str = ''
student_last_name:str = ''
course_name:str = ''
csv_data:str = ''
file = None
menu_choice:str = ''
student_data:list = []
students:list = []

#Add File Contents to Students
file = open(FILE_NAME, 'r')
for rows in file.readlines():
    student_data = rows.split(',')
    student_data = [student_data[0],student_data[1],student_data[2].strip()]
    students.append(student_data)
file.close()

#Begin Loop
while True:
    print(MENU)
    menu_choice = input("\nPlease select: ")

    #User Input
    if menu_choice == "1":
        student_first_name = input("What is the student's first name? ")
        student_last_name = input("What is the student's last name? ")
        course_name = input("What is the course name? ")
    #Create a Table from Input
        student_data = [student_first_name, student_last_name, course_name]
        students.append(student_data)
        continue

    #Present Data
    elif menu_choice == "2":
        print("\nThe data you have entered is: ")
        for student in students:
            print(f'{student[0:]}\n')
        continue

    #Process Table to File
    elif menu_choice == "3":
        file = open(FILE_NAME, 'w')
        for student in students:
            csv_data = f'{student[0]},{student[1]},{student[2]}\n'
            file.write(csv_data)
        file.close()
    #Read All Lines of File
        file = open(FILE_NAME, 'r')
        print("\nYou have saved:\n-------------")
        for each in file.readlines():
            print(each)

    #Exit Program
    elif menu_choice == "4":
        print("Exiting program...")
        break

    #If Non-Option is Entered
    else:
        print("That was not an option.")
        continue

