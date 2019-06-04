import os
import csv
import pandas as pd

filepath = "budget_data.csv"

print("Financial Analysis")
print()
print("----------------------")
print()
budgetdata = pd.read_csv(filepath)
#print()
#print(budgetdata.head())


monthcount = len(budgetdata["Date"].unique())
#print()
print("Total Months : " + str(monthcount))

totalprofit = int(budgetdata["Profit/Losses"].sum())
#print()
print("Total: " + str(totalprofit))

n = len(budgetdata)
#print()
#print(n)

average = int(budgetdata["Profit/Losses"].sum()) / n
#print()
print("Average Change: " + str(average))

besttoworse = budgetdata.sort_values(["Profit/Losses"], ascending = False)
#print()
#print(besttoworse.head())

bestprofit = besttoworse.iloc[0,:]
print()
print("Greatest Increase in Profit: " + str(bestprofit) )

worstprofit = besttoworse.iloc[n-1,:]

print()
print("Greatest Decrease in Profit" + str(worstprofit))

savefile = open("budgetdata.txt",'w')

savefile.write("Financial Analysis \n")
savefile.write("---------------------- \n")
savefile.write("\n Total Months : " + str(monthcount))
savefile.write("\n Total: " + str(totalprofit))
savefile.write("\n Average Change: " + str(average))
savefile.write("\n Greatest Increase in Profit: " + str(bestprofit))
savefile.write("\n Greatest Decrease in Profit" + str(worstprofit))
savefile.close()