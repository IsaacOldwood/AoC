import pandas as pd
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1
# Read input data
df = pd.read_csv(dir_path + "/input.txt", sep="   ", header=None, engine="python")

# Sort
df = df.sort_values(by=[0]).reset_index(drop=True)
df[1] = df.sort_values(by=[1])[1].reset_index(drop=True)

# Calculate the difference
df["diff"] = (df[1] - df[0]).abs()

# Total difference
total_diff = df["diff"].sum()
print(total_diff)