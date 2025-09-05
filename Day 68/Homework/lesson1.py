def append_items(lst, items):
    for item in items:
        lst.append(item)
    return lst

my_list = [1, 2, 3]
new_items = [4, 5, 6]
result = append_items(my_list, new_items)
print(result)  
