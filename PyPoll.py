# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
i = 0

# 4. List for names of candidates
candidate_votes = dict()
candidate_list = list()

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    #print(headers)

     # Print each row in the CSV file.
    for row in file_reader:
        #print(row)
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

         # Add the candidate name to the candidate list.
        #   Get unique candidate names
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
    
           # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

       # Add a vote to that candidate's count 
        candidate_votes[candidate_name] += 1


# 3. Print the total votes.
print(f'Total votes:{total_votes}')

# Print the candidate list.
print(candidate_list)

# Print candidate votes dictionary
print(candidate_votes)

#   Get percentage of votes casted for every candidate
winning_count = 0
winning_percentage = 0

for i in candidate_list:
    percentage = float(candidate_votes[i]/total_votes * 100)
    #print(f'Percentage of Votes casted for {i} is equal to {percentage}') 
    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{i}: {percentage:.1f}%  {candidate_votes[i]} \n")
    if candidate_votes[i] > winning_count:
        winning_count = candidate_votes[i]
        winning_percentage = percentage
        winner = i
        

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)