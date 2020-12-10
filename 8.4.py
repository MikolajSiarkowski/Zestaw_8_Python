import math
def heron(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        p = 0.5*(a+b+c)
        P= math.sqrt(p*(p-a)*(p-b)*(p-c))
        return "Pole = {}".format(P)
    else:
        raise ValueError("nie da sie zbudowac trojkata")

print("Dla bokow (3,4,5), ",heron(3,4,5))
print("Dla bokow (2,3,1), ",heron(2,3,1))
