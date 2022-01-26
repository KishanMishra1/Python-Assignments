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

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
