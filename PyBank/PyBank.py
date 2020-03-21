import os
import csv
total_months = 0
total_amount = 0
p_l = []
months = []
avg_change = []
total_change = 0
csvpath = os.path.join("BootCamp_Data","USC-LA-DATA-PT-08-2019-U-C","03-Python","Homework","Instructions","PyBank","Resources","budget_data.csv")
with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        total_months = total_months + 1
        total_amount = total_amount + int(row[1])
        p_l.append(row[1])
        months.append(row[0])
    for  i in range(1, len(p_l)):
        avg_change.append(int(p_l[i])  - int(p_l[i - 1]))
    for i in range(len(avg_change)):
        total_change = total_change  + avg_change[i]
    avg = total_change / len(avg_change)
    maxElem = max(avg_change)
    minElem = min(avg_change)
    print("Financial Analysis")
    print(".....................................")
    print("Total Months: " +str(total_months))
    print("Total: "+ "$"+ str(total_amount) )
    print("Average Change: "+ "$" + str(avg_change.index(maxElem)))
    print("Greatest Increase in Profits: "+ months[avg_change.index(maxElem) + 1] + " " + "(" + "$"+ str(maxElem) + ")")
    print("Greatest Decrease in Profits: " + months[avg_change.index(minElem) + 1] + " " + "($" + str(minElem) + ")")

csvPath = os.path.join("PyBank.txt")
with open(csvPath,'w',newline = "") as csvfile:
    csv_writer = csv.writer(csvfile, delimiter = " ")
    csv_writer.writerow(["Financial Analysis"])
    csv_writer.writerow(["....................................."])
    csv_writer.writerow(["Total Months: " +str(total_months)])
    csv_writer.writerow(["Total: "+ "$"+ str(total_amount)])
    csv_writer.writerow(["Average Change: "+ "$" + str(avg_change.index(maxElem))] )
    csv_writer.writerow(["Greatest Increase in Profits: "+ months[avg_change.index(maxElem) + 1] + " " + "($"+ str(maxElem) + ")"])
    csv_writer.writerow(["Greatest Decrease in Profits: " + months[avg_change.index(minElem) + 1] + " "  + "($" + str(minElem) + ")"])  