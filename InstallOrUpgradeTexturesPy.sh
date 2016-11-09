#!/bin/sh
# @(#) LotrSupportInOverviewer:InstallOrUpgradeTexturesPy.sh v1.00 (2015-09-27) / Hubert Tournier 

main( )
{
	if [ $# != 2 ]
	then	what ${0} | grep -v "${0}:" | sed "s/^[ 	]*//"
        	echo "Usage: `basename ${0}` path_to_overviewer_textures_py version_to_install"
		exit 1
	fi

	if [ ! -f "${1}" ]
	then	echo "FATAL ERROR: Please install Overviewer first (or verify its location in the Makefile)."
		exit 2
	fi

	INSTALLED_VERSION=`grep "^# { LotrSupportInOverviewer" ${1} | sed "s/[^0-9]*//g"`

	if [ "${INSTALLED_VERSION}" == "" ] 
	then	cat lotr_textures.py >> ${1}
		rm -f ${1}[co]

	elif [ "${INSTALLED_VERSION}" -lt "${2}" ]
	then	mv ${1} ${1}.old
        	awk	'
			/^# { LotrSupportInOverviewer/,/^# } LotrSupportInOverviewer/	{next}
													{print}
			END										{system("cat lotr_textures.py")}
			' ${1}.old > ${1}
		rm ${1}.old
		rm -f ${1}[co]
	fi
}

main $*

