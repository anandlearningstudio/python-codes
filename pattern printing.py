
n = int(input("Enter the starting number: "))
m = int(input("Enter the number of rows: "))


for i in range(0, m, 1):
    for j in range(0,i+1,1):
        print n,
    n += 1
    print("\n")
for i in range(m,0,-1):
    for j in range(0, i , 1):
        print n-1,
    print("\n")
    n -= 1

