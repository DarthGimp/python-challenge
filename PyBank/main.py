import csv
import os

print("Current Work Directory:", os.getcwd())

file_path = "/Users/obsid/Desktop/python-challenge/PyBank/Resources/budget_data.csv"
output_path = "analysis/financial _analysis.txt"

total_months = 0
total_profit_loss = 0
prev_profit_loss = None
changes = []
greatest_increase = {'date': '', 'amount': float('-inf')}
greatest_decrease = {'date': '', 'amount': float('inf')}


with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        date = row[0]
        profit_loss = int(row[1])


        total_months += 1
        total_profit_loss += profit_loss

        if prev_profit_loss is not None:
            change = profit_loss - prev_profit_loss
            changes.append(change)

            if change > greatest_increase['amount']:
                greatest_increase['amount'] = change
                greatest_increase['date'] = date

            if change < greatest_decrease['amount']:
                greatest_decrease['amount'] = change
                greatest_decrease['date'] = date

        prev_profit_loss = profit_loss

average_change = sum(changes) / len(changes) if changes else 0

analysis = (
    "Financial Analysis\n"
    "---------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase In Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease In Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
    )
print(analysis)

with open(output_path, mode='w') as file:
    file.write(analysis)

print(f"Analysis results have been save to {output_path}")
