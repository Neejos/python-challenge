import os
import csv

input_path= os.path.join("Resources", "election_data.csv")


count=0
i=0

our_l=[]
candidates_l = []

with open(input_path) as datafile:
    csvreader = csv.reader(datafile, delimiter = ",")
    csvheader = next(csvreader)
     
 # loop through the rows nad count the no of row to give total no of vote
#Also place the value of the "candidates" column in a list(our_l)
    for row in csvreader:
        count=count+1
        our_l.append(row[2])
        
print("Election Results")
print("-------------------------")
print(F"Total Votes : {count}")
print("-------------------------")

# loop through the names column list(our_l) and if the two adjacent value are not the same and if that first value is not in the candidates_l
#which is empty to start with,then the first compared value is appended to the candidates_l.
for i in range(count-1):
    if our_l[i+1]!=our_l[i] and our_l[i] not in candidates_l:
            candidates_l.append(our_l[i])
            
#  each value in candidates_l is compared to every value in the our_l and variable 'c' holds the no of times
#they are the same,which in turn shows the total votes per candidate
# variable b holds the candidate name
# variable a hold the percentage of votes per candidate
for j in range(len( candidates_l)):
    c = 0
    for i in range(count-1):
        if candidates_l[j] == our_l[i]:
           c = c+1
    b= candidates_l[j]
    a = (c/count)*100
    print("{} : {}% ({})".format(b,round(a,2),c))
        
          