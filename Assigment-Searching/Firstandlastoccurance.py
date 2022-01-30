#lex_auth_0127667364335943683412

def last_instance( num_list,  start,  end,  key):
    n=len(num_list)
    if (start <= end):
        mid = start + (end - start) // 2
        if ((mid == n - 1 or key < num_list[mid + 1]) and num_list[mid] == key):
            return mid
        elif (key < num_list[mid]):
            return last_instance(num_list, start, (mid - 1), key)
        else:
            return last_instance(num_list, (mid + 1), end, key)

    return -1

'''
def first(arr, low, high, x, n):
    if (high >= low):
        mid = low + (high - low) // 2
        if ((mid == 0 or x > arr[mid - 1]) and arr[mid] == x):
            return mid
        elif (x > arr[mid]):
            return first(arr, (mid + 1), high, x, n)
        else:
            return first(arr, low, (mid - 1), x, n)

    return -1'''

num_list=[1,1,2,2,3,4,5,5,5,5]
start=0
end=len(num_list)-1
key=5 #Number to be searched
#Pass different values for num_list, start,end and key and test your program
result=last_instance(num_list, start,end,key)

if(result!=-1):
    print("The index position of the last occurrence of the number:",result)
else:
    print("Number not found")
