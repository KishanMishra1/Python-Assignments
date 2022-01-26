'''Write a python program to validate the details provided by a user as part of registering to a web application.

Write a function validate_name(name) to validate the user name
    Name should not be empty, name should not exceed 15 characters
    Name should contain only alphabets

Write a function validate_phone_no(phoneno) to validate the phone number
    Phone number should have 10 digits
    Phone number should not have any characters or special characters
    All the digits of the phone number should not be same.
    Example: 9999999999 is not a valid phone number

Write a function validate_email_id(email_id) to validate email Id
    It should contain one '@' character and '.com'
    '.com' should be present at the end of the email id.
    Domain name should be either 'gmail', 'yahoo' or 'hotmail'
Note: Consider the format of email id to be username@domain_name.com

All the functions should return true if the corresponding value is valid. Otherwise, it should return false.

Write a function validate_all(name,phone_no,email_id) which should invoke appropriate functions to validate the arguments passed to it and display appropriate message. Refer the comments provided in the code.

Note: You may use str.isalpha(), str.isdigit() methods to check whether a string contains alphabets or digits alone.'''

#lex_auth_012694465248329728100

def validate_name(name):
    if 0<len(name)<=15 and name.isalpha():
        return True
    else:
        return False
    #Start writing your code here

def validate_phone_no(phno):
    if 0<len(str(phno))==10 and str(phno).isdigit():
        k=str(phno)[0]
        if str(phno).count(k)==len(str(phno)):
            return False
        return True
    return False

def validate_email_id(email_id):
    if email_id.count('@')==1:
        username,domain=email_id.split("@")
        if username.isalnum() and username.count('@')==0 and username.count(".")==0:
            dom=domain.split(".")
            doma=['gmail','yahoo','hotmail']
            if dom[0] in doma and dom[1]=="com":
                return True
            else:
                return False
            return True
        return False
    return False
def validate_all(name,phone_no,email_id):
    #Start writing your code here
    c=0
    if validate_name(name):
        c+=1
    else:
        print("Invalid Name")
    if validate_phone_no(phone_no):
        c+=1
    else:
        print("Invalid phone number")
    if validate_email_id(email_id):
        c+=1
    else:
        print("Invalid email id")
    if c==3:
        print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tom@sfdgg.com")

