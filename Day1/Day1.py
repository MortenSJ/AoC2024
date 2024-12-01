#Open and read file
f = open("Day1\\input.txt", "r")

left_list = []
right_list = []
for i in f:
    split = i.split("   ")
    left_list.append(int(split[0].strip()))
    right_list.append(int(split[1].strip()))

if len(left_list) == len(right_list):
    pass
else: 
    print("Crap!!")
    exit

left_sorted = sorted(left_list, key=None, reverse=False)
right_sorted = sorted(right_list, key=None, reverse=False)

sum = 0
for x in range(0,len(left_list)):
    value = left_sorted[int(x)]-right_sorted[int(x)]
    if value < 0:
        value = value*-1
    sum = sum + value

print(f'The sum for the first task is: {sum}')

#Part two of day1

similarity_score = 0

for i in left_sorted:
    if i in right_sorted:
        count = right_sorted.count(i)
        similarity_score = similarity_score + (i * count)

print(similarity_score)