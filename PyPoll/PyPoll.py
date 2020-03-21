import os
import csv
total_count = []
d = {}
total = 0
csvpath = os.path.join("BootCamp_Data","USC-LA-DATA-PT-08-2019-U-C","03-Python","Homework","Instructions","PyPoll","Resources","election_data.csv")
with open(csvpath, newline="")as csvfile:
    csv_reader= csv.reader(csvfile, delimiter =",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        total_count.append(row[2])
    for i in range(len(total_count)):
        if total_count[i] in d:
            d[total_count[i]] = d[total_count[i]] + 1
            
        else:
            d[total_count[i]] = 1
    for i in d.values():
        total = total + i
    print("Election Results")
    print("..............................")
    print("Total Votes: "+str(total))
    print("..............................")
    for x, y in d.items():
        print(x +": "+str(round((y/total)*100,3))+"% "+"(" +str(y) + ")")
      
    max = 0 
    for i, y in d.items():
        if y > max:
            max = y
            winner = i
    print("........................")
    print("Winner: "+str(winner))
    print(".........................")

    csvpath = ("pyPoll.txt")
    with open(csvpath,'w', newline = "") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Election Result"])
        csv_writer.writerow(["..................................."])
        csv_writer.writerow(["Total Votes: "+str(total)])
        csv_writer.writerow(["......................................."])
        for x, y in d.items():
            csv_writer.writerow([x +": "+str(round((y/total)*100,3))+"% " +"("+str(y)+")"])
        csv_writer.writerow(["........................"])
        csv_writer.writerow(["Winner: "+str(winner)])
        csv_writer.writerow(["........................"])