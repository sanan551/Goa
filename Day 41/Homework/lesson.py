product_list = ['lays','water','sprite','cola','fanta','doritos','milk','oil','salt','bread',
                'egg','phone','iphone','samsung','sausage','cheese','chicken','suger','candys',
                'cucumber','tomate','alpen gold','soap']

def vending_machine(index1):
    print(product_list[index1])
    

print('''lays (0)1lari, water (1)0.50lari, sprite (2)2lari, cola (3)3lari ,fanta (4)3lari ,doritos (5)2lari ,milk (6)7lari ,oil (7)10lari ,salt (8) 5lari ,bread (9)1.20lari,
                egg (10) 7lari ,iphone (12) 1500lari, samsung (13)1700lari ,sausage (14) 7lari ,cheese (15) 14lari ,chicken (16) 12lari ,suger (17) 9lari ,candys (18)25lari,
                cucumber (19) 2lari ,tomate (20) 3lari ,alpen gold (21) 7lari ,soap (22)15lari ''')

user_choice = int(input('Choose Product By Index: '))


vending_machine(user_choice)