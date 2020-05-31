word1 = "horse"
word2 = "ros"
def helper(word1,word2):
    n=len(word1)+1
    m=len(word2)+1
    dp=[[0 for j in range(m)]for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif word1[i-1]==word2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
    return dp[-1][-1]
print(helper(word1,word2))