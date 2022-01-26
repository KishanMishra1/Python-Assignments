def create_new_dictionary(prices):
    new_dict={}
    for i,j in prices.items():
        if j >200:
            new_dict[i]=j
    return new_dict
    
prices = { 'MANGO': 150.45,'POMOGRANATE': 250.67, 'BANANA': 20.55,'CHERRY': 500.10,'ORANGE': 200.75}
print(create_new_dictionary(prices))
