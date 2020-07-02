import os
import csv
import math
import statistics

input_path= os.path.join("Resources", "budget_data.csv")

i=0
our_l =[]
v_l=[]
date_l= []
print("       Financial Analysis")
print("--------------------------------------")

with open(input_path) as datafile:
    csvreader = csv.reader(datafile, delimiter = ",")
    csvheadear = next(csvreader)
    for row in csvreader:
       
        our_l.append(float(row[1])) #list of profit/losses
        date_l.append(row[0]) #list of months
    print("Total months: {}".format(len(date_l))) #Total no of months
    print(f"Total : $ {sum(our_l)}") # Sum of Profits/Losses
    



     #change in profit/loss  
for i in range(len(our_l)-1):
        v = our_l[i+1]-our_l[i]
        v_l.append(v)   # list of the change 
print("Average  Change : ${0:.2f}". format(statistics.mean(v_l))) #average of the change



for i in range(len(v_l)-1):
    if v_l[i] == max(v_l): #find the max change and its index value 'i' is used to find the corresponding value in the months list
        a= date_l[i+1]
        print("Greatest Increase in Profits: {0}   $({1:,.1f})".format(a,max(v_l)))
    elif v_l[i] == min(v_l): #find the min change and its index value 'i' is used to find the corresponding value in the months list
        b = date_l[i+1]
        print("Greatest Decrease in Profits: {0}   $({1:,.1f})".format(b,min(v_l)))
        
outfile=os.path.join("Analysis","analysis.txt")   #export to a text file

with open(outfile,"w") as data:
    data.writelines("       Financial Analysis\n")
    data.writelines("--------------------------------------\n")
    data.writelines("Total months: {}\n".format(len(date_l)))
    data.writelines(f"Total : $ {sum(our_l)}\n")
    data.writelines("Average  Change : ${0:.2f}\n". format(statistics.mean(v_l)))
    data.writelines("Greatest Increase in Profits: {0}   $({1:,.1f})\n".format(a,max(v_l)))
    data.writelines("Greatest Decrease in Profits: {0}   $({1:,.1f})\n".format(b,min(v_l)))
    
         
        
    

            
            
        
        