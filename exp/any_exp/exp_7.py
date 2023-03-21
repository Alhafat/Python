n=[-10,-9,-7,-6,-1,0,1,2,3,3,5,9,10,10]
m=[-8,-8,-4,-3,-2,2,4,5,5,6,6]
# a=n+m
# print(sorted(a))
b=[]
if len(n)>len(m):
    b.extend(n[-(len(n)-len(m)):])
length=len(b)
for i in range(len(n) - length)[::-1]:
    if n[i]==m[i]:
        b.insert(0,n[i])
        b.insert(0, m[i])
    elif n[i]>m[i]:
        b.insert(0, n[i])
        b.insert(0, m[i])
    else:
        b.insert(0, m[i])
        b.insert(0, n[i])
print((b))