def arrange_eve_odd_list(input_list):
    even_list = []
    odd_list = []
    return_list = []
    for ele in input_list:
        if ele % 2 == 0:
            even_list.append(ele)
        else:
            odd_list.append(ele)
    even_list = even_list[::-1]
    odd_list = odd_list[::-1]
    print even_list
    print odd_list
    for index in range(len(input_list)):
        if not len(even_list):
            return_list += odd_list
            return return_list
        if not len(odd_list):
            return_list += even_list
            return return_list
        if index % 2 == 0:
            return_list.append(even_list[-1])
            even_list.pop()
        else:
            return_list.append(odd_list[-1])
            odd_list.pop()
    return return_list

input_list = [1,2,3,4,5,6]
print arrange_eve_odd_list(input_list)
