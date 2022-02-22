import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
v = []
while nr_letters > 0:
    n_l = random.randint(0, 25)
    l = letters[n_l]
    f_lp = v.append(l)
    nr_letters-=1
t = []
while nr_numbers > 0:
    n_n = random.randint(0, 10)
    n = numbers[n_n]
    f_np = t.append(n)
    nr_numbers-=1
u = []
while nr_symbols > 0:
    n_s = random.randint(0, 8)
    s = symbols[n_s]
    f_sp = u.append(s)
    nr_symbols-=1

p= v+t+u
length = len(p)
random_pass = random.sample(p,length)

str1 = ""
password = str1.join(p)

str2 = ""
random_password = str2.join(random_pass)

print(f'\n\nOrder not randomised::-  {password}')
print(f'\n\nOrder of characters randomised::-  {random_password}')