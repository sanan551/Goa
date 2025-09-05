def print_counts(lst):
    seen = []
    for item in lst:
        if item not in seen:
            count = lst.count(item)
            print(f"{item} - {count}")
            seen.append(item)


fruits = ["apple", "banana", "apple", "cherry", "banana", "banana"]
print_counts(fruits)

