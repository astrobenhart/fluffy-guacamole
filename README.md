# fluffy-guacamole
A RNN example making Jazz. Inspired by Carykh's video doing the same thing with baroque music (https://www.youtube.com/watch?v=SacogDL_4JU&amp;t=248s).

Get_midi.py uses selenium to go to http://www.piano-midi.de and download all the midi files there. I was going to write
it so it would collect all the artist links then navigate to them and download al the midis. I spent a couple hours on
trying to get it to work but in then end I just hard coded all the artist links to save time. It saves all the midis in
midi_solo as these are solo piano files.

read_midi.py then reads up all of those downloaded midi files in midi_solo, converts them to csv, removes the lines with
Text_t and Copyright_t and them writes all of those files into a single txt file, midi_all.txt.

To make the music we have to train a RNN with midi_all.txt as the input. To do this I move midi_all.txt into a clone of
Andrej Karpathy's character RNN Github repository, https://github.com/karpathy/char-rnn in a data/Jazz repository. Then
I run "th train.lua -data_dir data/Jazz -rnn_size 512 -num_layers 3 -dropout 0.5 -gpuid -1" from the char_rnn dir.

This takes ages to train, reduce the rnn_size and num_layers if you want it to run faster, of course your model will
be suffer because of that. Also, if you have a GPU that will make things run much faster, just change -gpuid to your
GPU (try 0).

Once this has finished you can then sample (it will actually spit out models at epochs that you can also sample from).
From the char_rnn dir run "th sample.lua cv/lm_lstm_epoch(your epoch).t7 -gpuid -1" and you get your output, YAY!.
