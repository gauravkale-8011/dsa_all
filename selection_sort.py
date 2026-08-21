arr=[12,43,23,11,54,23,44,10]
for i in range(0,len(arr)-1):
    min=i
    for j in range(i+1,len(arr)):
        if arr[min] > arr[j]:
            min=j
    temp=arr[i]
    arr[i]=arr[min]
    arr[min]=temp
print(arr)