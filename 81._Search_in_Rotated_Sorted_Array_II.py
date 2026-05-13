arr=[1,0,1,1,1]
target=0
left=0
right=len(arr)-1
ans=0
while(left <=right):
    mid=(left+right)//2
    if(arr[mid]==target):
        ans=1
        break
    elif(arr[left]==arr[mid]==arr[right]):
        left=left+1
        right=right-1
    elif(arr[left] <= arr[mid]):
        if(arr[left] <= target <= arr[mid]):
            right=mid-1
        else:
            left=mid+1
    else:
        if(arr[mid] <= target <= arr[right]):
            left=mid+1
        else:
            right=mid-1
print(ans)



    