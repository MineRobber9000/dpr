import os, random, io, zipfile, json

import listdir

RANDOMIZE = ["loot_tables","structures"]

def randomize(dir,no_randomize=False):
	"""Create a dict mapping every file in `dir` to another file in `dir`. If `no_randomize` is True, skip randomization."""
	file_list = []
	remaining = []
	for filename in listdir.listdir(dir):
		file_list.append(filename)
		remaining.append(filename)
	mapping = dict()
	if no_randomize:
		for file in file_list: mapping[file]=file
		return mapping
	for file in file_list:
		i = random.randint(1,len(remaining))-1
		mapping[file]=remaining[i]
		del remaining[i]
	return mapping

def randomize_datapack(seed=None,no_randomize=False):
	if seed is not None:
		random.seed(seed)
	mapping = dict()
	for target in RANDOMIZE:
		mapping.update(randomize(os.path.join("data/minecraft",target),no_randomize=no_randomize))
	return mapping

def write_pack(name,desc,mapping):
	"""Write datapack with mapping `mapping` to file `name`.zip with the description `desc`."""
	# not sure why Seth doesn't just use the actual file but whatever, I'll do it his way.
	b = io.BytesIO()
	z = zipfile.ZipFile(b,"w",zipfile.ZIP_DEFLATED,False)
	# Write pack.mcmeta
	z.writestr("pack.mcmeta",json.dumps(dict(pack=dict(pack_format=1,description=desc))))
	# For each file f, write its doppelganger mapping[f] to it.
	for f in mapping:
		with open(mapping[f],"rb") as mf:
			z.writestr(f,mf.read())
	z.close()
	with open(name+".zip","wb") as f:
		f.write(b.getvalue())
