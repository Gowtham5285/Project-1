nums1=[1,2,3,4,5]
nums2=[6,7,8,9]
m=len(nums1)
n=len(nums2)
i=0
j=0
res=[]
while(i<m and j<n):
    if(nums1[i]<nums2[j]):
            res.append(nums1[i])
            i+=1
    elif(nums2[j]<nums1[i]):
            res.append(nums2[j])
            j+=1
    else:
            res.append(nums1[i])
            res.append(nums2[j])
            i+=1
            j+=1
while i<m:
    res.append(nums1[i])
    i+=1
while j<n:
    res.append(nums2[j])
    j+=1
print(res)