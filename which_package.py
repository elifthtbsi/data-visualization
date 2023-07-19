#2

from matplotlib import pyplot as plt
import numpy as np
import csv

packets={}

with open ('premium_logs.csv', 'r') as f:
    reader=csv.reader(f)
    
    for line in reader:
        option_id=line[2]
        if option_id!='pricing_option_id' and option_id not in packets:
            packets[option_id]=1
        elif option_id in packets:
            packets[option_id]+=1



plt.title('Package Sales')
packages=['Life time', 'Lite', 'Weekly', 'Yearly', 'Others']
how_many=[packets['life_time'], packets['lite'], packets['weekly'], packets['yearly'], packets['--']]
plt.grid(color='grey', linestyle='--', linewidth=1, axis='y')

plt.bar(packages, how_many)
plt.yticks(np.arange(0, max(how_many)+10 ,40))
plt.show()













