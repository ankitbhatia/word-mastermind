import csv
import glob
import pandas as pd

files = glob.glob("data/*.txt")

names = {}

for file in files:
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            name = row[0]
            sex = row[1]
            number = row[2]
            if name not in names.keys():
                names[name] = {}
                names[name]['freq'] = number
                names[name]['sex'] = sex
                names[name]['count'] = len(name)
            else:
                names[name]['freq'] += number


df = pd.DataFrame.from_dict(names, orient='index')

with open("dict/names",'w') as f:
    for v in df[df['count']==5].index.values:
        f.write(v + '\n')
           




        

