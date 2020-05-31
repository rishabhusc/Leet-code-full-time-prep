paths=["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
import collections
def helper(paths):
    d=collections.defaultdict(list)
    for i in paths:
        lst=i.split(" ")
        l=len(lst)
        if l>1:
            for j in range(1,l):
                charAtIdx=lst[j].index("(")
                charAtIdx1=lst[j].index(")")
                elem=lst[j][charAtIdx+1:charAtIdx1]
                d[elem].append(lst[0]+'/'+lst[j][0:charAtIdx])
    output=[]
    for k,v in d.items():
        if len(v)>1:
            output.append(v)
    return output

print(helper(paths))