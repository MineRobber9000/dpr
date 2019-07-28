# This is a script to find a file in a scrambled datapack.
# You can use this to see where to get X resource if you didn't have randomize
# output a log for you.
# Usage: python find_file.py <file> <dir>
import os, hashlib, sys

def md5sum(filename):
	with open(filename,"rb") as f:
		return hashlib.md5(f.read()).hexdigest()

def pairs(d):
	for k in d:
		yield k, d[k]

def index(dir):
	out = dict()
	for dirpath, dirnames, filenames in os.walk(dir):
		for file in filenames:
			out[os.path.join(dirpath,file)]=md5sum(os.path.join(dirpath,file))
	return out

def reverse(d):
	out = dict()
	for k,v in pairs(d):
		out[v]=k
	return out

def find(filename,dir):
	hash = md5sum(filename)
	ind = reverse(index(dir))
	return ind.get(hash,False)

if __name__=="__main__":
	_, file, dir = sys.argv
	print(find(file,dir))
