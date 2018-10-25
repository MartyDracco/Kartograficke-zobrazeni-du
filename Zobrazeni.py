#Kartograficke zobrazeni

#Lambertovo
#zakl vzorec pro vypocet:
#x = R* v , y = R*sin u

#R = 6371.11 km
import math
import string

R = 6371.11
L =()
A =()
B =()
M =()
zobrazeni=input("Zadej typ zobrazeni")


if zobrazeni == L:
    print "Lambertovo zobrazeni"
    m = int(input("Zadej meritko ve formatu 1:(zadane cislo)"))
    v = int(input("Zadej souradnici poledniku"))
    a = R * v / m
    print a
    #ted potrebuji prevest cislo a na centimetry na papire
    print "souradnice poledniku v centimetrech je", a*10, "cm od stredu"
elif zobrazeni == A:
    print "Marinovo zobrazeni"
    #doplnit
elif zobrazeni == B:
    print "Braunovo zobrazeni"
elif zobrazeni == M:
    print "Mercatorovo zobrazeni"
elif zobrazeni != L or zobrazeni !=A or zobrazeni!= B or zobrazeni!= M:
    print("Toto zobrazeni neni v programu")
else:
    print("Toto zobrazeni nelze vypocitat")

#doplnit lambertovo zobrazeni jako funkci





