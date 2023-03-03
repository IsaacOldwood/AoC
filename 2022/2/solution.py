import pandas as pd
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1
df = pd.read_fwf(dir_path + '/input.txt', header=None, dtype=str)
df.rename(columns={0:'op',1:'me'}, inplace=True)

# Debugging
df.replace('A', 'Rock', inplace=True)
df.replace('B', 'Paper', inplace=True)
df.replace('C', 'Scissors', inplace=True)
df.replace('X', 'Rock', inplace=True)
df.replace('Y', 'Paper', inplace=True)
df.replace('Z', 'Scissors', inplace=True)

df['score_1'] = 1
df.loc[df['me'] == 'Paper','score_1'] = 2
df.loc[df['me'] == 'Scissors','score_1'] = 3

# Lost
df['score_2'] = 0
# Draw
df.loc[df['me'] == df['op'],'score_2'] = 3
# Win
df.loc[
    ((df['me'] == 'Rock') & (df['op'] == 'Scissors')) |
    ((df['me'] == 'Paper') & (df['op'] == 'Rock')) |
    ((df['me'] == 'Scissors') & (df['op'] == 'Paper'))
    ,'score_2'] = 6

total = df[['score_1', 'score_2']].sum().sum()
print(total)