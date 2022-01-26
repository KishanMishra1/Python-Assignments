'''Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number.'''


#lex_auth_01269443664174284882
def palindrome(number):
    return str(number)==str(number)[::-1]
def nearest_palindrome(number):
    n=number+1
    while not palindrome(n):
        n=int(n)+1
    return n

number=12331
print(nearest_palindrome(number))
