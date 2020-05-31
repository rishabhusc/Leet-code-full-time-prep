lst=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
def helper(lst):
    if not lst:return 0
    n,m,count=len(lst),len(lst[0]),0
    def dfs(i,j):
        if i<0 or i>=n or j<0 or j>=m or lst[i][j]=="0":
            return
        lst[i][j]="0"
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j+1)
        dfs(i,j-1)
    for i in range(n):
        for j in range(m):
            if lst[i][j]=="1":
                count+=1
                dfs(i,j)
    return count
print(helper(lst))
