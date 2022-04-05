def Bubble_sort(list):
    for i in range(0,len(list)-1):
        for j in range(len(list)-1):
            if(list[j]>list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp

    return list

list=[5,7,2,6,9,4,1,5,6]

print("The sorted list is :",Bubble_sort(list))
