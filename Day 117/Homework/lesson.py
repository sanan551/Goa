import os

for i in range(1, 11):
    folder_name = f"folder_{i}"
    os.mkdir(folder_name)  

for i in range(1, 11):
    file_name = f"file_{i}.txt"
    with open(file_name, "w") as f:
        f.write(f"ეს არის {file_name}")
