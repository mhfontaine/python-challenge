#import budget data 
import os
import csv 
#working directory

#csvpath=os.path.join('..','Resources','budget_data.csv')
budget_data = os.path.join(r"/Users/marvinfontaine/Data-Analytics/Homework/python-challenge/PyBank/Resources/budget_data.csv")

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    
    #print(f"Header: {csv_header}")               

#Months       
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
   # print(len(month))
 #Revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    #print(total_revenue)

 #Avg Change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
 # append profit_loss
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    #print(revenue_change)
    monthly_change = Total / len(revenue_change)
    #print(monthly_change)
    #print(Total)
    
#Greatest Increase
    profit_increase = max(revenue_change)
    #print(profit_increase)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]
    
#Greatest Decrease
    profit_decrease = min(revenue_change)
    #print(profit_decrease)
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]



#Print statements output to screen
print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')
print("Total number of months: " + str(len(month)))
print("Total Revenue in period: $ " + str(total_revenue))
print("Average monthly change in Revenue : $" + str(monthly_change))
print(f"Month with Greatest Increase in Profits: {month_increase} (${profit_increase})")
print(f"Month with Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

# Path to name and write output file
output_path = os.path.join("Analysis", "FinancialResultsFile.txt")

# Code to create output file
with open(output_path, 'w') as outfile:
     outfile.write(f'Financial Analysis'+'\n')
     outfile.write(f'----------------------------'+'\n')
     outfile.write("Total number of months: " + str(len(month)))
     outfile.write('\n')
     outfile.write("Total Revenue in period: $ " + str(total_revenue))
     outfile.write('\n')
     outfile.write("Average monthly change in Revenue : $" + str(monthly_change))
     outfile.write('\n')
     outfile.write(f"Month with Greatest Increase in Profits: {month_increase} (${profit_increase})")
     outfile.write('\n')
     outfile.write(f"Month with Greatest Decrease in Profits: {month_decrease} (${profit_decrease})") 
     outfile.close()
