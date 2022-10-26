import pandas as pd
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1
df = pd.read_csv(dir_path + '/input.txt', sep="\n", header=None)
df.rename(columns={0:'depth'}, inplace=True)

depth_diff = df['depth'].diff()

output = (depth_diff > 0).value_counts()[1]

# print(output)