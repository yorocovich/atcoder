l1, r1, l2, r2 = map(int,input().split())
if(l1>l2):
    l1,r1,l2,r2=l2,r2,l1,r1
if(r1<=l2):
    print(0)
elif(r1<=r2):
    print(r1-l2)
else:
    print(r2-l2)
