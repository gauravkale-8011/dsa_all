string='abcaddef'
hash_table=[0]*(len(string)+1)
for i in string:
    hash_table[ord(i)-ord("a")]+=1
print(hash_table)
print(ord("f"))

