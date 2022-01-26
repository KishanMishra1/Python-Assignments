#lex_auth_01269446157664256093

def check_prime(n):
    if n==1:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def rotations(num):
    snum = str(num)
    return (int(snum[1:] + snum[0]))


def get_circular_prime_count(limit):
    prime=[]
    for num in range(1,limit):
        if check_prime(num) > 0 and num not in prime:
            #Taking special care for 11
            if num == 11:
                prime.append(num)
            else:
                cprime = [num]
                cnum = num
                for i in range(len(str(num)) - 1):
                    cnum = rotations(cnum)
                    if check_prime(cnum) > 0:
                        cprime.append(cnum)
                if len(cprime) == len(str(num)):
                    prime += cprime
    prime.sort()
    return len(prime)





    #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.

#Provide different values for limit and test your program
print(get_circular_prime_count(100))
#print(rotations(4))
