'''Use Luhn algorithm to validate a credit card number.

A credit card number has 16 digits, the last digit being the check digit. A credit card number can be validated using Luhn algorithm as follows:

Step 1a: From the second last digit (inclusive), double the value of every second digit.
Suppose the credit card number is 1456734512345698.
Take the double of 9,5,3,1,4,7,5 and 1
i.e., 18, 10, 6, 2, 8, 14, 10 and 2

Note: If any number is greater than 9, then sum the digits of that number.
i.e., 9, 1, 6, 2, 8, 5 ,1 and 2

Step 1b: Sum the numbers obtained in Step 1a.
i.e., 34

Step 2: Sum the remaining digits in the credit card and add it with the sum from Step 1b.
i.e., 34 + (8+6+4+2+5+3+6+4) = 72

Step 3: If the total is divisible by 10 then the number is valid else it is not valid.

Write a function, validate_credit_card_number(), which accepts a 16 digit credit card number and returns true if it is valid as per Luhn’s algorithm or false, if it is invalid. '''

#lex_auth_01269445968039936095
def sumofd(number):
    n=number
    sum=0
    ld=0
    while(n!=0):
        ld=n%10
        sum+=ld
        n//=10
    return sum

def validate_credit_card_number(card_number):
    res=[]
    ser=[]
    k=0
    n=len(str(card_number))
    for i in range(n):
        if i%2==0:
            res.append(int(str(card_number)[i])*2)
        else:
            ser.append(int(str(card_number)[i]))
    for i in res:
        if i>9:
            k+=sumofd(i)
        else:
            k+=i
    sum2=k+sum(ser)
    #print(sum2)
    if sum2%10==0:
        return True
    return False



card_number=5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
