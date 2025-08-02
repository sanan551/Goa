
with open("delete_me.txt", "w") as f:
    f.write("ეს ფაილი მალე წაიშლება!")


import os
os.remove("delete_me.txt")  
