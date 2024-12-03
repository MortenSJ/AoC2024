#Open and read file
f = open("Day3\\input.txt", "r")
sum = 0

muls = []

for i in f: 
    mul = str(i).split("mul(")
    mul = str(mul).split(")")
    print(mul)
    muls.append(mul)

for m in muls:
    if str(m).split(,)


print(f'The sum for the first task is: {sum}')