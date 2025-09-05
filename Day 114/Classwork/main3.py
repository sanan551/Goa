set1 = {1, 2, 3, 4, 5, 5, 6}  
set2 = {4, 5, 6, 7, 8, 8, 9}  

print(set1)
print(set2)


set1.add(10)
set2.add(11)

print(set1)
print(set2)


set1.remove(1)  
set2.remove(7)  

print(set1)
print(set2)


union_result = set1.union(set2)
print(union_result)


intersection_result = set1.intersection(set2)
print(intersection_result)


difference_result = set1.difference(set2)
print(difference_result)
