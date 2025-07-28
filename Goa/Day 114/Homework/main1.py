def manual_count(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

my_list = [1, 2, 3, 2, 4, 2]
print(manual_count(my_list, 2))   
print(manual_count(my_list, 5))   
