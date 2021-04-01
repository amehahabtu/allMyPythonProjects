nums=[1,2,3,4]
new_nums=[]
for i in nums:
    #print(i*i)
    new_nums.append(i*i)
print(new_nums)
#let us do it using list comprehension 
new_nums=[i*i for i in nums ] # This is list comprehension method.
print(new_nums)
new_nums=[i*i for i in nums if i>=3] # This is list comprehension method.
print(new_nums)
countries =['USA','Ethiopia','Finland','Denmark','England','Kenya','Korea','Isreal']
new_countries=[]
for country in countries:
    #print(country)
    new_countries.append(country.upper())
print(new_countries)
# using list comprehension method
new_countries=[country.upper() for country in countries]
print(new_countries)
# new_countries=[country.upper() for country in countries if 'land' in country]
# print(new_countries)
new_countries=[[country,country.upper(),country.upper()[0:3]] for country in countries]
print(new_countries)
evens=list(range(0,101,2))
print(evens)
odds=list(range(1,100,2))
print(odds)