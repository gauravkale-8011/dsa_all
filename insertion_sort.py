arr=[12,43,23,54,56,32]
n=len(arr)
for i in range(0,n):
    j=i
    while(j>0 and arr[j]<arr[j-1]):
        arr[j],arr[j-1]=arr[j-1],arr[j]
        j=j-1
print(arr)
