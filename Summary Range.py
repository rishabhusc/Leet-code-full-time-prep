lst=[0,1,2,4,5,7]
lst1=[0,2,3,4,6,8,9]
def helper(lst):
    lst=set(lst)
    res=[]
    for i in lst:
        if i-1 not in lst:
            y=i+1
            while y in lst:
                y+=1
            if i != y-1:
                res.append((str(i) +"->"+str(y-1)))
            else:
                res.append(str(i))
    return res

print(helper(lst))
print(helper(lst1))
