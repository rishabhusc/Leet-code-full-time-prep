username = ["uod","uod","uod","kfuagsh","uod"]

timestamp = [520778108,799976888,522803143,968158505,908405336]

website = ["bfx","taohbuuleq","vsryf","irmbcoebt","bfx"]



'''

'''
def helper(username, timestamp, website):
    cont=[]
    for i in range(len(username)):
        cont.append([username[i],timestamp[i],website[i]])
    d={}
    cont=sorted(cont,key=lambda x:(x[1]))

    uj={}
    for elem in cont:
        if elem[0] not  in uj:
            uj[elem[0]]=[]
        uj[elem[0]].append(elem[2])
    #webset=set()
    userPatternVisit = {}
    for elem in uj.values():
        for i in range(len(elem)):
            for j in range(i+1,len(elem)):
                for k in range(j+1,len(elem)):
                    res=[]
                    #res.append([]])
                    userPatternVisit[(elem[i],elem[j],elem[k])]=userPatternVisit.get((elem[i],elem[j],elem[k]),0)+1

    ans=[]
    maxValue=float('-inf')
    print(userPatternVisit)
    val=sorted(userPatternVisit,key=lambda x:x[1],reverse=True)
    print(val)
    for k,v in userPatternVisit.items():
        if v>maxValue:
            maxValue=v
            ans=k
    return ans

    print(userPatternVisit)




print(helper(username, timestamp, website))