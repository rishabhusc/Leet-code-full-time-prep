lst=[0,1,0,2,1,0,1,3,2,1,2,1]
def helper(lst):
    leftmax=0
    righmax=0
    left=0
    right=len(lst)-1
    total=0
    while left<right:
        if lst[left]<lst[right]:
            leftmax=max(leftmax,lst[left])
            total+=leftmax-lst[left]
            left+=1
        else:
            righmax=max(righmax,lst[right])
            total+=righmax-lst[right]
            right-=1
    return total
print(helper(lst))
