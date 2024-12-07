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
print(f"Part 1 answer: {total_diff=}")

# Part 2
# Set the default count to 0
df["count"] = 0
# Get the unique ids
unique_ids = df[0].unique()

# Count occurrences
for i in unique_ids:
    count = df.loc[df[1] == i].shape[0]
    df.loc[df[0] == i, "count"] = count

# Calculate the similarity
df["sim"] = df[0] * df["count"]

# Calculate the total similarity
total_sim = df["sim"].sum()
print(f"Part 2 answer: {total_sim=}")
