# @(#) LotrSupportInOverviewer:Makefile v1.10 (2016-11-28) / Hubert Tournier 

VERSION=1.10
PY_VERSION=11
LOTR_VERSION=31

OVERVIEWER_TEXTURES_PY=/usr/local/lib/python2.7/site-packages/overviewer_core/textures.py

HTTP_CLIENT=fetch
HTTP_CLIENT_ARGS=--no-verify-peer -q
#HTTP_CLIENT=curl
#HTTP_CLIENT_ARGS="-sO"

main: verify-pre-requisites overviewer_textures-1.7.10-with-lotr.jar lotr_textures.py

verify-pre-requisites:
	@if [ "`whereis -q ${HTTP_CLIENT}`" = "" ] ; then echo "FATAL ERROR: you'll need an HTTP client. Set one in the Makefile." ; exit 1 ; fi
	@if [ "`whereis -q zip`" = "" ] ; then echo "FATAL ERROR: you'll need a zip/unzip package." ; exit 2 ; fi
	@if [ "`whereis -q unzip`" = "" ] ; then echo "FATAL ERROR: you'll need a zip/unzip package." ; exit 2 ; fi
	@if [ "`whereis -q ShowLocalMinecraftIds.sh`" = "" ] ; then echo "FATAL ERROR: you'll need the ShowLocalMinecraftIds.sh command. See http://minecraft.tournier.org/" ; exit 3 ; fi
	@if [ ! -f "${OVERVIEWER_TEXTURES_PY}" ] ; then echo "FATAL ERROR: Please install the Minecraft Overviewer first." ; echo "or verify the location of its textures.py file in the Makefile." ; exit 4 ; fi

overviewer_textures-1.7.10-with-lotr.jar: overviewer lotr
	@cd OUTPUT_DIR ; \
	zip -qr ../overviewer_textures-1.7.10-with-lotr.jar *
	@echo "Created overviewer_textures-1.7.10-with-lotr.jar"

overviewer: overviewer_textures-1.7.10.jar
	@mkdir -p OUTPUT_DIR
	@cd OUTPUT_DIR ; \
	tar xf ../overviewer_textures-1.7.10.jar ; \
	rm -r *.class META-INF log4j2.xml net pack.png assets/minecraft/font assets/minecraft/lang assets/minecraft/shaders assets/minecraft/texts
	@echo "Extracted assets from overviewer_textures-1.7.10.jar"
 
overviewer_textures-1.7.10.jar:
	@${HTTP_CLIENT} ${HTTP_CLIENT_ARGS} https://s3.amazonaws.com/Minecraft.Download/versions/1.7.10/1.7.10.jar
	@mv 1.7.10.jar overviewer_textures-1.7.10.jar
	@echo "Downloaded overviewer_textures-1.7.10.jar"

lotr: The_Lord_of_the_Rings_Mod_B${LOTR_VERSION}.jar
	@mkdir -p OUTPUT_DIR
	@cd OUTPUT_DIR ; \
	tar xf ../The_Lord_of_the_Rings_Mod_B${LOTR_VERSION}.jar ; \
	rm -r META-INF credits.txt lotr mcmod.info
	@echo "Extracted assets from The_Lord_of_the_Rings_Mod_B${LOTR_VERSION}.jar"

The_Lord_of_the_Rings_Mod_B${LOTR_VERSION}.jar:
	@${HTTP_CLIENT} ${HTTP_CLIENT_ARGS} http://harda.tournier.org/files/The_Lord_of_the_Rings_Mod_B${LOTR_VERSION}.jar
	@echo "Downloaded The_Lord_of_the_Rings_Mod_B${LOTR_VERSION}.jar"

lotr_textures.py:
	@./GenerateLocalLotrTexturesPy.sh ${OVERVIEWER_TEXTURES_PY}
	@echo "Created lotr_textures.py"

install: main
	@cp ${OVERVIEWER_TEXTURES_PY} ${OVERVIEWER_TEXTURES_PY}.BACKUP
	@./InstallOrUpgradeTexturesPy.sh ${OVERVIEWER_TEXTURES_PY} ${PY_VERSION}
	@echo "Installed modified ${OVERVIEWER_TEXTURES_PY}"

tarball:
	@tar czf LotrSupportInOverviewer-${VERSION}.tar.gz License ReadMe Makefile GenerateLocalLotrTexturesPy.sh lotr_textures.py.template InstallOrUpgradeTexturesPy.sh
	@echo "Created LotrSupportInOverviewer-${VERSION}.tar.gz"

clean:
	@rm -rf overviewer_textures-1.7.10.jar The_Lord_of_the_Rings_Mod_B${LOTR_VERSION}.jar OUTPUT_DIR

distclean: clean
	@rm -f overviewer_textures-1.7.10-with-lotr.jar lotr_textures.py LotrSupportInOverviewer-${VERSION}.tar.gz

