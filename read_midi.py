import py_midicsv
import pandas as pd
import os

# path = 'midi_solo/'
# files = []
# for r, d, f in os.walk(path):
# 	for file in f:
# 		if '.mid' in file:
# 			# print(file)
# 			files.append(os.path.join(r, file))

files = 'midi_solo/alb_esp1.mid'

midi_list = []

for file in files:
	midi = py_midicsv.midi_to_csv(str(file))
	for line in midi:
		str_line = [x.strip() for x in line.split(',')]
		if (str(str_line[2]) != 'Copyright_t'
		    and str(str_line[2]) != 'Text_t'):
			# print(str_line)
			midi_list.append(str_line)

midi_all = pd.DataFrame(midi_list)
midi_all.to_csv('midi_all.txt', sep=',', index=False, header=False)