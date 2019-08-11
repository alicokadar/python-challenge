import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

months=[]
profit= []
previous=0
monthly_change=[]

with open(pybank_csv, newline="") as csvfile:

   
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader) 
    
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
        if row[0]!="Jan-2010":
            change=int(row[1])-previous
            monthly_change.append(change)
        previous=int(row[1])
       
       
       
total_months=len(months)
sum_profit=sum(profit)
greatest_increase=max(monthly_change)

greatest_decrease=min(monthly_change)

new_monthly_change=[1]+monthly_change

new_data_set=zip(months, new_monthly_change)

for row in new_data_set:
   
    if greatest_increase==row[1]:
        greatest_increase_date=row[0]
    if greatest_decrease==row[1]:
        greatest_decrease_date=row[0]

        
average_change=sum(monthly_change)/len(monthly_change)
rounded_average_change=round(average_change,2)

analysis = ('Financial Analysis'+ '\n'+
          '------------------'+ '\n'  +
          'Total Months: ' + str(total_months) + '\n' +
          'Total: ' + ' $'+ str(sum_profit) + '\n' +
          'Average Change:' + ' $' + str(rounded_average_change) + '\n' +
          'The Greatest Increase in Profits: ' + greatest_increase_date + ' $' + str(greatest_increase) + '\n' +
          'The Greatest Decrease in Profits: ' + greatest_decrease_date + ' $' + str(greatest_decrease) + '\n')

      

print(analysis)


output_file = os.path.join("bank_report.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write(analysis)
        
