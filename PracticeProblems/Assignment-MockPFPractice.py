def countz(str):
    alp=0
    dig=0
    for i in str:
        if i.isalpha():
            alp+=1
    return alp
def extract(str):
    st=""
    for i in str:
        if i.isalpha():
            st=st+i
    return st
def rotate(str,n):
    str=list(str)
    if n==2:
        return "".join(str[-n:]+str[:-n])
    elif n==1:
        return "".join(str[n:]+str[:(n+1)-1])

def list_rotate(uniquecode_list):
    rotated_list=[]
    counta=0
    for i in uniquecode_list:
        x,y=i.split("-")
        k=extract(x)
        c=countz(x)
        if c==2:
            rotated_list.append(k+rotate(y,c))
        elif c==1:
            rotated_list.append(k+rotate(y,c))
    return rotated_list

#You may modify the below code for testing
uniquecode_list=['G221-1011','S621-9699']
rotated_list = list_rotate(uniquecode_list)
print(rotated_list)
