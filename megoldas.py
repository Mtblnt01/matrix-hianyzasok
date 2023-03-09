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


# 3. Volt-e olyan hét, amikor ötnél kevesebb hiányzás volt
# 3. feladat: Volt olyan hét, amikor ötnél kevesebb hiányzó volt

index=0
while index<len(hianyzasok) and not (sum(hianyzasok[index]))<5:
    index+=1
if index<len(hianyzasok):
    print("Volt olyan hét, amikor ötnél kevesebb hiányzás volt.")
else:
    print("Nem volt olyan hét, amikor ötnél kevesebb hiányzás volt.")


# 5. Hányadik héten volt egyetlen hiányzás?
# 5. feladat: 4. héten volt egyetlen hiányzás
