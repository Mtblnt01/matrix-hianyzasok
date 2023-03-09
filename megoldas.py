#0.feladat A hianyzasok.txt beolvasa listaban listakba

hianyzasok=[]
with open("./adatok/hianyzasok.txt","r",encoding="UTF-8") as fm:
    for sor in fm:
        seged_lista=sor.strip().split(",")
        # l=[]
        # for szam in seged_lista:
        #     l.append(int(szam))
        # hianyzasok.append(l)
        hianyzasok.append(list(map(int, seged_lista)))

print("A beolvasott matrix")
print(hianyzasok)