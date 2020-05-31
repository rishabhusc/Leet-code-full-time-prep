nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
def helper(nums,lower,upper):
    result=[]
    def rangeForm(lower,upper):
        if upper==lower:
            return str(lower)
        else:
            return str(lower)+" -> "+str(upper)
    if not nums or len(nums)==0:
        result.append(rangeForm(lower,upper))
        return result
    if nums[0]>lower:
        result.append(rangeForm(lower,nums[0]-1))
    for i in range(0,len(nums)-1):
        if nums[i]!=nums[i+1] and nums[i+1]>nums[i]+1:
            result.append(rangeForm(nums[i]+1,nums[i+1]-1))
    if nums[len(nums)-1]<upper:
        result.append(rangeForm(nums[len(nums)-1]+1,upper))
    return result
print(helper(nums,lower,upper))



