def gcd(a,b):
    if a==b:
        return a
    elif a < b:
        return gcd(b,a)
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)

def bisection_root(function,a,b):
    median = (a+b)/2
    vala = function(a)
    valb = function(b)
    valm = function(median)
    if (vala > 0 and valb > 0) or (vala < 0 and valb < 0):
        raise ValueError
    if valm<0.001:
        return value
    elif (valm < 0 and vala < 0) or (valm>0 and vala>0)
        return bisection_root(function,valm,b)
    elif (valm < 0 and valb < 0) or (valm>0 and valb>0)
        return bisection_root(function,a,valm)