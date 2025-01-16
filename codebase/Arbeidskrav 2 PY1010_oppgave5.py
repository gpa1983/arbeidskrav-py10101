"""
Program : PY1010 Arbeidskrav 2  (Oppg 5)
Created on Thu Jan 16 2025
Author : Ghanashyam Niroula
"""
#Oppg 5)

import math

def beregn_figur(a, b):
    # Radius for halvsirkelen
    r = a / 2
    
    # Areal av trekanten
    trekant_areal = (a * b) / 2
    
    # Areal av halvsirkelen
    halvsirkel_areal = (math.pi * (r*r)) / 2
    
    # Totalt areal
    totalt_areal = trekant_areal + halvsirkel_areal
    
    # Ytre omkrets (svart strek): b + hypotenusen til trekanten + omkrets av halvsirkelen
    hypotenus = math.sqrt(a**2 + b**2)
    halvsirkel_omkrets = math.pi * r
    ytre_omkrets = b + hypotenus + halvsirkel_omkrets
    
    # Returnerer resultatene
    return totalt_areal, ytre_omkrets

# Brukeren skriver inn verdier for a og b
a = float(input("Skriv inn lengden av a: "))
b = float(input("Skriv inn lengden av b: "))

# Kall funksjonen og hent resultater
areal, omkrets = beregn_figur(a, b)

# Skriver ut resultatene
print(f"Arealet til figuren er: {areal:.2f}")
print(f"Den ytre omkretsen til figuren er: {omkrets:.2f}")
