string1="anagram"
string2="nargama"
hash_table1=[0]*26
hash_table2=[0]*26
for i in string1:
    hash_table1[ord(i)-ord("a")]+=1
for j in string2:
    hash_table2[ord(j)-ord("a")]+=1
if(hash_table1==hash_table2):
    print("True")
else:
    print("False")