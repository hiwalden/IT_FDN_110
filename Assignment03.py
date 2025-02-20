# ------------------------------------------------------------------------------------------ #
# Title: Assignment03
# Desc: This assignment demonstrates using conditional logic and looping
# Change Log: 
#   Walden Marcus, 2/7/25, Created Program
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU:str = ("\n----Course Registration Program----\
            \nSelect from the following menu:\
            \n1. Register a Student for a Course\
            \n2. Show current data\
            \n3. Save data to file\
            \n4. Exit the program\n")
FILE_NAME:str = "Enrollments.csv"

# Define the Data Variables
student_first_name:str = ' '
student_last_name:str = ' '
course_name:str = ' '
csv_data:str = ' '
file_obj = None
menu_choice:str = ' '

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("Select your option: ")

    # Input user data
    if menu_choice == "1":
        student_last_name = input("What is the student's last name? ")
        student_first_name = input("What is the student's first name? ")
        course_name = input("What is the name of the course? ")
        continue

    # Present the current data
    elif menu_choice == "2":
        csv_data = f"{student_last_name},{student_first_name},{course_name}\n"
        print(csv_data)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        print("Recording data...")
        file_obj = open(FILE_NAME, "a")
        file_obj.write(csv_data)
        file_obj.close()
        print("Data recorded: " + csv_data)
        continue

    # Stop the loop
    elif menu_choice == "4":
        print("You have chosen to exit. Goodbye! ")
        break

    #Invalid entry
    else:
        print("You have not entered a valid option. Please try again.\n")
        continue 
        