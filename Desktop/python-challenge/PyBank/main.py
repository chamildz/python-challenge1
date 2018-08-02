import csv
import os

csv_file_path = os.path.join("Resources","budget_data.csv")

print(csv_file_path)

numberOfMonths = 0
totalAmountOfProfitLoss = 0
averageChangeInProfitLoss=0
greatestIncreaseInProfits=0
greatestDecreaseInProfits =0
greatestIncreaseMonthYear = ""
greatestDecreaseMonthYear = ""

with open(csv_file_path,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)
    next(csvfile)

    for row in csvreader:
        numberOfMonths += 1
        #Calculate Total
        totalAmountOfProfitLoss += int(row[1])
        #Finding the greatet increae in profit
        if greatestIncreaseInProfits<int(row[1]):
            greatestIncreaseInProfits=int(row[1])
            greatestIncreaseMonthYear = row[0]
        #Finding the greatest decrease in profit
        if greatestDecreaseInProfits>int(row[1]):
            greatestDecreaseInProfits = int(row[1])
            greatestDecreaseMonthYear = row[0]

averageChangeInProfitLoss = round(totalAmountOfProfitLoss/numberOfMonths,2)

#Build the summary message
summaryMessage = f"Financial Analysis \n"
summaryMessage +=f"---------------------\n"
summaryMessage+=f"Total Months : {numberOfMonths}\n"
summaryMessage+=f"Total : ${totalAmountOfProfitLoss}\n"
summaryMessage+=f"Average Change : ${averageChangeInProfitLoss}\n"
summaryMessage+=f"Greatest Increase in Profits: {greatestIncreaseMonthYear} $({greatestIncreaseInProfits})\n"
summaryMessage+=f"Greatest Decrease in Profits: {greatestDecreaseMonthYear} $({greatestDecreaseInProfits})\n"

print(summaryMessage)



