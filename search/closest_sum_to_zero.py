import sys

def closest_sum_to_zero(num):
    num_length = len(num)
    num.sort()
    left = 0
    right = num_length - 1
    min_left = 0
    min_right = num_length - 1
    min_sum = sys.maxint
    while (left < right):
        sum = num[left] + num[right]
        if abs(min_sum) > abs(sum):
            min_lift = left
            min_right = right
            min_sum = sum
        if sum < 0:
            left += 1
        else:
            right -= 1
    return (min_left, min_right)

num = [-1,2,3,4,5]
a,b = closest_sum_to_zero(num)
print (num[a], num[b])
