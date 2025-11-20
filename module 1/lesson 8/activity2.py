x=int(input("enter a numerator: ")) 
y=int(input("enter a denomenator"))
result=x/y
print(result)

if x%y==0:
    print("divisible")
else:
    print("not divisible")