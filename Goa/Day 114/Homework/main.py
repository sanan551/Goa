def manual_index(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1  

my_list = [10, 20, 30, 40]
print(manual_index(my_list, 30))  
print(manual_index(my_list, 50))  
