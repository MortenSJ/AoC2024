#Open and read file
f = open("Day2\\input.txt", "r")
sum = 0

for i in f:
    list_of_reports = i.strip().split(" ")
    add_to_safe_list = False
    for x in range(0,len(list_of_reports)-1):

        if abs((int(list_of_reports[x])-int(list_of_reports[int(x)+1])) >3 or abs(int(list_of_reports[x])-int(list_of_reports[int(x)+1])) < 1) and (all(list_of_reports[i] <= list_of_reports[i + 1] for i in range(len(list_of_reports) - 1)) == False or all(list_of_reports[i] >= list_of_reports[i + 1] for i in range(len(list_of_reports) - 1)) ==False):
            add_to_safe_list = False
            #print("false " + str(list_of_reports))   
        else: 
            add_to_safe_list = True

        """For checking ascending order
        if all(list_of_reports[i] <= list_of_reports[i + 1] for i in range(len(list_of_reports) - 1)) == True or all(list_of_reports[i] >= list_of_reports[i + 1] for i in range(len(list_of_reports) - 1)) ==True:
            print(f'List is decending og accending')
        else:
            add_to_safe_list = False"""
        
    if add_to_safe_list == True:
        print("True " + str(list_of_reports))
        sum = sum + 1

print(f'The sum for the first task is: {sum}')