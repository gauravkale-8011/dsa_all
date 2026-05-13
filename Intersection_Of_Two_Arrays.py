arr1= [4,9,5]
arr2=[9,4,9,8,4]
seen1=set()
seen2=set()
seen3=set()
list=[]
for i in arr1:
    if i not in seen1:
        seen1.add(i)
for j in arr2:
    if j not in seen2:
       seen2.add(j)
for k in seen1:
    seen3.add(k)
for l in seen2:
    if l in seen3:
        list.append(l)
print(list)


### class Solution:
###    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
###       return list(set(nums1) & set(nums2))