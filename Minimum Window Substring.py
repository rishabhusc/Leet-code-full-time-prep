S = "ADOBECODEBANC"
T = "ABC"
def helper(S,T):
    d={}
    for i in T:
        d[i]=d.get(i,0)+1
    i=0
    j=0
    minlength=len(S)
    len_S,len_T=len(S),len(T)
    output=''
    while i<len_S:
        if S[i] in d:
            if d[S[i]]>0:
                len_T-=1
            d[S[i]]-=1
        while len_T==0:
            if i-j+1<minlength:
                minlength=i-j+1
                output=S[j:i+1]
            if S[j] in d:
                d[S[j]]+=1
                if d[S[j]]>0:
                    len_T+=1
            j+=1
        i+=1
    return output
print(helper(S,T))