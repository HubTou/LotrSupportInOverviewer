About LotrSupportInOverviewer
=============================
A tool that can generate a new Minecraft Overviewer textures jar including the Lord of the Rings Mod's textures, and modify installed Overviewer software taking into account local block IDs, so that the Minecraft Overviewer can support LOTR's new blocks rendering.


Installation
============
Verify you have installed Overviewer and that it's location is the one indicated in the OVERVIEWER_TEXTURES_PY Makefile's variable.

You'll also need :

- the zip/unzip package

- my ShowLocalMinecraftIds.sh utility (see http://minecraft.tournier.org/)


Usage
=====
Type "make", in order to fetch and build the necessary files.
You'll have to provide the path to a specific Lord of the Rings Mod instance when requested.

If everything goes well, type "make install", which will modify or upgrade your existing Overviewer installation.
Just to be on the safe side, a backup copy of your original Overviewer files will be done.

After that, copy the overviewer_textures-1.7.10-with-lotr.jar at the place you put the standard Overviewer textures file and reference the new one in your existing configuration.
For example, here's a simplified Overviewer configuration file doing that:
 	texturepath = "overviewer_textures-1.7.10-with-lotr.jar"
	
 	worlds["world"] = "world/DIM100"
	
 	renders["normalrender"] = {
 	    "world": "world",
 	    "title": "world map",
 	}
	
 	outputdir = "public_html/map"


Bugs
====
Stairs, walls and fences are not correctly represented.
Ent jars and barrels sides are disjoint.

Caveat
======
The Overviewer software is currently server wide installed, but the modifications we make to it are specific to a peculiar Minecraft server instance because block items provided by mods have instance specific IDs...
The glowing effect of Gulduril bricks is not represented.
A barrel tap side is undistinguished from the other sides.
There are no color differences between orc bombs strengths and their handles are not shown.
We don't distinguish from the top, middle and bottom of pillar's sides.
Mugs and plates are ugly.
The top part of Flame of Harad and Hibiscus have the same data value than Yellow Iris, so they all have yellow tops.
Clovers and tallGrass are not supported.
Blocks without textures are missing (beacons, stalactite, flower pots, elven & morgul portals, unsmeltery, etc.)


Versions and changelog
======================
 1.09	2015-10-31	Added support for LOTR Utumno bricks (used for The Pits)
 1.08	2015-10-24	Added support for LOTR mallornLadder, torches, orcTorches, beds, buttons, pressure plates, Utumno pillars, thatch floors, orcBombs
 1.07	2015-10-21	Added support for LOTR walls (buggy), fences (buggy)
 1.06	2015-10-18	Added support for LOTR pillars, single & double slabs, ovens, forges, hearth, Ungoliant's webs, ent jars (buggy), barrels (buggy), dwarven doors
 1.05	2015-10-14	Added support for LOTR stairs (buggy), bars
 1.04	2015-10-14	Corrected support for LOTR leaves, mordorGrass, aridGrass, quenditeGrass
 			Added support for LOTR corrupt mallorn sapling, flowers & plants
 			Buggy support for plantations, doubleFlowers
 			No support for tallGrass and clovers
 1.03	2015-10-11	Added support for LOTR saplings, crafting tables
 1.02	2015-10-08	Added support for LOTR woods, gulduril bricks (but without glow)
 			Corrected an indentation bug
 			Added multiple block IDs substitutions on the same line
 1.01	2015-10-07	Added support for LOTR rocks, leaves, planks, bricks, ore blocks
 1.00	2015-09-27	Initial release


License
=======
This open source software is distributed under a BSD license (see the "License" file for details).

The lotr_textures.py.template file contains code derived from samples of the Minecraft Overviewer textures.py file, which has the following license:
Minecraft Overviewer is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.


Credits
=======
The Minecraft Overviewer project!
Cf. http://overviewer.org/

The Lord of the Rings Minecraft mod
Cf. http://lotrminecraftmod.wikia.com/wiki/The_Lord_of_the_Rings_Minecraft_Mod_Wiki


Author
======
Hubert Tournier

October, 31 2015
