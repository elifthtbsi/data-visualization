#1
from matplotlib import pyplot as plt
import numpy as np
import csv

providers={'web':0, 'mobil':{'apple':0, 'google':0}}

with open('premium_logs.csv', 'r') as f:
    reader=csv.reader(f)

    for line in reader:
        provider=line[8]

        if provider=='--':
            providers['web']+=1

        elif provider=='apple':
            providers['mobil']['apple']+=1
        
        elif provider=='google':
            providers['mobil']['google']+=1

plt.title('Which Provider')
provider = ['Web', 'Apple', 'Google']
sales = [providers['web'], providers['mobil']['apple'], providers['mobil']['google']]
plt.grid(color='grey', linestyle='--', linewidth=1, axis='y')

plt.bar(provider, sales)
plt.yticks(np.arange(0, max(sales), 40))
plt.show()

