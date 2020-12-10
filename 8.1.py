def solve1(a,b,c):
    if a == 0 and b == 0:
        if c == 0:
            return "nieskonczenie wiele rozwiazan"
        else:
            return "sprzecznosc, brak rozwiazan"
    if a != 0 and b == 0:
        return "B jest rowne 0, rozwiaznie: ({},y), y z przedzialu".format(-c/a)
    if a == 0 and b != 0:
        return "A jest rowne 0, rozwiaznaie: (x,{}), x z przedzialu".format(-c/b)
    if a != 0 and b != 0:
        if c == 0:
            return "rozwiazanie: (x,{}*x), x z przedziału".format(-a/b)
        else:
            return "rozwiazanie: (x,{}*x+{}), x z przedzialu".format(-a/b,-c/b)

print("1.Dla a=0,b=0,c=0\n",solve1(0,0,0))
print("2.Dla a=0,b=0,c=1\n",solve1(0,0,1))
print("3.Dla a=1,b=0,c=1\n",solve1(1,0,1))       
print("4.Dla a=0,b=1,c=1\n",solve1(0,1,1))
print("5.Dla a=1,b=1,c=0\n",solve1(1,1,0))
print("6.Dla a=1,b=1,c=1\n",solve1(1,1,1))
