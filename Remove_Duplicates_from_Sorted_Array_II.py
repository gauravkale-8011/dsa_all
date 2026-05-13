arr=[1,1,2,2,3,3,4,4,8]
left=0
right=len(arr)-1
single_ele=0
first=0
last=len(arr)-1
res=0
if(arr[first]!=arr[first+1]):
        single_ele=arr[first]
        
elif(arr[last]!=arr[last-1]):
        single_ele=arr[last]
        
while(right >= left):
    mid=(left+right) // 2
    if(arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]):
        single_ele=arr[mid]
        break
    elif(arr[mid]==arr[mid-1] and mid%2==0):
            right=mid-1
    elif(arr[mid]==arr[mid+1] and mid%2==0):
            left=mid+1
    elif(arr[mid]==arr[mid-1] and mid%2!=0):
            left=mid+1
    elif(arr[mid]==arr[mid+1] and mid%2!=0):
            right=mid-1
print(single_ele)


    