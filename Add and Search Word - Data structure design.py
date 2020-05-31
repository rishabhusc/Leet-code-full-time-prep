class Trie:
    def __init__(self,val):
        self.val=val
        self.children={}
        self.isWord=False
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Trie(None)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        root=self.root
        for w in word:
            if w not in root.children:
                root.children[w]=Trie(w)
            root=root.children[w]
        root.isWord=True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def helper(root,word):
            for i,char in enumerate(word):
                if char not in root.children and char!=".":
                    return False
                if char==".":
                    for elem in root.children:
                        return helper(root.children[elem],word[i+1:])
                else:
                    root=root.children[char]
            return root.isWord
        root=self.root
        return helper(root,word)

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))# -> false
print(obj.search("bad"))# -> true
print(obj.search(".ad"))# -> true
print(obj.search("b.."))# -> true