import pandas as pd

df = pd.read_csv('discharge.csv')

while True:
    hadm_id = int(input())
    t = df[df['hadm_id'] == hadm_id]['text'].values[0]
    print(t)

