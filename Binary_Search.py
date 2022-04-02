pos=-1
def search(list,n):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        if list[mid]==n:
            global pos
            pos=mid
            return True
        elif list[mid]<n:
            low=mid+1
        else:
            high=mid-1

list=[1,2,3,4,5,6,7,8,9]
n=6
if search(list,n):
    print(f"Element found at {pos+1}")
else:
    print("Element not found")