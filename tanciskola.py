#!/usr/bin/python3
# -*- coding:utf-8 -*- 
"""2015.majus.12 Idegen nyelvi Informatika erettsegi python programozasi nyelven."""
print("1. feladat")
"""Be kell olvasni a tancrend.txt --t amit en egy szotarba gondolok megtenni.Ami igy nezne ki:
tancrend={Hanyadik tanc={
"tanc neve":"cha-cha"
"ferfi tag":"Feri"
"Noi tag":"Irma"        
}
}
"""
tancrend={}
szam=0
n=0
with open("tancrend.txt", "rt", encoding="utf-8") as f:
    for s in f:
        sor = s.replace("\n", "")
        szam+=1
        if szam == 1:
            n+=1
            tancrend[n] = {}
            tancrend[n]["Tanc neve"]=sor
        elif szam == 2:
            tancrend[n]["Lany neve"]=sor
        elif szam == 3:
            tancrend[n]["Fiu neve"]=sor
            szam=0
#print(tancrend)

print("2. feladat")
"""Elsokent es utolsokent bemutatott tanc nevet ki kell irni a kepernyore."""
print("Elsokent bemutatott tanc neve: {0}\nUtolsokent bemutatott tanc neve: {1}".format(tancrend[1]["Tanc neve"], tancrend[len(tancrend)]["Tanc neve"]))

print("3. feladat")
"""Ki kell irni hogy hany par mutatta be a szambat."""
print("{} par mutatta be a sambat".format(len([a['Tanc neve'] for a in tancrend.values() if a['Tanc neve'] == "samba"])))

print("4. feladat")
"""Ki kell irni a kepernyore hogy Vilma melyik tancokben szerepelt."""
print("Vilma ezekben a tancokben szerepelt: {}".format(" ".join([a["Tanc neve"] for a in tancrend.values() if a["Lany neve"] == "Vilma"])))

print("5. feladat")
"""Be kell kerni egy tanc nevet es meg kell adni hogy azt a tancot Vilma kivel mutatta be."""
tanc=str(input("Kerem adjon meg egy tanc nevet: "))
bemutat=False
for a in tancrend.values():
    if a["Lany neve"] == "Vilma" and a["Tanc neve"] == tanc:
        print("Vilma {0} tancban {1} volt a parja.".format(tanc, a["Fiu neve"]))
        bemutat=True
        break
if bemutat== False:
    print("Vilma nem tancolt {}-t".format(tanc))
        
#print("6. feladat")
"""Keszitsen listat a bemutaton resztvett lanyokrol es fiukrol es ki kell irni a szepeplok.txt fajlba."""
lany = []
fiu = []
for a in tancrend.values():
    if a["Lany neve"] not in lany:
        lany.append(a["Lany neve"])
    if a["Fiu neve"] not in fiu:
        fiu.append(a["Fiu neve"])

with open("szereplok.txt", "wt", encoding="utf-8") as g:
    g.write("Lanyok: {0}\nm".format(", ".join(lany)))
    g.write("Fiuk: {}".format(", ".join(fiu)))
    
print("7. feladat")
"""Ki kell irni melyik fiu szerepel a legtobbszor a fiuk kozul es melyik lany szerepel a legtobszor a lanyok kozul."""
fiuk = []
lanyok = []
for v in tancrend.values():
    fiuk.append(v["Fiu neve"])
    lanyok.append(v["Lany neve"])
szotarfiu = {}
szotarlany = {}
for f in set(fiuk):
    szotarfiu[fiuk.count(f)] = f
for l in set(lany):
    szotarlany[lanyok.count(l)] = l
print("Fiuk kozul {} szerepelt a legtobbszor.".format([szotarfiu[k] for k in sorted(szotarfiu.keys())][-1] ))
print("Lanyok kozul {} szerepelt a legtobbszor.".format([szotarlany[k] for k in sorted(szotarlany.keys())][-1] ))