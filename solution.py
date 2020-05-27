from fractions import Fraction
from itertools import permutations 

def one_dig_div(x,y):
    if x[0]==y[0]: a=x[1]
    else: a=x[0]
    if x[1]==y[1]: b=y[0]
    else: b=y[1]
    return a/b

ans=Fraction(1,1)
perm = permutations(range(1,10), 2)
perm=list(perm)
for num in perm:
    for den in perm:
        if num == den: continue
        if den[0] in num or den[1] in num:
            if (num[0]*10+num[1])/(den[0]*10+den[1]) == one_dig_div(num,den):
                print(num[0]*10+num[1],"/", den[0]*10+den[1])
                ans*=Fraction(num[0]*10+num[1],den[0]*10+den[1])
print("Sol.: ", ans.denominator)
