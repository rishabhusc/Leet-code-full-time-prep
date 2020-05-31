lst=[10,9,2,5,3,7,101,18]
def helper(lst):
    if len(lst)==1:
        return 1
    if len(lst)==0:
        return 0
    dp=[1]*len(lst)
    for i in range(1,len(lst)):
        for j in range(0,i):
            if lst[j]<lst[i]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)
print(helper(lst))