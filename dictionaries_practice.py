voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

counties_dict = {"Arapahoe":42222, "Denver":3000, "Jefferson":5000}

for county_dict in voting_data:
    print(county_dict)

for county_dict in range(len(voting_data)):
    print(voting_data[county_dict])
    
for i in voting_data:
    for j in i.values():
        print(j)

for i in voting_data:
    print(f"{i['county']} county has {i['registered_voters']} registered voters")        
