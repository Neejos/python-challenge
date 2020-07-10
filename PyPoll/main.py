import os
import csv
import math

input_path= os.path.join("Resources", "election_data.csv")

i=0
name_l=[]

voter_id_l=[]
candidates_l = []
key_l=[]
val_l=[]

with open(input_path) as datafile:
    csvreader = csv.reader(datafile, delimiter = ",")
    csvheader = next(csvreader)
     
 # loop through the rows nad count the no of row to give total no of vote
#Also place the value of the "candidates" column in a list(our_l)
    for row in csvreader:
        
        candidates_l.append(row[2])
        voter_id_l.append(row[0])
    dict={}
    for i in set(candidates_l):   #convert list to set to get the unique values
        dict.update({i:0})        #  each value in the set is converted to a dictionary so that the no of votes for each
                                  # candidate can be set to 0
            
    for i in candidates_l:       #  parse through row in the candidate list 
        dict[i] = dict[i] +1     # and  every time a value in the dict is found the corresponding vote value in th dict in increased by one
    print(dict)                 # unique candidate list and the corresponding total votes for each
    
   
key_l = list(dict.keys()) 
val_l = list(dict.values()) 
 

outfile=os.path.join("Analysis","ElectionResults.txt")

with open(outfile,"w") as data:
    data.writelines("       Election Analysis\n")
    data.writelines("--------------------------------------\n")
    data.writelines(f"Total Votes : {len(voter_id_l)}\n")
    data.writelines("--------------------------------------\n")
    print(f"Election Results")
    print(f"-------------------------")
    print(F"Total Votes : {(len(voter_id_l))}")
    print(f"-------------------------")
    for i in range(len(key_l)):
        a =key_l[i]
        b= round((float(val_l[i]/len(voter_id_l)))*100,2)
        c = val_l[i]

        print(f"{a} : {b}%   ({c})")
        data.writelines(f"{a} : {b}%   ({c})\n")
        
    for i in range(len(key_l)):
        if val_l[i] == max(val_l):
        
            print(f"-------------------------")            
            print(f"Winner : {key_l[i]}")
            data.writelines("-------------------------\n")
            data.writelines(f"Winner : {key_l[i]}")
          