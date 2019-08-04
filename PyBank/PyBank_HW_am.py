import os 
import csv 

#open csv #Read and delimit the data

pybank_csv = os.path.join("Homework/Instructions/PyBank/Resources/budget_data.csv")

with open(pybank_csv,newline="") as pybank_file:
    csvreader=csv.reader(pybank_file, delimiter=',')
    
#Initialize Variable
    months=0
    prof_loss=0

    # Counts the Total Rows
    rows=[r for r in csvreader]

    #Defaulting to the First Value available in the Sheet
    change_prof_loss=int(rows[1][1])
    max = rows[1]
    min=rows[1]
    
    #Looping through Data

    for i in range(1,len(rows)):
        
        months=months+1
        row=rows[i]
        prof_loss= int(row[1]) + prof_loss
        
        #Excluding the Header Row
        if i > 1:
            chage_prof_loss=change_prof_loss + int(row[1])-int(rows[i-1][1])
        #Finding and Max Profits/Losses
        if int(max[1]) < int(row[1]):
            max=row
        #Finding and Min Profits/Losses
        if int(min[1]) > int(row[1]):
            min=row

#Calculating Average and Average Change in Profits/Loss
average= int(prof_loss /months)
average_change_prof_loss=int(change_prof_loss/months)

#Printing the Outputs
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(months))
print("Total: " +"$" +str(prof_loss))       
print("Average Change: " +"$"+ str(average))
print("Greatest Increase in Profits:" + str(max[0])+" ($" + str(max[1])+")")
print("Greatest Decrease in Profits:" + str(min[0])+" ($" + str(min[1])+")")


# Print to a file
PyBank_Output = os.path.join("/Users/alexandermiller/WUSTL201907DATA2/03-Python/Homework/Instructions/PyBank/PyBank_Out_csv")
with open(PyBank_Output, 'w', newline="") as PyBankOutput_file:
    # Initialize csv.writer
    csvwriter = csv.writer(PyBank_Output_file, delimiter=',')
    # First Row
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow(['Total Months:', total_months])
    csvwriter.writerow(['Total:', total_money])
    csvwriter.writerow(['Average Change:', average_change])
    csvwriter.writerow(['Greatest Increase in Profits:', max_date, greatest_increase])
    csvwriter.writerow(['Greatest Decrease in Profits:', min_date, greatest_decrease])
​
# convert variables to string for txt file
total_months_str = str(total_months)
total_money_str = str(total_money)
average_change_str = str(average_change)
max_date_str = str(max_date)
min_date_str = str(min_date)
greatest_increase_str = str(greatest_increase)
greatest_decrease_str = str(greatest_decrease)
​
​
​
# Print to a txt file
f= open("PyBankOutput.txt","w+")
​
f.write('Finaancial Analysis\n')
f.write('Total Months:' + total_months_str + '\n')
f.write('Total:' + total_money_str + '\n')
f.write('Average Change:' + average_change_str + '\n')
f.write('Greatest Increase in Profits:' + max_date_str + greatest_increase_str + '\n')
f.write('Greatest Decrease in Profits:' + min_date_str + greatest_decrease_str + '\n')
​
​
f.close()