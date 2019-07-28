import json, listdir

# This script removes any "killed_by_player" conditions from the loot tables.
# This is to make finishing the game with these packs possible (since we can't
# guarantee that the blaze loot table ends up on a mob).

def loadf(filename):
	with open(filename) as f: return json.load(f)

def dumpf(filename,d):
	with open(filename,"w") as f: return json.dump(d,f,indent=2)

loot_tables = listdir.listdir("data/minecraft/loot_tables")

for file in loot_tables:
	loot_table = loadf(file)
	if any([x.get("conditions",False) for x in loot_table.get("pools",[])]):
		for pool in loot_table["pools"]:
			if not pool.get("conditions",False): continue
			try:
				pool["conditions"].remove({"condition":"minecraft:killed_by_player"})
			except ValueError: # x not in list
				pass
			if not pool["conditions"]: del pool["conditions"] # remove any empty condition list
		dumpf(file,loot_table)
