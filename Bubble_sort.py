

my_list_soln = [1,2,3,4,8,10]

def bubble_sort(my_list):
    print ("Hello There!!")
    for i in range(len(my_list)):
        print ("Outer Loop started.. Whooa!! i is: ",i)#This will always shows you the value of outer loop.
        for j in range(len(my_list)-1,i,-1):
            print ("Inner loop also started.. Whooa!!, j is now: ",j)#This will always shows you the value of inner loop.
            if my_list[j] < my_list[j-1]:
                my_list[j],my_list[j-1] = my_list[j-1],my_list[j]


    return (my_list)

soln = bubble_sort(my_list_soln)
print(soln)


