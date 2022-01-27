#lex_auth_0127426336682147841449

def check_double(list1,list2):
    res=[]
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]*2 == list2[j]:
                res.append(list1[i])
    return res
#Provide different values for the variables and test your program
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
print(check_double(list1, list2))
