'''Given two numbers, write a python function which returns true if first number is a seed of second number. Otherwise it returns false.

A number X is said to be a seed of number Y, if multiplying X by its each digit equates to Y

For example, 123 is a seed of 738 as 123*1*2*3 = 738.'''


# lex_auth_0127135857243832321154

def seed_no(number, ref_no):
    mul=number
    while(number!=0):
        ld=number%10
        mul*=ld
        number//=10
    if mul==ref_no:
        return True
    return False


# start writing your code here

number = 45
ref_no = 1000
print(seed_no(number, ref_no))
