import csv
import os

input_file_path = "Resources/election_data.csv"
output_file_path = "analysis/election_results.txt"

total_votes = 0
candidate_vote = {}

with open(input_file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        total_votes += 1
        candidate = row[2]

        if candidate not in candidate_vote:
            candidate_vote[candidate] = 0
        candidate_vote[candidate] +=1

winner = max(candidate_vote, key=candidate_vote.get)

results = (
    "Election Results\n"
    "--------------------------------\n"
    f"Total Votes: {total_votes}\n"
    "--------------------------------\n"
)

for candidate, votes in candidate_vote.items():
    percentage = (votes / total_votes) * 100
    results += f"{candidate}: {percentage:.3f}% ({votes})\n"
    
results += (
    "---------------------------------\n"
    f"Wienner: {winner}\n"
    "---------------------------------\n"
)

print(results)\

with open(output_file_path, mode='w') as file:
    file.write(results)

print(f"Analysis results have been saved to {output_file_path}")