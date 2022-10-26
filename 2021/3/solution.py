import pandas as pd
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1
df = pd.read_csv(dir_path + '/input.txt', sep="\n", header=None, dtype=str)
df.rename(columns={0:'report'}, inplace=True)
df = df['report'].str.split('', expand=True)
df.drop(columns=[0, 13], inplace=True)

most_common_df = df.mode()
combined_df = most_common_df.agg(''.join, axis=1)

gamma_binary = combined_df[0]
epsilon_binary = gamma_binary.replace('0','2').replace('1','0').replace('2','1')

gamma_decimal = int(gamma_binary, 2)
epsilon_decimal = int(epsilon_binary, 2)

print(gamma_decimal * epsilon_decimal)