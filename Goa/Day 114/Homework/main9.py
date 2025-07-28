def modify_set(s):
    s.add("apple")     
    s.add("banana")    
    s.add("cherry")    
    s.remove("banana") 

    return s           


my_set = set()
result = modify_set(my_set)
print(result)
