list_of_numbers = [1, 8, 9, 4, 6, 2, 11, 0, 13, 5, 15, 7, 10, 14, 12, 3]

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
    
print(linear_search(list_of_numbers, 30))