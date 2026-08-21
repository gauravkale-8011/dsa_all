arr=[1, 0, 1, 1, 0, 1]
count=0
maxi=0
for i in arr:
    if (i==1):
        count+=1
    if(i!=1):
        count=0
    if(count>maxi):
        maxi=count
print(maxi)