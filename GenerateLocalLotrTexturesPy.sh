#!/bin/sh
# @(#) LotrSupportInOverviewer:GenerateLocalLotrTexturesPy.sh v1.01 (2015-10-08) / Hubert Tournier 

main( )
{
	if [ $# != 1 ]
	then	what ${0} | grep -v "${0}:" | sed "s/^[ 	]*//"
        	echo "Usage: `basename ${0}` path_to_overviewer_textures_py"
		exit 1
	fi

	if [ ! -f "${1}" ]
	then	echo "FATAL ERROR: Please install Overviewer first (or verify its location in the Makefile)."
		exit 2
	fi

	while true
	do	echo -n "Path to your Minecraft world level.dat file: "
		read LEVEL_DAT_PATH
		[ -f "${LEVEL_DAT_PATH}" ] 2>/dev/null && break
	done

	ShowLocalMinecraftIds.sh -b -m lotr -l "${LEVEL_DAT_PATH}" \
	| awk '
		BEGIN				{
							FS=";"
						}
		/^[0-9]*;01;lotr:tile.lotr:.*/	{
							BlockId[$3] = $1
							next
						}
		/<lotr:tile.lotr:.*>/		{
							while (match($0, /<lotr[^>]*>/))
							{
								K = substr($0, RSTART + 1, RLENGTH - 2)
								V = BlockId[ K ]
								sub(/<lotr[^>]*>/, V)
							}
						}
						{
							print
						}
		' - lotr_textures.py.template \
	> lotr_textures.py
}

main $*

