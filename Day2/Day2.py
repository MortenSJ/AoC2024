#Open and read file
f = open("Day2\\input.txt", "r")
sum = 0

for i in f:
    list_of_reports = i.strip().split(" ")
    add_to_safe_list = False

    for x in range(0,len(list_of_reports)-1):    
        line_direction = (int(list_of_reports[1])-int(list_of_reports[0]))
        
        if int(line_direction) > 0:
            x_direction = "up"
        else: 
            x_direction = "down"

        #check for increasing or decreasing
        if (int(list_of_reports[int(x)+1])-int(list_of_reports[int(x)])) >0:
            direction = "up"
        else: direction = "down"

        #Adding check
        diff = abs((int(list_of_reports[int(x)])-int(list_of_reports[int(x)+1])))
        if diff > 0 and diff < 4 and direction == x_direction:
            add_to_safe_list = True
        else: 
            add_to_safe_list = False
            break

    if add_to_safe_list == True:
        sum = sum + 1
    else: pass

print(f'The sum for the first task is: {sum}')
