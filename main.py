list_of_numbers = [1, 8, 9, 4, 6, 2, 11, 0, 13, 5, 15, 7, 10, 14, 12, 3]
print(len(list_of_numbers))

class Sorts():
    def bubble_sort(list):
        print("original list:{list}")
        length = len(list_of_numbers)
    

class RandomShit():
    def double(given_list):
        new_list = [item * 2 for item in given_list]
        return new_list
    
        #for x in my_list:
        #new_list.append(x * 2)
        
    def randprac1(given_list):
        value = 0
        for x in given_list:
            value += x
        return value
    
    def linear_search(given_list, var):
        tries = 0
        for num in given_list:
            if num == var:
                return tries
                break
            else:
                tries += 1
            if tries == len(given_list):
                return False

    


print(RandomShit.double(list_of_numbers))

num = Sorts.bubble_sort(list_of_numbers)
print(num)
