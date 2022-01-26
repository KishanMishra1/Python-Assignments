#lex_auth_01269442760027340879
def factors(num):
    res=[]
    for i in range(1,num+1):
        if num%i==0:
            res.append(i)
    return res

def find_smallest_number(num):
    i=int(1)
    while(True):
        x=factors(i)
        if(len(x)==num):
            print(x)
            break
        else:
            i=i+int(1)
    return x[-1]
    
num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
