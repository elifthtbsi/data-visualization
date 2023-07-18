#4

from matplotlib import pyplot as plt
import csv


google=0
apple=0

with open ('premium_logs.csv', 'r') as f:
    reader=csv.reader(f)

    for line in reader:
        store=line[8]

        if store=='google':
            google+=1
        elif store=='apple':
            apple+=1
        

labels=['Apple', 'Google']
slices=[apple, google]


plt.pie(slices, labels=labels, autopct='%1.1f%%', shadow=True, wedgeprops={'edgecolor':'black'})
plt.title("Mobile Sales")
plt.show()

