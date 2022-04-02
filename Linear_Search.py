pos=-1
def linearsearch(list,n):
    for i in range(len(list)):
        if n==list[i]:
           global pos
           pos=i
           return True
        
    
    else:
         return False
list=[1,2,3,4,5]
n=3
if linearsearch(list,n):
    print(f"Element found at {pos}")

else:
    print("Element not found")
