import pandas as pd
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1
df = pd.read_fwf(dir_path + '/input.txt', header=None, dtype=str)
df.rename(columns={0:'ranges'}, inplace=True)

df[['range1', 'range2']] = df['ranges'].str.split(',', expand=True)
df[['range1_start', 'range1_end']] = df['range1'].str.split('-', expand=True)
df[['range2_start', 'range2_end']] = df['range2'].str.split('-', expand=True)

df['range1_set'] = [set(range(int(i), int(j)+1)) for i, j in df[['range1_start', 'range1_end']].values]
df['range2_set'] = [set(range(int(i), int(j)+1)) for i, j in df[['range2_start', 'range2_end']].values]

df['subset_1'] = df[['range1_set', 'range2_set']].apply(lambda x: set(x["range1_set"]).issubset(set(x["range2_set"])), axis=1)
df['subset_2'] = df[['range1_set', 'range2_set']].apply(lambda x: set(x["range2_set"]).issubset(set(x["range1_set"])), axis=1)

subsets = df[['subset_1', 'subset_2']].value_counts()

#print(subsets.sum() - (subsets.loc[subsets.index == (False, False)]).sum())

# Part 2
df['subset_1'] = df[['range1_set', 'range2_set']].apply(lambda x: len(set(x["range1_set"]).intersection(set(x["range2_set"]))) > 0, axis=1)
df['subset_2'] = df[['range1_set', 'range2_set']].apply(lambda x: len(set(x["range2_set"]).intersection(set(x["range1_set"]))) > 0, axis=1)

subsets = df[['subset_1', 'subset_2']].value_counts()

print(subsets.sum() - (subsets.loc[subsets.index == (False, False)]).sum())