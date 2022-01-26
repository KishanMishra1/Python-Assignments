#lex_auth_01269446533799116898

def check_perfect_number(number):
    div=[]
    if number<1:
        return False
    for i in range(1,number+1):
        if number%i==0 and i!=number :
            div.append(i)
    #print(div)
    if sum(div)==number:
        return True
    else:
        return False

def check_perfectno_from_list(no_list):
    res=[]
    for i in range(len(no_list)):
        if check_perfect_number(no_list[i]):
            res.append(no_list[i])
        else:
            pass
    if len(res):
        return res
    return []
    #start writing your code here

perfectno_list=check_perfectno_from_list([18,4,2,1,0])
print(perfectno_list)
