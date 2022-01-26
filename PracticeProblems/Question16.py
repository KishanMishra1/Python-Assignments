# lex_auth_0127136084107673601177

def rotate_list(input_list, n):
    return input_list[-n:]+input_list[:-n]


input_list = [1, 2, 3, 4, 5, 6]
output_list = rotate_list(input_list, 4)
print(output_list)
