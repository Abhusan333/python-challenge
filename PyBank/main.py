import csv 
import os
 
files_to_load = os.path.join("Resources","budget_data.csv")
output_files = os.path.join("Analysis","budget_analysis.txt")
total_month_count = 0
month_change = []
net_change_list = []
increase_great = ["",0]
decrease_great = ["",300000000000]
net_total = 0
with open(files_to_load) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)
    first_datarow = next(reader)  # Jan-2010,867884
    total_month_count = total_month_count + 1
    net_total = int(first_datarow[1])
    previous_net = int(first_datarow[1]) # 867884

    for datarow in reader:
        total_month_count = total_month_count + 1 
        net_total = net_total + int(datarow[1])
        month_change.append(datarow[0])
        net_change = int(datarow[1]) - previous_net #322013 - 984655
        net_change_list.append(net_change) # [2000,3245]
        previous_net = int(datarow[1]) #322013

        #calculate_greatest_increase
        if net_change > increase_great[1]:
            increase_great[0] = datarow[0]
            increase_great[1] = net_change
            #[june 2010, 379920] 

        #greatest_decrease
        if net_change < decrease_great[1]:
            decrease_great[0] = datarow[0]
            decrease_great[1] = net_change 
            
Avg_net_change = sum(net_change_list)/len(net_change_list)
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)



output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_month_count}\n"
    f"Total: ${net_total}\n"
    f"Average  Change: ${Avg_net_change:.2f}\n"
    f"Greatest Increase in Profits: {increase_great[0]} (${increase_great[1]})\n"
    f"Greatest Decrease in Profits: {decrease_great[0]} (${decrease_great[1]})\n")

with open(output_files,"w") as output_view:
    output_view.write(output)

print (output)
    

    # print (net_total)
    # print (total_month_count)
    # print (net_total/total_month_count)

    
             
         