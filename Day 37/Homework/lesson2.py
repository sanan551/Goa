def numbers(list):
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
    return min

my_list = [2,5,4,8,0]

result = numbers(my_list)

print(result)

