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


# 1. Hány óra hiányzás volt összesen?
# 1. feladat: 30 óra hiányzás volt összesen
osszeg=0
for het in hianyzasok:
    osszeg+=sum(het) 
print(f"1.feladat: {osszeg} óra hiányzás volt összesen")