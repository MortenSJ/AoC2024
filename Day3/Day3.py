import re

#Open and read file
f = open("Day3\\input.txt", "r")
sum = 0

muls = []

for i in f: 
    mul3 = re.findall("mul\(.{1,4},.{1,4}\)", i)
    
    for m in mul3:
        muls.append(m)

for x in muls:
    x = str(x).replace("mul(","").replace(")","").replace("[","").replace("]","").replace("'","")

    if x != '':
        first_val = int(x.split(",")[0])
        sec_val = int(x.split(",")[1])
        multiply = first_val*sec_val

    sum = sum + multiply

print(f'The sum for the first task is: {sum}')

#Task two!!
#start_pos = muls[0]
sum=0
muls2 = []

f = open("Day3\\input.txt", "r")

for o in f: 
    print("Finding mul...")
    mul = re.findall("do\(\).{0,2}mul\(.{1,4},.{1,4}\)", o)
    
    print(f'Mul is {mul}')
    for n in mul:
        muls2.append(n)

for c in muls2:
    c = str(x).replace("mul(","").replace(")","").replace("[","").replace("]","").replace("'","")

    if c != '':
        first_val = int(x.split(",")[0])
        sec_val = int(x.split(",")[1])
        multiply = first_val*sec_val

    sum = sum + multiply

#sum = sum + start_pos
print(f'The sum for the sec task is: {sum}')

#1624642 too low