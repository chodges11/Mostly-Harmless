#----------------------------------------------------------#
# Title: assignment01.py
# Desc: Script prompts the User to input their first name. After
# receiving User input, this script checks the format of the User entry,
# and then prints out the User's first name.
# Changes Log: (Who, When, What)
# Charles Hodges(chodges11@uw.edu), 2021-July-11, Created File
#----------------------------------------------------------#

# Defines a function to request and accept User input of first name.
def inputName():
    first_name = input("Please enter your first name, here --> ")
    return first_name

# Defines a function to check that the User only entered letters.
def checkNameFormat(first_name):
    while first_name.isalpha() == True:
        return True
    else:
        return False

# Explains User participation expectation.
print("Hello! When prompted, please input your first name.")

# Calls a function which asks the User to enter their name.
user_name = inputName()

# Checks that the entered characters are in an acceptable format.
while checkNameFormat(user_name) == False:
    print("Please enter letters for your name.")
    user_name = inputName()
else:
    # Prints out the User's first name, and capitalizes it, if needed.
    print("Your first name is: ", user_name.title())
