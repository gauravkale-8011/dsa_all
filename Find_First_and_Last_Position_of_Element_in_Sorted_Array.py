arr=[5,7,7,8,8,10]
left=0
right=len(arr)-1
target=8
ans=[-1,-1]
while(left <= right):
    mid=(left+right) //2
    if(arr[mid]== target):
        if(target > arr[left]):
            left=left+1
        elif(target < arr[right]):
            right=right-1
        elif(target==arr[left] and target==arr[right]):
            ans=[left,right]
            break
    elif(arr[mid]<target):
        left=mid+1
    elif(arr[mid] > target):
        right=mid-1
print(ans)