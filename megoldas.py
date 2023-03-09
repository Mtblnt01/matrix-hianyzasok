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

# 3. Volt-e olyan hét, amikor ötnél kevesebb hiányzás volt
# 3. feladat: Volt olyan hét, amikor ötnél kevesebb hiányzó volt

index=0
while index<len(hianyzasok) and not (sum(hianyzasok[index]))<5:
    index+=1
if index<len(hianyzasok):
    print("Volt olyan hét, amikor ötnél kevesebb hiányzás volt.")
else:
    print("Nem volt olyan hét, amikor ötnél kevesebb hiányzás volt.")

# 4. Melyik héten volt a legtöbb hiányzás?
def maximum_kivalasztas(hianyzasok):
    max_index=0
    for index in range(1,len(hianyzasok)):
        if hianyzasok[max_index]<hianyzasok[index]:
            max_index=index
    return max_index
print(maximum_kivalasztas(hianyzasok))
print(f"A legtöbb hiányzás a {maximum_kivalasztas(hianyzasok)+1}. héten volt ({sum(hianyzasok[2])} óra)") 



# 5. Hányadik héten volt egyetlen hiányzás?
# 5. feladat: 4. héten volt egyetlen hiányzás
index=0
while index<len(hianyzasok) and not(sum(hianyzasok[index])==1):
    index+=1

van=index<len(hianyzasok)
if van:
    sorszam=index
    print(f"5. feladat: 4. héten volt egyetlen hiányzás")
else:
    sorszam=-1
    print(f"5. feladat: egyik héten sem volt egyetlen hiányzás")
    
