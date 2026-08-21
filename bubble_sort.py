arr=[5,4,3,2,4]
n=len(arr)
for i in range(0,n):
    for j in range(0,n-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
    n=n-1
print(arr)