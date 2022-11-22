list_of_numbers = [1, 8, 9, 4, 6, 2, 11, 0, 13, 5, 15, 7, 10, 14, 12, 3]
print(len(list_of_numbers))

class Sorts():
    def bubble_sort(list):
        print("original list:{list}")
        length = len(list_of_numbers)
    
    
def double(list):
    new_list = [item * 2 for item in list]
    return new_list

    #for x in my_list:
    #new_list.append(x * 2)


print(double(list_of_numbers))

num = Sorts.bubble_sort(list_of_numbers)
print(num)
