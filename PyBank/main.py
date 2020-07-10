import os
import csv
import math
import statistics

input_path= os.path.join("Resources", "budget_data.csv")


i=0
our_l =[]
v_l=[]
date_l= []


with open(input_path) as datafile:
    csvreader = csv.reader(datafile, delimiter = ",")
    csvheadear = next(csvreader)
    for row in csvreader:
        
        our_l.append(float(row[1])) #list of profit/losses
        date_l.append(row[0]) #list of months
    
    
      #change in profit/loss  
for i in range(len(our_l)-1):
        v = our_l[i+1]-our_l[i]
        v_l.append(v)   # list of the change 


for i in range(len(v_l)-1):
    if v_l[i] == max(v_l): #find the max change and its index value 'i' is used to find the corresponding value in the months list
        a = date_l[i+1]
       
    elif v_l[i] == min(v_l): #find the min change and its index value 'i' is used to find the corresponding value in the months list
        b = date_l[i+1]
       

final_str=f'''      Financial Analysis
--------------------------------------
Total months: {len(date_l)}                
Total : $ {sum(our_l)}
Average Change : $ {round(sum(v_l)/len(v_l),2)}
Greatest Increase in Profits: {a}   $({max(v_l)})
Greatest Decrease in Profits: {b}   $({min(v_l)})'''

        
print(final_str)
        
outfile=os.path.join("Analysis","analysis.txt")   #export to a text file

with open(outfile,"w") as data:
    data.writelines(final_str)
  
         
        
    

            
            
        
        