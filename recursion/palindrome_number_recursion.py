test_num = 134

def is_palindrome(num, temp):
    if num == 0:
        return temp
    temp = (temp * 10) + (num % 10)
    return is_palindrome(num/10, temp)

def main():
    temp = 0
    returned_num = is_palindrome(test_num, temp)
    if returned_num == test_num:
        print "yes"
    else:
        print "no"

if __name__ == "__main__":
    main()
