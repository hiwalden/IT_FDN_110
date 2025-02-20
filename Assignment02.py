# ------------------------------------------------------------------------------------------ #
# Title: Assignment02
# Desc: This assignment demonstrates using constants, variables,
#         operators, formatting, files and calculations
# Change Log: (Who, When, What)
#   Walden Marcus, 1/29/2025, Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
COURSE_NAME:str = "Python 100"
COURSE_PRICE:float = 999.98
STATE_TAX:float = .09
TOTAL_PRICE:float = COURSE_PRICE + COURSE_PRICE * STATE_TAX
FILE_NAME:str = "Enrollments.csv"

# Define the Data Variables
student_first_name:str = ' ' 
student_last_name:str = ' '
csv_data:str = ' '
file_obj:object = None

# Get data from the user
student_first_name:str = input("What is the student's first name? ")
student_last_name:str = input("What is the student's last name? ")

# Present the data to the user
csv_data = f"{student_last_name},{student_first_name},\
{COURSE_NAME},{COURSE_PRICE},{TOTAL_PRICE}\n"
print(csv_data)

# Process the data to a file
file_obj = open(FILE_NAME, "w")
file_obj.write(csv_data)
file_obj.close()
print("Data recorded!")



