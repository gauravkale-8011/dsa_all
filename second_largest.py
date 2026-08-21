arr=[7,7,6,5,4,3]
max=arr[0]
second_max=0
for i in arr:
    if i > max:
        temp=max
        max=i
        second_max=temp
    elif(i>second_max and i < max):
        second_max=i
print(second_max)