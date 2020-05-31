lst=[1,1,2]
def helper(lst):
    res=[]
    used=[False]*len(lst)
    path=[None]*len(lst)
    def dfs(curpos,startpos,path,used,lst):
        if curpos==len(path):
            res.append(path[::])
            return
        for i in range(startpos,len(path)):
            if not used[i]:
                used[i]=True
                path[i]=lst[curpos]
                if curpos+1<len(path) and lst[curpos]==lst[curpos+1]:
                    dfs(curpos+1,i+1,path,used,lst)
                else:
                    dfs(curpos + 1, 0, path, used, lst)
                used[i]=False
    dfs(0,0,path,used,lst)
    return res
print(helper(lst))