#Open and read file
f = open("Day2\\input.txt", "r")
sum = 0

for i in f:
    list_of_reports = i.strip().split(" ")
    add_to_safe_list = False
    print(f"start {str(list_of_reports)}")

    for x in range(0,len(list_of_reports)-1):
        print(f'list_of_reports[x] is: {list_of_reports[x]} and list_of_reports[int(x)+1] is: {list_of_reports[int(x)+1]}')
        
        #Adding check
        diff = abs((int(list_of_reports[int(x)])-int(list_of_reports[int(x)+1]))) #< 3 or abs(int(list_of_reports[int(x)])-int(list_of_reports[int(x)+1])) > 0):
        if diff > 0 and diff < 4:
            add_to_safe_list = True
            print(f'Diff is: {abs((int(list_of_reports[x])-int(list_of_reports[int(x)+1])))}')
        else: 
            add_to_safe_list = False
            break
    
    if add_to_safe_list == True:
        print("Add check is true, checking order...")
        #Ascending check
        #print(all(list_of_reports[int(i)] <= list_of_reports[i + 1]))
        print(i.strip())
        print(f'list is ascending = {i == sorted(i)}')
        add_to_safe_list = i == sorted(i)
#        if all(list_of_reports[i] <= list_of_reports[i + 1] for i in range(len(list_of_reports) - 1)) == True:
#            print(f'list is ascending')
#            add_to_safe_list = True
#        else: add_to_safe_list = False
        
        #descending check
        if add_to_safe_list == False: #and all(list_of_reports[i] >= list_of_reports[i + 1] for i in range(len(list_of_reports) - 1)) == True:
            add_to_safe_list = i == sorted(i, reverse=True)
            print(f'list is descending = {i == sorted(i, reverse=True)}')
  
    
    if add_to_safe_list == True:
        print("True " + str(list_of_reports))
        sum = sum + 1
    else:
        print("Fasle " + str(list_of_reports))


print(f'The sum for the first task is: {sum}')

#221 is too low
#530 is too high
