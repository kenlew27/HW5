import math


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
    if (valm>0 and valm<0.0000001) or (valm<0 and valm> -0.0000001):
        return median
    elif (valm < 0 and vala < 0) or (valm >  0 and vala > 0):
        return bisection_root(function,median,b)
    else:
        return bisection_root(function,a,median)
        
def remove_pairs(str):
    if len(str)==0:
        return ""
    if str[0:2] == "ew" or str[0:2] == "we" or str[0:2] == "ns" or str[0:2] == "sn":
        return remove_pairs(str[2:])
    else:
        return str[0] + remove_pairs(str[1:])







