arr=[9, -3, 3, -1, 6, -5]
k=0
maxi=0
left=0
right=0
sum1=0
while(right<len(arr) and left <len(arr)):
    sum1=sum1+arr[right]
    if(sum1==k):
        if( maxi < (right-left+1)):
            maxi=right-left+1
    while(sum1>k):
        sum1=sum1-arr[left]
        left+=1
    right+=1
print(maxi)