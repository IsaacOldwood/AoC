import pandas as pd
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1
df = pd.read_csv(dir_path + '/input.txt', sep="\n", header=None)
df.rename(columns={0:'depth'}, inplace=True)

depth_diff = df['depth'].diff()

output = (depth_diff > 0).value_counts()[1]

# print(output)

# Part 2
sliding_window = df['depth'].rolling(3)
sliding_mean = sliding_window.mean()

sliding_mean_diff = sliding_mean.diff()

output = (sliding_mean_diff > 0).value_counts()[1]

# print(output)