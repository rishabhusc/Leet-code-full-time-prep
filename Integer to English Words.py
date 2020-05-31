n=12345
def helper(n):
    top19="One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirtenn Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
    tens="Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
    if n<20:
       
        return top19[n-1:n]
    if n<100:
        return [tens[n//10 -2]]+helper(n%10)
    if n<1000:
        return [top19[n//100 -1]] +['Hundred'] + helper(n%100)
    for p,w in enumerate(('Thousand', 'Billion', 'Million')):
        if n<1000**(p+1):
            return helper(n//1000**p)+[w]+helper(n%1000**p)

print(' '.join(helper(n) or "Zero"))

