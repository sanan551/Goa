def insert_item(lst, index, item):
    lst.insert(index, item)
    return lst


my_list = [1, 2, 3, 5]
new_list = insert_item(my_list, 3, 4)
print(new_list) 
