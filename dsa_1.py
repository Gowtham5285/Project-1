a=[1,2,3,4]
cary=1
for i in range(len(a)-1,-1,-1):
    if a[i]+cary==10:
        a[i]=0
        cary=1
    else:
        a[i]+=cary
        cary=0
if cary==1:
    a=[cary]+a
print(a)