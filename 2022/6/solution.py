import pandas as pd
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1
with open(dir_path + '/input.txt') as file:
    stream = file.readline()

stream_list = list(stream)
solution = None
for idx, c in enumerate(stream_list):
    # If following three characters are different then break and return position as solution
    substream = [c, stream_list[idx+1], stream_list[idx+2], stream_list[idx+3]]
    if len(substream) == len(set(substream)):
        solution = idx + 4
        break

print(solution)