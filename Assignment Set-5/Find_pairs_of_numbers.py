def find_pairs_of_numbers(num_list,n):
    count=0
    for i in range(len(num_list)-1):
        for y in range(i+1,len(num_list)):
            if num_list[i]+num_list[y]==n:
                count+=1
    return count
num_list=[1, 2, 7, 4, 5, 6, 0, 3]
n=6
print(find_pairs_of_numbers(num_list,n))
