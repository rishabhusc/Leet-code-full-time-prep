board=[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCB"

def helper(board,word):
    if not board:return
    n=len(board)
    m=len(board[0])
    def  dfs(i,j,count):
        if count==len(word):return True
        if i<0 or i>=n or j<0 or j>=m or board[i][j]!=word[count]:
            return False
        tmp=board[i][j]
        board[i][j]="."
        found=dfs(i+1,j,count+1) or dfs(i-1,j,count+1) or dfs(i,j+1,count+1) or dfs(i,j-1,count+1)
        board[i][j]=tmp
        return found

    for i in range(n):
        for j in range(m):
            if board[i][j]==word[0] and dfs(i,j,0):
                return True
    return False
print(helper(board,word))