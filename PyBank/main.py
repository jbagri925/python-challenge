import csv

csvpath = 'Resources/budget_data.csv'

with open(csvpath, 'r') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(reader)

    months = []
    net = []
    change =[]
    change_alt = []
    previous = 0

    for row in reader:
        months.append(row[0])
        net.append(row[1])
        
        diff = int(row[1]) - int(previous)
        previous = row[1]
        change.append(diff)


total_months = len(months)
total = sum(map(int, net))
average_change = sum(change) / len(change)
increase = max(change)
decrease = min(change)

month_decrease = 0
month_increase = 0

print(f'Financial Analysis')
print(f'___________________________')
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {month_increase}')
print(f'Greatest Decrease in Profits: {month_decrease}')

with open('PyBank.txt', 'w') as text_file:
    print(f'Financial Analysis', file=text_file)
    print(f'___________________________', file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Total: ${total}', file=text_file)
    print(f'Average Change: ${average_change:.2f}', file=text_file)
    print(f'Greatest Increase in Profits: {month_increase}', file=text_file)
    print(f'Greatest Decrease in Profits: {month_decrease}', file=text_file)
