lst=[1,2,3]
def helper(lst):
    res=[]
    used=[False]*len(lst)
    path=[None]*len(lst)
    def dfs(curpos,used,path,lst):
        if curpos==len(path):
            res.append(path[::])
            return
        for i in range(len(path)):
            if not used[i]:
                used[i]=True
                path[i]=lst[curpos]
                dfs(curpos+1,used,path,lst)
                used[i]=False
    dfs(0,used,path,lst)
    return res



print(helper(lst))