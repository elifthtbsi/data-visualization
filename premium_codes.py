
"""
toplam premium kod sayısı ve iki kez kullanılan premium kodları verir
"""

import csv

premiums_codes={}
codes=[]
number_of_uses=[]
two_times_used=[]

with open ('premium_logs.csv', 'r') as f:
    reader=csv.reader(f)

    for line in reader:
        code=line[3]
        if code!='--' and code!='premium_code_id':
            if code not in premiums_codes:
                premiums_codes[code]=1
            elif code in premiums_codes:
                premiums_codes[code]+=1
                two_times_used.append(code)
        
print("total number of premium codes:", len(premiums_codes))
print("2 times used codes:", two_times_used)