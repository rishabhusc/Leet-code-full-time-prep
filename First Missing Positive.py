lst=[3,4,-1,1]
def helper(lst):
    i=0
    n=len(lst)
    while i<n:
        if lst[i]>0 and lst[i]<=n:
            if lst[i]!=lst[lst[i]-1]:
                tmp=lst[i]
                lst[i]=lst[lst[i]-1]
                lst[tmp-1]=tmp
                i-=1
        i+=1
    for i in range(n):
        if lst[i]!=i+1:
            return i+1
    return n+1
print(helper(lst))


def helper(lst):
    i=0
    n=len(lst)
    while i<n:
        if lst[i]>0 and lst[i]<=n:
            if lst[i]!=lst[lst[i]-1]:
                tmp=lst[i]
                lst[i]=lst[lst[i]-1]
                lst[tmp-1]=tmp
                i-=1
        i+=1
    for i in range(n):
        if lst[i]!=i+1:
            return i+1
    return n+1
print(helper(lst))


