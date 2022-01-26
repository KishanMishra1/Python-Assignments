def exchange_list(number_list):
    n=len(number_list)
    return number_list[n//2:][::-1]+number_list[:n//2]



number_list = [1,2,3,4,5,6,7,8,9,10]
print(exchange_list(number_list))
