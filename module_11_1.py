import requests as req
import pandas as pd
import numpy as np

#request the random

THE_URL = 'https://www.random.org/integers/?num=20&min=1&max=20&col=1&base=10&format=plain&rnd=new'
response = req.get(THE_URL).text.split('\n')
print(response)

#make a csv
with open('module_11_1.csv', 'w', newline='\n') as f:
    writer = pd.DataFrame(response).to_csv(f, header=False, index=False)

#read the csv, multiplay it by 5
print((np.genfromtxt('module_11_1.csv', delimiter=',', max_rows=5)) * 5)
