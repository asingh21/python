def get_gcd(num1, num2):
    while num1 % num2 != 0:
        temp = num1
        num1 = num2
        num2 = temp % num2
        print "num1 = {} and nume = {}".format(num1, num2)
    print "gcd = {}".format(num2)

get_gcd(45,10)
