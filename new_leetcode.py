
a="google"
b="lg"
c=0
# new=""
# for i in range(len(a)):
#     if a[i] in b:
#         new+=a[i]

# for i in range(len(b)):
#     if new[i]==b[i] :
#         print("True")
#     else:
#         print("False")
for i in range(len(b)):
    for j in range(len(a)):
        if b[i]==a[j]:
            long=j
            break
    if long>c:
        c=long
    elif long<c:
        print("False")
    else:
        print("True")
