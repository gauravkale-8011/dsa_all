arr=[-1,0,3,5,9,12]
tar=2
left=0
right=len(arr)-1
ans=-1
while(left < right):
    mid = left + (right - left) // 2
    print(mid)
    if(arr[mid] == tar):
        ans=mid
        break
    elif(tar < arr[mid]):
        right=mid
    elif(tar > arr[mid]):
        left=mid


        