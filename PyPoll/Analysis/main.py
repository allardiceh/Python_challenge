import os
import csv

filepath = '/Users/heatherallardice/Desktop/personal-data/Python_challenge/PyPoll/Resources/election_data.csv'
csvfile = os.path.join('/Users/heatherallardice/Desktop/personal-data/Python_challenge/PyPoll/Resources/election_data.csv')

# Counting total number of votes
with open(filepath) as csvfile:
# #     # CSV reader specifies delimiter and variable that holds contents
    
    csvreader = csv.reader(csvfile,  delimiter=',')
# #     # Read the header row first (skip this step if there is no header)

    header = next(csvreader)
# #    # Allows count of total votes cast 
    count = (1)   
    count=sum(1 for row in csvfile)
# #    # Empty list so that I can later add percent values    
    div=[]


with open(filepath) as csvfile:

# #     # CSV reader specifies delimiter and variable that holds contents 
    
# #     #csvreader = csv.reader(csvfile,  delimiter=',')
    
   
    result = {}      
    rd = csv.DictReader(csvfile, delimiter=',')
# #    # Dictonary that enables to call unique candidates and associated values. Calls teh keys by "candidate"
    for k in rd: 
        if 'Candidate' in k: 
            result[k['Candidate']] = result.get(k['Candidate'], 0) + 1 
        
# #    # Creates lists out of keys, one for candiate names and on for values. Once values is retrieved you can write a for loop to calculate percent 

    L=list(result.keys())
    
    
    V=list(result.values())
    
    
    for values in V:
        div.append ((round(((values)/ (count))* 100)))

# #   # Indexes a list based off the values in another list 

    best = max(V)
    index = V.index(best)
    Winner= L[index]


print("Election Results\n")
print("-------------------------\n")
print(f'Total Votes: {count}\n')
print("-------------------------\n")
print(f'{L[0]}: ({V[0]}) {div[0]} %\n')
print(f'{L[1]}: ({V[1]}) {div[1]} %\n')
print(f'{L[2]}: ({V[2]}) {div[2]} %\n')
print(f'{L[3]}: ({V[3]}) {div[3]} %\n')
print("-------------------------\n")
print(f'Winner: {Winner}\n')
print("-------------------------") 


# #    # Print to text file. Before attempting you need to remove "print"
with open ("../Resources/election_out.txt", "w") as textfile:
    textfile.write(
"Election Results\n"
"-------------------------\n"
f'Total Votes: {count}\n'
"-------------------------\n"
f'{L[0]}: ({V[0]}) {div[0]} %\n'
f'{L[1]}: ({V[1]}) {div[1]} %\n'
f'{L[2]}: ({V[2]}) {div[2]} %\n'
f'{L[3]}: ({V[3]}) {div[3]} %\n'
"-------------------------\n"
f'Winner: {Winner}\n'
"-------------------------") 
    



        

        




    





