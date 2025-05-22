students = []

for i in range(3):
    name = input("სახელი: ")
    s1 = float(input("ქულა 1: "))
    s2 = float(input("ქულა 2: "))
    s3 = float(input("ქულა 3: "))
    avg = (s1 + s2 + s3) / 3
    students.append([name, avg])

for name, avg in students:
    print(f"{name}: {avg}")
