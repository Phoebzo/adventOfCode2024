import re

text= open("mul.txt", 'r') 

text = text.read()

found_mul = []

pattern = r"mul\(\d{1,3},\d{1,3}\)"
found_mul = re.findall(pattern, text)

print(len(found_mul))

stripped_mul_list = []

for i in found_mul:
    stripped_mul = i.strip("mul(")
    stripped_mul = stripped_mul.strip(")")
    stripped_mul = stripped_mul.split(",")
    stripped_mul_list.append(stripped_mul)

multiplied_list = []
counter = 0
for i in stripped_mul_list:
    multiplication = int(i[0]) * int(i[1])
    multiplied_list.append(multiplication)

    counter += multiplication

print(counter)


