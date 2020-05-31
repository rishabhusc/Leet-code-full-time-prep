'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order.
All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
'''
lst=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
def helper(lst):
    grpah={}
    for src,des in lst:
        if src in grpah:
            grpah[src].append(des)
        else:
            grpah[src]=[des]
    for src in grpah.keys():
        grpah[src].sort(reverse=True)
    stack=["JFK"]
    res=[]
    while len(stack)>0:
        elem=stack[-1]
        if elem in grpah and len(grpah[elem])>0:
            stack.append(grpah[elem].pop())
        else:
            res.append(stack.pop())
    return res
    print(grpah)
print(helper(lst))