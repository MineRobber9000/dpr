import librandomize
import argparse, os.path

targets = [x.replace("_"," ") for x in librandomize.RANDOMIZE]
randomizes = (", ".join(targets[:-1])+", and "+targets[-1]).replace("recipes","crafting/furnace recipes")

parser = argparse.ArgumentParser(description="Randomizes datapacks. Currently randomizes "+randomizes+".")
parser.add_argument("-s","--seed",help="Seed for randomizer.")
parser.add_argument("-l","--log",help="Outputs a log of what file maps to what.")
parser.add_argument("output",nargs="?",default="random",help="Filename for the randomized datapack.")
parser.add_argument("description",nargs="?",default="MineRobber's Data Pack Randomizer")
args = parser.parse_args()

mapping = librandomize.randomize_datapack(args.seed)

if args.seed is not None:
	desc = args.description+", seed {}".format(args.seed)
else:
	desc = args.description

librandomize.write_pack(args.output,desc,mapping)

if args.log is not None:
	end = ""
	if os.path.exists(args.log):
		i = 1
		while os.path.exists(args.log+"."+str(i)):
			i+=1
		end = "."+str(i)
	with open(args.log+end,"w") as f:
		for file in mapping:
			f.write("{} -> {}".format(mapping[file],file))
