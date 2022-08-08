def gcd_2(a,b):		
    a,b = max(a,b),min(a,b)
    if a%b == 0:
        return b
    else:
        return gcd_2(b,a%b)

def gcd(s):
    g = 0
    for i in range(len(s)):
        if i == 0:
            g = s[i]
        else:
            g=gcd_2(g,s[i])
    return g

