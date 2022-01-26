# lex_auth_01269442545042227276
def find_ten_substring(num_str):
    m = []
    ans=[]
    for i in range(0, len(num_str)):
        for j in range(i, len(num_str)):
            m.append(num_str[i:j + 1]) #subarray
    #return m
    for i in  set(m):
        s=0
        for j in range(0,len(i)):
            s=s+int(i[j])
            #print(s)
            if s==10 and j+1==len(i):
                ans.append(i)
    return ans



        #
    # Remove pass and write your logic here


num_str = '3523014'
print("The number is:", num_str)
#['5230', '23014', '523', '352']
result_list = find_ten_substring(num_str)
print(result_list)
