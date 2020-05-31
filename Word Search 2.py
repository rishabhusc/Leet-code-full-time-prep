board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
import collections
class TrieNode:
    def __init__(self):
        self.children=collections.defaultdict(TrieNode)
        self.isChild=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        node=self.root
        for w in word:
            node=node.children[w]
        node.isChild=True

    def search(self,word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isChild



class Solution:


    def helper(self,board,words):

        def dfs(i,j,node,path,res):
            if node.isChild:
                res.append(path)
                node.isChild=False
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return False
            tmp=board[i][j]
            node=node.children.get(tmp)
            if not node:
                return False
            board[i][j]=''
            dfs(i+1, j, node, path+tmp, res)
            dfs(i-1, j, node, path+tmp, res)
            dfs(i, j+1, node, path+tmp, res)
            dfs(i, j-1, node, path+tmp, res)
            board[i][j]=tmp



        trie=Trie()
        node=trie.root


        res=[]

        for w in words:
            trie.insert(w)

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,node,'',res)
        return res
sol=Solution()
print(sol.helper(board,words))
