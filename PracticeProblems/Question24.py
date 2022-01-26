'''Given two positive integers. Write a python function to return the greatest common divisor of the given numbers'''


def find_gcd(num1, num2):
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(1, small + 1):
        if ((num1 % i == 0) and (num2 % i == 0)):
            gcd = i

    return gcd

def find_gcd(num1, num2):
    if (num2 == 0):
        return num1
    else:
        return find_gcd(num2, num1 % num2)

# start writing your code here


num1 = 800
num2 = 2800
print(find_gcd(num1, num2))
