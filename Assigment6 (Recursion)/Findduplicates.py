#lex_auth_01269443477535129681

def find_duplicates(list_of_numbers):
    uni=[]
    res=[]
    count=0
    s=set(list_of_numbers)
    for i in s:
        uni.append(i)
    #return uni
    for i in uni:
        for j in list_of_numbers:
            if i==j:
                count+=1
            if count>=2:
                res.append(i)
                break
        count=0
    return res

def find_duplicates2(list_of_numbers):
l=[]
for i in list_of_numbers:
x=list_of_numbers.count(i)
if x>=2:
l.append(i)
l=set(l)
l=list(l)
return l


list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
