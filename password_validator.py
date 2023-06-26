import string
#Passoword Validator
#Coded by David Cui
#Completed: 6/26/2023

#This project checks if the password passes all of the parameters one desires such as 
    #Capital letters
    #Numbers
    #Length
    #Punctuation points

#Input
inputed_password = input("What is your password: ")

#Check if all of the criterias are met for the password
    #length is greater than 8
    #1 capital letter
    #1 number
def password_criteria_checker():
    pass_length = False
    capital = False
    number = False
    punct = False
    if len(inputed_password) >= 8:
        pass_length = True
    for i in inputed_password:
        if i.isupper():
            capital = True
        if i.isnumeric():
            number = True
        if i in string.punctuation:
            punct = True
    
    if pass_length and capital and number and punct:
        return True
    else:
        return False


if password_criteria_checker():
    print("Your password meets all requirements")
else:
    print("Please reconstruct your password to fit all requirements")
