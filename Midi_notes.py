from mido import MidiFile as mid
import py_midicsv
import pandas as pd
import os

class Midi_convert:

	def __init__(self, midi_path, text_file):
		self.midi_path = midi_path
		self.text_file = text_file
		self.timer = 240
		self.timer_min = 15
		self.chr_add = 33
		midi_csv = py_midicsv.midi_to_csv(self.midi_path)
		midi_list = []
		for line in midi_csv:
			str_line = [x.strip() for x in line.split(',')]
			if str(str_line[2]) == 'Note_on_c':
				str_line = str_line[1:2] + str_line[4:5]
				str_line[1] = chr(33 + int(str_line[1]))
				midi_list.append(str_line)
		for i in range(len(midi_list) - 1):
			diff = abs(int(midi_list[i][0]) - int(midi_list[i + 1][0]))
			if diff < self.timer and diff != 0 and diff > self.timer_min:
				self.timer = diff

# def midi_timing(self):
# 		midi_csv = py_midicsv.midi_to_csv(self.midi_path)
# 		midi_list = []
# 		for line in midi_csv:
# 			str_line = [x.strip() for x in line.split(',')]
# 			if str(str_line[2]) == 'Note_on_c':
# 				str_line = str_line[1:2]+str_line[4:5]
# 				str_line[1] = chr(33 + int(str_line[1]))
# 				midi_list.append(str_line)
# 		for i in range(len(midi_list)-1):
# 			diff = abs(int(midi_list[i][0]) - int(midi_list[i + 1][0]))
# 			if diff < self.timer and diff != 0 and diff > self.timer_min:
# 				self.timer = diff

	def midi_to_string(self):
		midi_csv = py_midicsv.midi_to_csv(self.midi_path)
		midi_list = []
		for line in midi_csv:
			str_line = [x.strip() for x in line.split(',')]
			if str(str_line[2]) == 'Note_on_c':
				str_line = str_line[1:2]+str_line[4:5]
				str_line[1] = chr(int(self.chr_add) + int(str_line[1]))
				midi_list.append(str_line)
		str_out = ''
		time = 0
		for line in midi_list:
			if int(line[0]) == self.timer:
				str_out += str(line[1])
			else:
				num_spaces = int(line[0]) - time
				str_out += ' '*int(num_spaces/(int(self.timer)))
				str_out += str(line[1])
			time = int(line[0])
		return str_out

	def str_to_midi(self):
		midi_csv = []
		with open(self.text_file, 'r') as file:
			text = file.read()
		for i in text:
			midi_csv.append()



path = 'midi_solo/'
files = []
for r, d, f in os.walk(path):
	for file in f:
		if '.mid' in file:
			# print(file)
			files.append(os.path.join(r, file))

str_out = ''
for file in files:
	str_out += midi_to_string(file)

print(len(str_out))

output = open('input.txt', 'w')
output.write(str_out)
output.close()










# midifile = mid(midi_path)
#
# midi_list = []
#
# for i, track in enumerate(midifile.tracks):
# 	if track.name == 'Piano right':
# 		print('Track {}: {}'.format(i, track.name))
# 		for msg in track:
# 			if str(msg)[:4] == 'note':
#
# 				midi_list.append(str(msg).replace('note_on channel=0 ', '').replace('note=', '').replace('velocity=', '', ) .split(' '))
# 	if track.name == 'Piano left':
# 		print('Track {}: {}'.format(i, track.name))
# 		for msg in track:
# 			if str(msg)[:4] == 'note':
# 				midi_list.append(str(msg).split(' '))
#
#
#
# pd.DataFrame(midi_list).to_csv('test_output.csv', header=False, index=False)