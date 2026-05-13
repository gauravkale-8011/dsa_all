arr=[1,2,2,3,2,1,4]
hash_table=[0]*(len(arr)+1)
for i in range(0,len(arr)):
    hash_table[arr[i]]+=1
print(hash_table)