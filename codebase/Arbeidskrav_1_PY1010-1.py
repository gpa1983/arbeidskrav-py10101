# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:23:39 2024

@author: ghanashyam.niroula
"""

# Dictionary for electric car
electric_car = {
    "årlig_forsikring": { 
        "beløp": 5000.0
    },
    "daily_traffic_insurance_rate": { 
        "beløp": 8.38
    },
    "yearly_kilometer": 10000.0,
    "fuel_rate_per_km": {
        "beløp": 0.4  # This is the result of 0.2 * 2.0
    },
    "Bomavgift_per_km": {
        "beløp": 0.1
    }
}

# Dictionary for petrol car
petrol_car = {
    "årlig_forsikring": { 
        "beløp": 7500.0
    },
    "daily_traffic_insurance_rate": { 
        "beløp": 8.38
    },
    "yearly_kilometer": 10000.0,
    "fuel_rate_per_km": {
        "beløp": 1
    },
    "Bomavgift_per_km": {
        "beløp": 0.3
    }
}

# Function to retrieve cost from a dictionary
def get_cost(kostnad):
    return kostnad["beløp"]

# Function to calculate total annual cost for a car
def beregn_bilkostnad(bil):
    net_cost = 0.0
    
    # Add annual insurance cost
    net_cost += get_cost(bil["årlig_forsikring"])
    
    # Add daily traffic insurance cost (daily rate * 365)
    net_cost += get_cost(bil["daily_traffic_insurance_rate"]) * 365
    
    # Add fuel cost (fuel rate per km * yearly kilometer)
    net_cost += get_cost(bil["fuel_rate_per_km"]) * bil["yearly_kilometer"]
    
    # Add toll cost (toll rate per km * yearly kilometer)
    net_cost += get_cost(bil["Bomavgift_per_km"]) * bil["yearly_kilometer"]
    
    return net_cost

# Find annual cost for electric car
elbil_kostnad = beregn_bilkostnad(electric_car)

# Find annual cost for petrol car
bensinbil_kostnad = beregn_bilkostnad(petrol_car)

# Print annual costs
print("Elbil koster", elbil_kostnad, "NOK årlig")
print("Bensinbil koster", bensinbil_kostnad, "NOK årlig")

# Compare costs and print the difference
if (elbil_kostnad - bensinbil_kostnad) > 0:
    print("Elbil koster", elbil_kostnad - bensinbil_kostnad, "NOK mer enn bensinbil årlig")
else:
    print("Bensinbil koster", bensinbil_kostnad - elbil_kostnad, "NOK mer enn elbil årlig")
