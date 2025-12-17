print("half pyramid pattern of stars")
n = int(input("enter the number of rows: "))
for i in range (1, n+1):
    for i in range(i):
        print("*", end="")
    print()