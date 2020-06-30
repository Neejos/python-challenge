import os
import csv
import math

input_path= os.path.join("Resources", "budget_data.csv")

count = 0
total=0
i=0
r=0
our_l =[]
v_l=[]
with open(input_path) as datafile:
    csvreader = csv.reader(datafile, delimiter = ",")
    csvheadear = next(csvreader)
    for row in csvreader:
        # no of months
        count= count +1
        # Sum of Profits
        total = float(total) + float(row[1])
        our_l.append(float(row[1]))
        
    
for i in range(len(our_l)-1):
        v = our_l[i+1]-our_l[i]
        v_l.append(v)
for i in range(len(v_l)-1):
    if v_l[i+1] > v_l[i]:
         g = v_l[i+1]
        
    else:
         g =v_l[i]
        


for position,item in enumerate(v_l):
    if item == max(v_l):
        a=position
    if item ==min(v_l):
        b=position
    
    
with open(input_path) as datafile:
    csvreader = csv.reader(datafile, delimiter = ",")
    csvheadear = next(csvreader)
            
    for position1,item1 in enumerate(csvreader):
        if position1 == a+1:
            c=item1[0]
            
        if position1 == b-1:
            d=item1[0]
           
    print("Total months: {}".format(count))
print(f"Total : $ {sum(our_l)}")
print(f"Average  Change : ${round((sum(v_l) / len(v_l)),2)}")
print(f"Greatest Increase in Profits: ${c}  {max(v_l)}")
print(f"Greatest Decrease in Profits: ${d}  {min(v_l)}")
