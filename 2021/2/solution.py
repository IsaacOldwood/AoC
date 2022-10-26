import pandas as pd
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1
df = pd.read_csv(dir_path + '/input.txt', sep="\n", header=None)
df.rename(columns={0:'command'}, inplace=True)
df = df['command'].str.split(' ', expand=True)
df.rename(columns={0:'direction', 1:'magnitude'}, inplace=True)
df['magnitude'] = df['magnitude'].astype(int)

df.loc[df['direction'] == 'up', 'magnitude'] = df.loc[df['direction'] == 'up', 'magnitude'] * -1

up_down_total = df.loc[df['direction'].isin(['up', 'down']), 'magnitude'].sum()
forward_total = df.loc[df['direction'] == 'forward', 'magnitude'].sum()

# print(up_down_total * forward_total)

# Part 2
df['aim'] = df.loc[df['direction'].isin(['up', 'down']), 'magnitude'].cumsum()
df['aim'].ffill(inplace=True)
df.loc[0, 'aim'] = 0

df['depth'] = df.loc[df['direction'] == 'forward', 'magnitude'] * df.loc[df['direction'] == 'forward', 'aim']
df['depth'].fillna(0, inplace=True)

depth_total = df['depth'].astype(int).sum()

# print(forward_total * depth_total)