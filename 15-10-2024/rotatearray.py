nums=[1,2,3,4,5,6,7]
k=3
arr=[]
length=len(nums)
diff=length-k
arr=nums[diff:]+nums[:diff]
print("The rotated array is:",arr)