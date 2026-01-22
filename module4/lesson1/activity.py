list1=['physics','chemistry',1997,2000]

#sizeof the list
print(len(list1))
#accessing an element
print(list1[1])

#sliceing
print(list1[1:3])

#printing all the iteam 
for item in list1:
    print(item)

list2=[3,1,44,2,5,]

#concatenate list1 and list2
list3 =list1+list2
print(list3)

#sorting list2
list2.sort()
print(list2)
