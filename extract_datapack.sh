#!/bin/bash

# Remove any remaining data pack files
rm -rf data

# Extract all data files (minus the ones we don't want to randomize)
unzip minecraft.jar -x *.class log4j2.xml pack.mcmeta META-INF/* assets/* pack.png version.json data/minecraft/tags/* data/minecraft/advancements/*

# Remove killed_by_player conditions from loot tables to ensure completability
python ./fix_tables.py
