from collections import Counter

nums=[0,1,1,1,2,3,3,3]

counts=Counter(nums)
min_count=2
max_count=3
result=[]
for num,count in counts.items():
    if count>=min_count:
        result.extend([num]*min_count)
    elif count==1:
        result.append(num)
    else:
        result=None

underscores_number=len(nums)-len(result)
result.extend(['_']*underscores_number)
print(result)

