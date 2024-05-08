def gcd(a,b):
    '''
    GCD function with two number input and modulus operation
    '''
    if a==b:
        return a
    if a < b:
        return gcd(b,a)
    if b == 0:
        return a
    return gcd(b, a%b)

def bisection_root(function,a,b):
    '''
    Bisection Function with function and two bounds input
    '''
    median = (a+b)/2
    vala = function(a)
    valb = function(b)
    valm = function(median)
    if (vala and valb) > 0 or (vala and valb) < 0:
        raise ValueError
    if (valm>0 and valm<0.0000001) or (valm<0 and valm > -0.0000001):
        return median
    if (valm and vala < 0 ) or (valm and vala >  0 ):
        return bisection_root(function,median,b)
    else:
        return bisection_root(function,a,median)

def remove_pairs(strg):
    '''
    Remove pairs of elements within string
    '''
    if len(strg)==0:
        return ""
    if strg[0:2] == "EW" or strg[0:2] == "WE" or strg[0:2] == "NS" or strg[0:2] == "SN":
        return remove_pairs(strg[2:])
    return strg[0] + remove_pairs(strg[1:])
