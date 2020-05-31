cpdomains=["9001 discuss.leetcode.com"]
def helper(cpdomains):
    ans=[]
    hmap={}
    for i in cpdomains:
        count,domin=i.split()
        add=domin.split(".")
        for j in range(len(add)):
            key=".".join(add[j:])
            if key not in hmap:
                hmap[key]=int(count)
            else:
                hmap[key]+=int(count)
    for k,v in hmap.items():
        ans.append((str(v)+" "+k))
    return ans
print(helper(cpdomains))

