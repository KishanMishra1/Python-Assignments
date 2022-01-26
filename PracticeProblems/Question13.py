def close_number(num1,num2,num3):
    lis  = [num1, num2, num3]
    lis.sort()
    if lis[1] == lis[0]+1 or lis[1] == lis[2]-1 or lis[1] == lis[0] or lis[1] == lis[2]:
        if lis[1]+2 <= lis[2] or lis[0]+2 <=lis[1]:  
            return True
        else:
            return False
    else:
        return False
