#0. feladat: A hianyzasok.txt beolvasása listában listákba
hianyzasok=[]
with open("./adatok/hianyzasok.txt","r",encoding="utf-8") as fm:
    for sor in fm:
        seged_lista=sor.strip().split(",")
        # l=[]
        # for szam in seged_lista:
        #     l.append(int(szam))
        # hianyzasok.append(l)
        hianyzasok.append(list(map(int, seged_lista)))
print("A beolvasott mátrix: ")
print(hianyzasok)

#1. feladat: Hány óra hiányzás volt összesen?
#30 óra hiányzás volt összesen
osszeg=0
for het in hianyzasok:
    osszeg+=sum(het)

print(f"{osszeg} óra hiányzás volt összesen")
