lst=[100, 4, 200, 1, 3, 2]
def helper(lst):
    lst=set(lst)
    count=0
    for i in lst:
        if i-1 not in lst:
            y=i+1
            while y in lst:
                y+=1
            count=max(count,y-i)
    return count

print(helper(lst))