lst=[5,4,3,2,1]
def helper(lst):
    one=two=three=float('inf')
    for i in lst:
        if i<=one:
            one=i
        elif i<=two:
            two=i
        else:
            return True
    return False
print(helper(lst))