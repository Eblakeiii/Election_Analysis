# Add dependencies
import csv
import os

# Assign variable to a file to load with path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to file to be saved with the new info
file_to_save = os.path.join("analysis", "(election_analysis.txt")

# Initialize vote counter
total_votes = 0

# Declare a list
candidate_options = []

# Declare a dictionary
candidate_votes = {}

# Winning candidate name and info
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the loaded file to be read and assign name to the file applying the csv function
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row and omit from calculations
    headers = next(file_reader)
    # Go through all the rows in the csv file
    for row in file_reader:
        # Tally total votes
        total_votes += 1
        # Identify candidate name from each row
        candidate_name = row[2]
        # Add candidate name to the list if not on list s
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Sets candidate votes to zero
            candidate_votes[candidate_name] = 0
        # Increment candidate votes
        candidate_votes[candidate_name] += 1
    
        # Identify winning candidate and vote count   
        # Iterate through the candidate list
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote ({votes:,})\n")

        # Print out each candidate's name, vote count, and percentage of votes
        if (votes > winning_count) and (vote_percentage > winning_percentage):           
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
    # Print winner summary
    winner_summary = (
        f"------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------------------\n")
    print(winner_summary)
