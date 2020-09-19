import os
import csv
filepath = '../Resources/budget_data.csv'
csvfile = os.path.join('../Resources/budget_data.csv')

with open(filepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    
    csvreader = csv.reader(csvfile,  delimiter=',')

 
   

    # Read the header row first (skip this step if there is no header)

    header = next(csvreader)

    task = []
    Lista =[]
    Listb= []
    counter = 0
    
    difference =[]

   
# #   #count total number of votes    

    for row in csvreader:

        


    
       
       
        
        task.append(int(row[1]))

     
        total= sum(task)
        
        
        
        
# #    # The counter bumps all of the items in list a up by one

        if counter > 0 :

            Lista.append(int(row[1]))
        counter = counter + 1
           
            
        Listb.append(int(row[1]))

        
       
    zip_object = zip(Lista, Listb)


# #    # Calculates Delta by subtracting list B from a modified list a 

    for Lista_i, Listb_i in zip_object:

         difference.append(Lista_i-Listb_i)
        
# #    # Defines all teh components needed for print 

    Big=max(difference) 
    Small=min(difference)
    avg = sum (difference)
    s=sum(difference)/len(difference)
    length = (len(Listb))
    

print(f"Financial Analysis\n")
print(f"---------------------------------\n")
print(f"Total Months :{length}\n")
print(f"Total: {total}\n")
print(f"Average Change: {s}\n")
print(f"Greatest Increase in Profits: {Big}\n")
print(f"Greatest Decrease in Profits:{Small}")


# #   #Prints into a text file 

with open ("../Resources/budget_out.txt", "w") as textfile:
    textfile.write(
        f"Financial Analysis\n"
        f"---------------------------------\n"
        f"Total Months :{length}\n"
        f"Total: {total}\n"
        f"Average Change: {s}\n" 
        f"Greatest Increase in Profits: {Big}\n"
        f"Greatest Decrease in Profits:{Small}")















  
   
       


    # lines= len(list(task))
    # print(lines)
       
        #  print(lines)
    
        

        

         

     
         #print(row[1])
         
        

     

       
        
     

        
