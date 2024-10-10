list1=[9,2,3,10]
for i in range(len(list1)-1):
    for j in range(len(list1)-1-i):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print("sorted list:",list1)
    

    