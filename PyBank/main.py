#importing modules
    import os
    import csv
#reading csvfile
    csvpath = os.path.join('Resources', 'budget_data.csv')
    with open(csvpath,'r') as csvfile:
        csv_reader=csv.reader(csvfile)
    #storing header row
        header = next(csv_reader)
    #converting csvfile's data into list
        date_list=[]
        profit_losses_list = []
        for row in csv_reader:
            date = str(row[0])
            profit_losses = int(row[1])
            date_list.append(date)
            profit_losses_list.append(profit_losses)
    #finding the total number of months and net profits/losses
        total_months = len(date_list)
        total_amount = sum(profit_losses_list)
    #calculating the average change
        changes = [profit_losses_list[i+1] - profit_losses_list[i] for i in range(len(profit_losses_list)-1)]
        average_profit_losses_changes = sum(changes)/len(changes)
    #finding the months with the greatest increased and decreased profits
        greatest_increase = max(changes)
        greatest_decrease = min(changes)
        greatest_increase_date = date_list[changes.index(greatest_increase)+1]
        greatest_decrease_date = date_list[changes.index(greatest_decrease)+1]
#converting variables to string for printing 
    analysis = f'''
        Financial Analysis
        .................................
        Total Months: {total_months}
        Total: ${total_amount}
        Average Change: ${round(average_profit_losses_changes,2)}
        Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})
        Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})
        '''
#printing financial analysis in terminal
    print(analysis)
#creating new txtfile for exporting financial analysis
    new_path = os.path.join ('Analysis', 'Financial Analysis.txt')
    with open (new_path,'w',newline='') as txtfile:
        txtfile.write(analysis)
    
    
