'''
Given a list of 24-hour clock time points in "Hour:Minutes" format
find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1

'''
lst=["23:59","00:00"]
def helper(lst):
    def diff(first,second):
        ah,am=first.split(":")
        bh,bm=second.split(":")
        atotal=int(ah)*60+int(am)
        btotal=int(bh)*60+int(bm)
        return btotal-atotal

    if len(lst)<2:return
    ans=1440
    time=sorted(lst)
    for i in range(1,len(lst)):
        first=time[i-1]
        second=time[i]
        ans=min(ans,diff(first,second))
        if ans==0:return 0
    difvalue=diff(time[-1],time[0])
    difvalue+=1440
    ans=min(ans,difvalue)
    return ans
print(helper(lst))
