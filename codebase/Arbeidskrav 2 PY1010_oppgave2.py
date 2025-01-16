"""
Program : PY1010 Arbeidskrav 2  (Oppg 2)
Created on Thu Jan 16 2025
Author : Ghanashyam Niroula
"""
import math

antall_elever = int(input('Skriv inn antall elever: '))
if antall_elever < 0 :
    print(f'Assumimg that minus was a mistake !!')
    antall_elever = -1*antall_elever
pizza_per_elev = 0.25
totalt_pizzaer = antall_elever * pizza_per_elev

# Rund opp til nærmeste heltall for å sikre at det er nok pizza
pizzaer_å_handle = math.ceil(totalt_pizzaer)

print(f'Det må handles inn {pizzaer_å_handle} pizzaer til {antall_elever} elever til festen.')

