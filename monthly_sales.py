#5
import csv
from matplotlib import pyplot as plt
from datetime import datetime

dates=[]

with open('premium_logs.csv', 'r') as f:
    reader=csv.reader(f)

    for line in reader:
        if line[4]=='created_at':
            continue
        date=line[4].split(" ")[0]
        date=date.split("-")
        
        for i in range(len(date)):
            if i==0:
                year=date[i]
            elif i==1:  
                month=date[i] 
            elif i==2:
                day=date[i]
        date=day+'/'+month+'/'+year
        date_obj=datetime.strptime(date, "%d/%m/%Y").date()
        dates.append(date_obj)
    
    dates.sort()
    months={}

    for i in range(len(dates)):
        if dates[i].month not in months:
            months[dates[i].month]=1
        else:
            months[dates[i].month]+=1


x=['January', 'February', 'March', 'April', 'May', 'June', 'July']
y=[months[1], months[2], months[3], months[4], months[5], months[6], months[7]]
plt.title('Monthly Sales')
plt.grid(color='grey', linestyle='--', linewidth=1, axis='y')
plt.plot(x,y, color='black', linewidth=3)
plt.show()

   
        
       





