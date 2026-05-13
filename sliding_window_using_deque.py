from collections import deque
arr=[1,3,-1,-3,5,3,6,7]
k = 3
dq=deque()
list=[]
for i in range(0,len(arr)):
    while(dq and dq[0] < i-k+1):
        dq.popleft()
    while(dq and arr[dq[-1]] <= arr[i]):
        dq.pop()
    dq.append(i)
    if(i >= k-1):
        list.append(arr[dq[0]])
print(list)


    




