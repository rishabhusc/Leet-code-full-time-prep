asteroids = [5, 10, -5]
def helper(asteroids):
    ans=[]
    for elem in asteroids:
        while len(ans)!=0 and elem<0 and 0<ans[-1]:
            if -elem<ans[-1] or -elem==ans.pop():
                break
        else:
            ans.append(elem)
    return ans
print(helper(asteroids))