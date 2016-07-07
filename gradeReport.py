# Standard Grade Report
#
# ----------------------------------------------------------------------------------
#
# Assignments:		% (100 / n * %):    Points:		Weighted:		
# ----------------------------------------------------------------------------------
# Assignment_Group_1    Percentage_n        Earned / Total      Percentage * Points
# Assignment_Group_2    Percentage_n        Earned / Total      Percentage * Points
# Assignment_Group_3    Percentage_n        Earned / Total      Percentage * Points
# ...                   ...                 ...                 ...
# Assignment_Group_n    Percentage_n        Earned / Total      Percentage * Points
# ----------------------------------------------------------------------------------
# Total (n) 		100%		    552/600		Total Weighted %
#
# ----------------------------------------------------------------------------------
#
# Weighted Score:	__TW%__
#
# Letter Grade:		__LG__
#
# "Comment Based on Letter Grade"
#
# ---------------------------- EOF -------------------------------------------------
#
# */

from __future__ import print_function
import time, math, os, datetime

print("\nWhich class is this Grade Report for?:")
classTitle = (raw_input())
os.system('clear')

print("\n=============================="
      "\nGrade Report for",classTitle,
      "\n==============================")

print("\nHow many Assignment types? :")
totalAssignments = (raw_input())
os.system('clear')

if totalAssignments.isdigit():
    n = int(totalAssignments)
    totalTotal = 0
    totalEarned = 0
    totalWeighted = 0
    totalPercentage = 0
    printAll = []
    print("\n=============================="
          "\nGrade Report for",classTitle,
          "\n==============================\n")
    for i in range(0, n):
        print("Assignment :")
        print((i+1),"/",n)
        print("\nTitle")
        assignTitle = (raw_input())
        print("\nPercentage")
        assignPercentage = int(raw_input())
        print("")
        print("Points Earned")
        assignEarned = float(raw_input())
        print("Points Total")
        assignTotal = float(raw_input())
        assignRaw = (assignEarned / assignTotal)
        assignWeighted = (assignRaw * assignPercentage)
        totalPercentage += assignPercentage
        totalTotal += assignTotal
        totalEarned += assignEarned
        totalWeighted += assignWeighted
        print("\nAssignement\tPercentage\tPoints\t\tWeighted")
        points = assignEarned / assignTotal
        printStatement = (assignTitle, assignPercentage, assignEarned, "/", assignTotal, assignWeighted)
        os.system('clear')
        print("\n=============================="
              "\nGrade Report for",classTitle,
              "\n==============================\n")
    date = datetime.date.today().strftime("%B %d %Y")
    print(date,": Final Weighted Score\n")
    int(totalWeighted)
    if 0 < totalWeighted < 70:
        print(totalWeighted,": NR\n\nGive up...")
    elif 70 <= totalWeighted < 80:
        print(totalWeighted, ": C\n\nCs get Degrees ;)")
    elif 80 <= totalWeighted < 90:
        print(totalWeighted, ": B\n\nMaintain...")
    elif 90 <= totalWeighted:
        print(totalWeighted, ": A\n\nOutstanding!")

print("\n========= End of File ========\n")

