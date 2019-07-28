# dpr

Data Pack randomizer. Based on the same idea as SethBling's loot table 
randomizer (and I cribbed a couple notes from how he did it).

## How to use

You will need to extract the vanilla datapack. (If you're using a ZIP 
downloaded from the Releases tab, don't worry! I did it for you.)
Copy the latest version of Minecraft to `minecraft.jar` in this directory. Run 
`make data`. This will extract the datapack.

Once you have a `data` folder with the vanilla datapack, run `python randomize.py`.

```
usage: randomize.py [-h] [-s SEED] [-l LOG] [output] [description]

Randomizes datapacks. Currently randomizes loot tables, and structures.

positional arguments:
  output                Filename for the randomized datapack.
  description

optional arguments:
  -h, --help            show this help message and exit
  -s SEED, --seed SEED  Seed for randomizer.
  -l LOG, --log LOG     Outputs a log of what file maps to what.
```

## What's being randomized

* Loot tables
    * Mob drops, tile drops, bonus chests, etc.
* Structures

### What isn't being randomized (and why)

* Advancements - As far as I can tell, the only result of randomizing these is 
that you might end up needing an Elytra before you get the Acquire Hardware 
advancement. Not as interesting as getting dirt from diamond ore.
* Tags - This would probably break stuff in ways I don't want to think of.
* Crafting recipes - I will eventually get around to implementing this (hence it being extracted) but this requires some modifications per JSON file. Otherwise, the only thing that gets messed up is recipe overrides in other packs.
