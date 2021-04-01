from random import randint
#print(randint(1,10))
from math import * 
print(pi)
print(sqrt(4))
print(pow(2,3))
print(2**3)
print(e)
print(tau)
print(ceil(9.81))
print(ceil(9.18))
print(floor(9.81))
print(floor(9.18))
print(round(9.81))
print(round(9.18))
# We can import our own modules.
from countrieslist import countries
from pprint import pprint
#pprint(countries)
countries_withland=[]
for country in countries:
    if 'land' in country:
       # print(country)
       countries_withland.append(country)
#print(countries_withland)
from countries_data import countriesData
#pprint(countriesData)

for country in countriesData:
    pprint(country)