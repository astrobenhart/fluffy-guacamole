import py_midicsv
import pandas as pd

file = py_midicsv.midi_to_csv('accustomed.mid')

midi_list = []
for line in file:
    str_line = [x.strip() for x in line.split(',')]
    midi_list.append(str_line)


midi = pd.DataFrame(midi_list)

for i in midi[2].unique():
    print(i)

# print(midi)