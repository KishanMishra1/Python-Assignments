'''Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.

The number and its double should have exactly the same number of digits.

Both the numbers should have the same digits ,but in different order.

Otherwise it should return False.

Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.'''


#lex_auth_01269441810970214471

def check_double(number):
    dob=2*number
    ld=0
    count=0
    temp=dob
    n=len(str(number))
    while(dob!=0):
        ld=dob%10
        for i in range(n):
            if str(number)[i]==str(ld):
                count+=1
        dob//=10

    if len(str(temp))==n and count==n:
        return True
    return False



#Provide different values for number and test your program
print(check_double(11))
