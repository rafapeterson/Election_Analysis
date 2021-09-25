# The data we need to retrieve.

#assign a variable for the file to load and the path
#file_to_load = 'Resources/election_results.csv'

#add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

#declare a new list to record candidates
candidate_options = []

# Create a dictionary of candidates w vote count

candidate_votes = {}

# Winning candidate & winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here.
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            # Add name to list of candidates
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1.Iterate through the candidate list.
for candidate_name in candidate_votes:
    
    # 2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]

    # 3. Calculate percentage of votes
    vote_percentage = (float(votes) / float(total_votes)) * 100

   
    # Print the candidate name & percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine winning vote count & candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes & winning_percent =
        # vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set winning_candidate equal to candidate's name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print (winning_candidate_summary)


# Create a filename variable to a direct or indirect path to the file.

# Using the open() function with the "w" mode we will write data to the file.
#with open(file_to_save, "w") as txt_file:
    # write some data to the file.
    #txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")

#close the file
#txt_file.close()
#To do: perform analysis


#close the tile.




# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.