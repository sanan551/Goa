list1 = ['car','home','school','audi','mercedes','bike','codding','programing','case','python']
list2 = ['bmw','wolksvagen','bus','bike','pc','police','hospital','university','college','gray']
list3 = ['pc','phone','samsung','xiaomi','discord','footbal','messi','ronaldo','neymar','arsenal']
list4 = ['door','color','border','html','css','java','javascript','unity','unreal engine','pencil']
         #  -10      -9   -8         -7       -6         -5      -4       -3       -2          -1
            #  0         1    2          3         4         5       6       7        8           9


print(list1[0:4])


for item in list2[3:8]:
    print(item)

print(list3[-4:])

index = 0

while index < len(list4):
    print(list4[index])
    index += 1
