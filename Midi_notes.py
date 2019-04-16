from mido import MidiFile as mid
import py_midicsv
import pandas as pd
import os
import sys
import subprocess

class Midi_convert:

	def __init__(self, midi_path):
		self.midi_path = midi_path
		self.timer = 240
		self.timer_min = 15
		self.chr_add = 33
		self.str_out = ''
		self.time = 0
		self.output_text = 'intput.txt'
		self.data_dir = 'RNN/data'
		if type(self.midi_path) == list:
			midi_list = []
			for file in self.midi_path:
				print(str(file))
				try:
					midi_csv = py_midicsv.midi_to_csv(file)
				except:
					sys.exit('could not find midi file: '+str(self.midi_path))
				for line in midi_csv:
					str_line = [x.strip() for x in line.split(',')]
					if str(str_line[2]) == 'Note_on_c':
						str_line = str_line[1:2] + str_line[4:5]
						str_line[1] = chr(33 + int(str_line[1]))
						midi_list.append(str_line)
						self.midi_list = midi_list
			for i in range(len(midi_list) - 1):
				diff = abs(int(midi_list[i][0]) - int(midi_list[i + 1][0]))
				if diff < self.timer and diff != 0 and diff > self.timer_min:
					self.timer = diff

		elif type(midi_path) == str:
			try:
				midi_csv = py_midicsv.midi_to_csv(self.midi_path)
			except:
				sys.exit('could not find midi file: '+str(self.midi_path))
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

	def midi_to_string(self):
		if type(self.midi_path) == list:
			# for file in self.midi_path:
			# 	print(str(file))
			# 	midi_csv = py_midicsv.midi_to_csv(file)
			# 	midi_list = []
			# 	for line in midi_csv:
			# 		str_line = [x.strip() for x in line.split(',')]
			# 		if str(str_line[2]) == 'Note_on_c':
			# 			str_line = str_line[1:2] + str_line[4:5]
			# 			str_line[1] = chr(int(self.chr_add) + int(str_line[1]))
			# 			midi_list.append(str_line)
			for line in self.midi_list:
				if int(line[0]) == self.timer:
					self.str_out += str(line[1])
				else:
					num_spaces = int(line[0]) - self.time
					self.str_out += ' ' * int(num_spaces / (int(self.timer)))
					self.str_out += str(line[1])
				self.time = int(line[0])

		elif type(self.midi_path)  == str:
			# midi_csv = py_midicsv.midi_to_csv(self.midi_path)
			# midi_list = []
			# for line in midi_csv:
			# 	str_line = [x.strip() for x in line.split(',')]
			# 	if str(str_line[2]) == 'Note_on_c':
			# 		str_line = str_line[1:2]+str_line[4:5]
			# 		str_line[1] = chr(int(self.chr_add) + int(str_line[1]))
			# 		midi_list.append(str_line)
			for line in self.midi_list:
				if int(line[0]) == self.timer:
					self.str_out += str(line[1])
				else:
					num_spaces = int(line[0]) - self.time
					self.str_out += ' '*int(num_spaces/(int(self.timer)))
					self.str_out += str(line[1])
					self.time = int(line[0])
		else:
			sys.exit('I don\'t recognise the midi_path')
		return self.str_out

	def write_to_text(self):
		output = open(str(self.data_dir) + str(self.output_text), 'w')
		output.write(self.str_out)
		output.close()

class Learn_to_play_music(Midi_convert):
	def __init__(self, rnn_size, num_layers, dropout):
		self.rnn_size = rnn_size
		self.num_layers = num_layers
		self.dropout = dropout
		Midi_convert.__init__(self,self.midi_path)

	def learn(self):
		subprocess.run(['th', 'RNN/train.lua', '-data_dir', 'RNN/data', '-rnn_size', str(self.rnn_size), '-num_layers', str(self.num_layers), '-dropout', str(self.dropout), '-gpuid -1'])

class Back_to_csv(Midi_convert):
	def __init__(self, output_midi):
		Midi_convert.__init__(self, self.midi_path)
		self.output_csv = output_midi








	# def str_to_midi(self, text_file):
	# 	midi_csv = []
	# 	with open(text_file, 'r') as file:
	# 		text = file.read()
	# 	for i in text:
	# 		midi_csv.append()



path = 'midi_solo/'
files = []
for r, d, f in os.walk(path):
	for file in f:
		if '.mid' in file:
			# print(file)
			files.append(os.path.join(r, file))

# midi_test = Midi_convert(midi_path='midi_solo/alb_esp1.mid')
# midi_string = midi_test.midi_to_string()
# output = open('input.txt', 'w')
# output.write(midi_string)
# output.close()

midi_test = Midi_convert(files)
midi_string = midi_test.midi_to_string()

print(len(midi_string))

output = open('input.txt', 'w')
output.write(midi_string)
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