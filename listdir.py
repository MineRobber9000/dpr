import os

def listdir(dir):
	out = []
	for dirpath, dirnames, filenames in os.walk(dir):
		for file in filenames:
			out.append(os.path.join(dirpath,file))
	return out
