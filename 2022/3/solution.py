import pandas as pd
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1
df = pd.read_fwf(dir_path + '/input.txt', header=None, dtype=str)
df.rename(columns={0:'rucksack'}, inplace=True)

df['comp1'] = df['rucksack'].apply(lambda text: text[:len(text)//2])
df['comp2'] = df['rucksack'].apply(lambda text: text[len(text)//2:])

df['comp_shared'] = df[['comp1', 'comp2']].apply(lambda x: ''.join(set(x["comp1"]).intersection(set(x["comp2"]))), axis=1)

df['comp_shared_num'] = df['comp_shared'].apply(lambda t: sum([(ord(char) - 96) if char.islower() else (ord(char) - 63 + 25) for char in t]))

print(df['comp_shared_num'].sum())