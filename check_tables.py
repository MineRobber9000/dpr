import json, listdir

# This script checks the conditions each table has.
# It does not change any of the files.

def loadf(filename):
	with open(filename) as f: return json.load(f)

def get_conditions(table):
	out = []
	if "pools" not in table: return []
	for pool in table["pools"]:
		if not pool.get("conditions",False): continue
		for condition in pool["conditions"]:
			out.append(condition["condition"])
	return out

loot_tables = listdir.listdir("data/minecraft/loot_tables")

for file in loot_tables:
	loot_table = loadf(file)
	if any([x.get("conditions",False) for x in loot_table.get("pools",[])]):
		print("File {} has conditions: {}".format(file,", ".join(get_conditions(loot_table))))
