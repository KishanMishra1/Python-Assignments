'''Write a Python function which generates and returns a dictionary where the keys are numbers between 1 and n (both inclusive) and the values are square of keys.'''
# lex_auth_0127135904626688001159

def generate_dict(number):
    dic={}
    for i in range(1,number+1):
        dic[i]=i**2

    return dic


number = 20
print(generate_dict(number))
