def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        midle = (low + high)
        guess = list[midle]
        if guess == item:
            return midle
        if guess > item:
            high = midle - 1
        else:
            low = midle + 1
    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(my_list, 4))
