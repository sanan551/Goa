numbers = list(range(1, 9))


def double(x):
    return x * 2

doubles = list(map(double, numbers))


def is_odd(x):
    return x % 2 != 0

odd = list(filter(is_odd, numbers))


print("original numbers:", numbers)
print("doubles:", doubles)
print("odd numbers:", odd)


def manual_map(func, lst):
    result = []
    for x in lst:
        result.append(func(x))
    return result


def manual_filter(func, lst):
    result = []
    for x in lst:
        if func(x):
            result.append(x)
    return result


manual_doubles = manual_map(double, numbers)
manual_odd = manual_filter(is_odd, numbers)

print(manual_doubles)
print(manual_odd)
