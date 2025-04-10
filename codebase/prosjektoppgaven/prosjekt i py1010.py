#Prosjekt i PY1010 

#Problembeskrivelse
#Programmet analyserer månedlige salgsdata fra en mobiltelefonbutikk, beregner totalt salg, identifiserer måneder med høyest og lavest salg, og visualiserer salgstrender over tid.
#Datasettet er en CSV-fil med to kolonner: Måned og Salg.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Custom funksjon for å laste inn data fra en fil
def last_inn_data(file_path):
    """
    Laster inn data fra en CSV-fil og returnerer det som en DataFrame.
    """
    return pd.read_csv(file_path)

# Custom funksjon for å beregne grunnleggende statistikk
def beregn_statistikk(salgsdata):
    """
    Beregner og returnerer totalt, gjennomsnittlig, maks og min salg.
    """
    totalt_salg = np.sum(salgsdata)
    gjennomsnitt_salg = np.mean(salgsdata)
    maks_salg = np.max(salgsdata)
    min_salg = np.min(salgsdata)
    return totalt_salg, gjennomsnitt_salg, maks_salg, min_salg

# Last inn data
file_path = "sales_data.csv"  # Erstatt med CSV-filnavn
data = last_inn_data(file_path)

# Hent ut 'Sales'-kolonnen
salg = data['Sales']

# Beregn statistikk
totalt, gjennomsnitt, maks_salg, min_salg = beregn_statistikk(salg)
print(f"Totalt salg: {totalt}")
print(f"Gjennomsnittlig salg: {gjennomsnitt}")
print(f"Høyeste salg: {maks_salg}")
print(f"Laveste salg: {min_salg}")

# Identifiser måneder med høyest og lavest salg
maks_måned = data.loc[data['Sales'].idxmax(), 'Month']
min_måned = data.loc[data['Sales'].idxmin(), 'Month']
print(f"Høyeste salg var i: {maks_måned}")
print(f"Laveste salg var i: {min_måned}")

# Lagre sammendrag i en fil
sammendrag = f"""
Totalt salg: {totalt}
Gjennomsnittlig salg: {gjennomsnitt}
Høyeste salg: {maks_salg} (Måned: {maks_måned})
Laveste salg: {min_salg} (Måned: {min_måned})
"""
with open("salg_sammendrag.txt", "w") as f:
    f.write(sammendrag)
print("Sammendrag lagret i salg_sammendrag.txt")

# Plot salgsdata
plt.figure(figsize=(10, 6))
plt.plot(data['Month'], data['Sales'], marker='o', linestyle='-', color='b')
plt.title('Månedlig Salgsdata')
plt.xlabel('Måned')
plt.ylabel('Salg')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("salgs_trend.png")  # Lagre plottet som et bilde
print("Lukk plottet for å avslutte")
plt.show()
