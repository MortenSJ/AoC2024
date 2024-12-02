#Open and read file
f = open("Day2\\input.txt", "r")
sum = 0

for i in f:
    list_of_reports = i.strip().split(" ")
    #print(list_of_reports)
    for x in range(0,len(list_of_reports)):
        if int(list_of_reports[x])-int(list_of_reports[int(x)+1]) >3 or int(list_of_reports[x])-int(list_of_reports[int(x)+1]) < 1:
            break
        else: sum = sum +1

print(f'The sum for the first task is: {sum}')