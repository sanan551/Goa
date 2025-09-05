def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # თუ სია ცარიელია, ანიშნება რომ საშუალო არითმეტიკული არ არსებობს
    return sum(numbers) / len(numbers)


numbers = [1, 3, 4, 5, 2]
print(calculate_average(numbers))  # output: 3
