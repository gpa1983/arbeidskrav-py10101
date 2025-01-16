"""
Program : PY1010 Arbeidskrav 2  (Oppg 3)
Created on Thu Jan 16 2025
Author : Ghanashyam Niroula
"""
#Oppg 3)

import numpy as np

def grader_til_radianer(v_grad):
    # Regner om fra grader til radianer
    return v_grad * np.pi / 180

# Brukeren skriver inn gradtallet
v_grad = float(input('Skriv inn gradtallet: '))

# Kall funksjonen og regn ut radianer
v_rad = grader_til_radianer(v_grad)

# Skriver resultatet til skjermen
print(f'Vinkelen på {v_grad} grader tilsvarer {v_rad:.4f} radianer.')
