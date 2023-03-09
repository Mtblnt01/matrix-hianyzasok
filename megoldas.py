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

print("A beolvasott matrix")
print(hianyzasok)


# 1. Hány óra hiányzás volt összesen?
# 1. feladat: 30 óra hiányzás volt összesen
osszeg=0
for het in hianyzasok:
    osszeg+=sum(het) 
print(f"1.feladat: {osszeg} óra hiányzás volt összesen")

# 2. Volt-e olyan hét, amikor nem volt hiányzó?
def eldontes(hianyzasok):
    i=0
    while i<len(hianyzasok[i]) and not(sum(hianyzasok[i])>=1):
        i+=1
    van=i<len(hianyzasok[i])
    return van
if eldontes(hianyzasok):
    print("2.Feladat: Nem volt olyan hét, amikor nem volt hiányzó")
else:
    print("Volt olyan hét, amikor nem volt hiányzó")