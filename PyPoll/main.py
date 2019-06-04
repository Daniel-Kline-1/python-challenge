import os
import csv
import pandas as pd

filepath = "election_data.csv"




electiondata = pd.read_csv(filepath)

totalvotenum = len(electiondata)

candidates = electiondata["Candidate"].unique()

#khanpercent = candidates["Khan"].value_counts()/ totalvotenum
#correypercent = candidates["Correy"].value_counts()/ totalvotenum 
#lipercent = candidates["Li"].value_counts()/ totalvotenum
#otoolpercent = candidates["O'Tooley"].value_counts()/ totalvotenum

khandata = electiondata.loc[electiondata["Candidate"] == "Khan",:]
correydata = electiondata.loc[electiondata["Candidate"] == "Correy",:]
lidata = electiondata.loc[electiondata["Candidate"] == "Li",:]
otooldata = electiondata.loc[electiondata["Candidate"] == "O'Tooley",:]
#print(candidates)
#print()
#print(khandata.head())
#print()
#print(correydata.head())
#print()
#print(lidata.head())
#print()
#print(otooldata.head())


khannumber = len(khandata)
correynumber = len(correydata)
linumber = len(lidata)
otoolnumber = len(otooldata)

khanpercent = len(khandata)*100/totalvotenum
correypercent = len(correydata)*100/totalvotenum
lipercent = len(lidata)*100/totalvotenum
otoolpercent = len(otooldata)*100/totalvotenum




if (khannumber > correynumber) & (khannumber > linumber) & (khannumber > otoolnumber):
    winner = "Khan"
elif (correynumber>khannumber) & (correynumber>linumber) & (correynumber>otoolnumber):
    winner = "Correy"
elif (linumber>khannumber) & (linumber>correynumber )& (linumber>otoolnumber):
    winner = "Li"
elif (otoolnumber>khannumber) & (otoolnumber>correynumber) & (otoolnumber>linumber):
    winner = "O'Tooley"






print()
print("Election Results \n")
print("----------------")
print("Total Votes: " + str(totalvotenum) )

#print(candidates)
#print()
#print(khandata.head())
#print()
#print(correydata.head())
#print()
#print(lidata.head())
#print()
#print(otooldata.head())
print("---------------")
print("Khan: " + str(khanpercent)+"%"+ " ("+str(khannumber)+")")
print("Correy: "+ str(correypercent)+"% ("+str(correynumber)+")")
print("Li: " + str(lipercent)+"% ("+str(linumber)+")")
print("O'Tooley: "+ str(otoolpercent)+"% ("+str(otoolnumber)+")")
print("-----------------")
print("Winner: " + winner)
print("--------------------")

savefile = open("election_data.txt",'w')

savefile.write("Election Results \n")
savefile.write("------------------------- \n")
savefile.write("\nTotal Votes: " + str(totalvotenum) )
savefile.write("\n -------------------------------")
savefile.write("\nKhan: " + str(khanpercent)+"%"+ " ("+str(khannumber)+")")
savefile.write("\nCorrey: "+ str(correypercent)+"% ("+str(correynumber)+")")
savefile.write("\nLi: " + str(lipercent)+"% ("+str(linumber)+")")
savefile.write("\nO'Tooley: "+ str(otoolpercent)+"% ("+str(otoolnumber)+")")
savefile.write("\n----------------------")
savefile.write("\nWinner: " + winner)
savefile.write("\n----------------------")
savefile.close()