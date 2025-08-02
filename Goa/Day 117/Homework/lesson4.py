count = 0  
max_mustache = 20 

while True:
    num = int(input("რამდენი ულვაში დათვალა ზღვის ლომმა? "))

    if num > max_mustache:
        print("ზღვის ლომს მაგდენი ულვაში არ აქვს!")
        break

    
    for i in range(1, num + 1):
        with open(f"ulvashi_{i}.txt", "w") as f:
            f.write(f"ეს არის ულვაში {i}\n")
    
    print(f"{num} ულვაშის ფაილი შეიქმნა!\n")
