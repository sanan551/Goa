number = int(input("რამდენი ლუდის ბოთლი მოითხოვა ნუგზარმა? "))

for i in range(1, number + 1):
    file_name = f"ludi_{i}.txt"
    with open(file_name, "w") as f:
        f.write(f"ლუდი {i}\n")
