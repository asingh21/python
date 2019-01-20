import math
import datetime

def prime_deco(func):
    def inner_deco(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        end = datetime.datetime.now()
        print "Time taken to run = {}".format(end - start)
    return inner_deco

@prime_deco
def if_prime(n):
    if type(n) == str:
        n = int(n)
    assert type(n) == int, "Please pass the input number in either int or str"
    if n == 0 or n == 1 or n < 0:
        return False
    #prime_list = if_prime_helper(n)
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            print "Fail"
            break
    else:
        print "Pass"

def if_prime_helper(n):
    prime_list = []
    for outer_i in range(2, n):
        for inner_i in range(2 ,int(math.sqrt(outer_i)+1)):
            if outer_i % inner_i == 0:
                break
        else:
            prime_list.append(outer_i)
    #print prime_list
    return prime_list

if_prime(99999967)
