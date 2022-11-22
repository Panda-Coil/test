my_list = [1, 2, 3]

def double(list):
    new_list = [item * 2 for item in list]
    return new_list

    #for x in my_list:
    #new_list.append(x * 2)

print(double(my_list))