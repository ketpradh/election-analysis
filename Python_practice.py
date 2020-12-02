print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if counties[2] != 'Jefferson':

   print(counties[2])

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")   

for county in counties:
    print(county)     

counties_dict = {"Arapahoe":42222, "Denver":3000, "Jefferson":5000}
for i in counties_dict.keys():  
    print(counties_dict.get(i))
    print(i)

str1 = " county has "
str2 = " registered voters."
for i, j in counties_dict.items():
    #print(str(i) + str1 + str(j) + str2 )
    #print("{}{}{}{}".format(i,str1,j,str2))
    print(f'{i} county has {j:,} registered voters')

for i in counties_dict:
    for j in counties_dict.values():
        print(j)
