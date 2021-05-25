import csv
import os

files_to_load = os.path.join("Resources","election_data.csv")
output_files = os.path.join("Analysis","election_analysis.txt")
total_vote_count = 0
candidate_list = []
candidate_vote_percent = 0
votes_won = []
election_winner = []
candidate_votes = {}

with open(files_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
   

    for datarow in reader:
        total_vote_count = total_vote_count + 1
        candidate = datarow[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] = candidate_votes[candidate] + 1            

# candidate_votes['Khan']/total_vote_count * 100
highest_winner = 0
highest_winner_name = ''
output_list = [] #print line 42, 43, 44 , 45 to output file
for candidate in candidate_list:
    vote = candidate_votes[candidate]
    if vote > highest_winner: 
        highest_winner = vote
        highest_winner_name = candidate

    perc = vote/total_vote_count * 100
    candidate_output = ('{}: {}% ({})'.format(candidate, round(perc,3), vote))
    output_list.append(candidate_output)
    



output = (
    f" Election Results\n"
    f"----------------------------\n"
    f"Total votes: {total_vote_count}\n"
    f"----------------------------\n"
    f"{output_list[0]}\n"
    f"{output_list[1]}\n"
    f"{output_list[2]}\n"
    f"{output_list[3]}\n"
    f"-----------------------------\n"
    f"Winner: {highest_winner_name}\n"
    f"----------------------------\n")


with open(output_files,"w") as output_view:
    output_view.write(output)

print (output) #print candidate_output to output file.
# print line 50, 51, 52 to output file

#     Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------