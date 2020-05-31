'''

Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly :
one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1
where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.



Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".

'''

lst=["a","b","ba","bca","bda","bdca"]
def helper(lst):
    d={}
    words=sorted(lst,key = lambda x:(len(x),x))
    for word in words:
        found=False
        for i in range(len(word)):
            search=word[:i]+word[i+1:]
            print(search,d,word)
            if search in d:
                d[word]=max(d.get(word,0),d[search]+1)
                found=True
            if not found:
                d[word]=1
    return max(d.values())
print(helper(lst))