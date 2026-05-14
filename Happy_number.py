num=19
seen=set()
string=str(num)
seen.add(num)
sum=0
if(num!=1):
    while (sum != 1):
        sum=0
        for i in string:
            sum=sum + int(i) *int(i)
        if sum in seen:
            print("False")
        else:
            seen.add(sum)
            string=str(sum)
    if(sum==1):
        print("True")
else:
    print("True")
