"""
Program : PY1010 Arbeidskrav 2  (Oppg 4)
Created on Thu Jan 16 2025
Author : Ghanashyam Niroula
"""
#Oppg 4)

#a)
# Opprett dictionary
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

#b,c)
# Be brukeren skrive inn et land
land = input("Skriv inn et land: ")

# Sjekk om landet finnes i dictionaryen
if land in data:
    hovedstad, innbyggere = data[land]
    print(f"Hovedstaden i {land} er {hovedstad}, og den har {innbyggere} millioner innbyggere.")
else :
    new_capital=input(f"Could not find this country in the dataset\nEnter capital of {land} : ")
    new_population=float(input(f"Enter population of {land} in millions : "))   
    data.update({land:[new_capital,new_population]})
    print(f"New country {land} added to dataset")
    print(str(data))

