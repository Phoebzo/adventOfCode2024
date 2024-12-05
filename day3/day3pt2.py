import re

text= open("mul.txt", 'r') 

text = text.read()
count = text.count("do()")
counts = text.count("don't()")

do = text.split(sep="do()")
print(count, len(do), counts)

do_and_dont = []

for i in do:

    splitted = i.split(sep="don't()")
    do_and_dont.append(splitted)

found_mul = []

for i in do_and_dont:
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    found_do = re.findall(pattern, i[0])
    found_mul.append(found_do)

print(found_mul)

stripped_mul_list = []

for i in found_mul:
    for j in i:
        stripped_mul = j.strip("mul(")
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

