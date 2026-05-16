from collections import defaultdict
list1=["eat","tea","tan","ate","nat","bat"]
dict1=defaultdict(list)
arr=[]
for i in list1:
    sorted_=sorted(i)
    dict1[tuple(sorted_)].append(i)
for i in dict1.values():
    arr.append(i)
print(arr)
