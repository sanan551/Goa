def append_lists(list1, list2):
    for item in list2:
        list1.append(item)
    return list1


a = [1, 2, 3]
b = [4, 5, 6]
result = append_lists(a, b)
print(result) 