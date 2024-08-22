import os
import csv

budget_csv = os.path.join("C://Users//16692//Desktop//python-challange//PyBank//resources//budget_data.csv")



# open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
 #skip the header row
    next(csv_reader)
    data = [row for row in csv_reader]

   #Analyze the data
   # Total number of months included in the dataset
    total_months = len(data)
    print(f"Total Months: {total_months}")


#The net total amount of "profit/losses" over the entire period
total= sum(int(row[1]) for row in data)
print(f"Total: {total}  ")


#Changes in profit/losses over the entire period, and then the average of those changes
changes = [int(data[i+1][1])-int(data[i][1]) for i in range (len(data)-1)]
average = sum(changes)/len(changes)
print(f"average: {average}")      

#Greatest increase in profits over the entire period
max_increase = max(changes)
max_increase_index = changes.index(max_increase)
max_date = data[max_increase_index + 1][0]
print(f"Greatest Increase in profits :{max_date} (${max_increase})")


#Greates decrease in profits over the entire period.
max_decrease = min(changes)
max_decrease_index = changes.index(max_decrease)
max_decrease_date = data[max_decrease_index + 1][0]
print(f"Greatest Decrease in profits :{max_decrease_date} (${max_decrease})")

#exporting result in text file
with open("budget_data_analysis.txt","w")as file:
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: {total}\n")
    file.write(f"average: {average}\n")
    file.write(f"Greatest Increase in profits :{max_date} (${max_increase})\n")
    file.write(f"Greatest Decrease in profits :{max_decrease_date} (${max_decrease})")

#confirmation msg
print("budget_data_analysis.txt is saved")    