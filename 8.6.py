def rekurencjaP(i,j):
    if i == 0 and j == 0:
        return 0.5
    if i>0 and j ==0:
        return 0.0
    if i == 0 and j > 0:
        return 1.0
    if i>0 and j>0:
        return 0.5*(rekurencjaP(i-1,j)+rekurencjaP(i,j-1))
    else:
        raise ValeError("Zle dane wejsciowe")

def dynamicP(i,j):
    wartosc = {}
    if (i,j) in wartosc:
        return wartosc[i,j]
    else:
        if i == 0 and j == 0:
            wartosc[i,j] = 0.5
        if i > 0 and j == 0:
            wartosc[i,j] = 0.0
        if i == 0 and j > 0:
            wartosc[i,j] = 1.0
        if i > 0 and j > 0:
            wartosc[i,j] = 0.5*(dynamicP(i-1,j)+dynamicP(i,j-1))
    return wartosc[i,j]
    

    
print("rekurencyjnie P(2,1) = ",rekurencjaP(2,1))
print("rekurencyjnie P(0,0) = ",rekurencjaP(0,0))
print("rekurencyjnie P(0,1) = ",rekurencjaP(0,1))
print("rekurencyjnie P(1,0) = ",rekurencjaP(1,0))

print("dynamicznie P(2,1) = ",dynamicP(2,1))
print("dynamicznie P(0,0) = ",dynamicP(0,0))
print("dynamicznie P(0,1) = ",dynamicP(0,1))
print("dynamicznie P(1,0) = ",dynamicP(1,0))
