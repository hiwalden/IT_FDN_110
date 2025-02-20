# ------------------------------------------------------------------------------------------ #
# Title: Assignment01
# Desc: This assignment demonstrates using constants, variables, and print()
# Change Log: (Who, When, What)
#   Walden Marcus, 01/24/25, Created Script
# ------------------------------------------------------------------------------------------ #

#Data
#--- Constants
COURSE_NAME : str = "Python 100"
#--- Variables
student_first_name : str = input("What is your first name? ")
student_last_name : str = input("What is your last name? ")

#Registration Confirmation
#---Written in one line
registration_confirmation_1 : str = "\nHello, " + student_first_name + " " + student_last_name + ". You are registered for " + COURSE_NAME + "."
print(registration_confirmation_1)
#---Using \ for code readability
registration_confirmation_2 : str = "\nHello, " + student_first_name + " "\
    + student_last_name + ". You are registered for " + COURSE_NAME + "."
print(registration_confirmation_2)


      
