# { LotrSupportInOverviewer 11
# @(#) LotrSupportInOverviewer:lotr_textures.py v1.10 (2016-11-28) / Hubert Tournier

################################################################################
# Opaque single-texture full blocks without data value: ########################
################################################################################

block(blockid=<lotr:tile.oreCopper>, top_image="assets/lotr/textures/blocks/oreCopper.png")
block(blockid=<lotr:tile.oreTin>, top_image="assets/lotr/textures/blocks/oreTin.png")
block(blockid=<lotr:tile.oreSilver>, top_image="assets/lotr/textures/blocks/oreSilver.png")
block(blockid=<lotr:tile.oreMithril>, top_image="assets/lotr/textures/blocks/oreMithril.png")
block(blockid=<lotr:tile.oreNaurite>, top_image="assets/lotr/textures/blocks/oreNaurite.png")
block(blockid=<lotr:tile.oreQuendite>, top_image="assets/lotr/textures/blocks/oreQuendite.png")
block(blockid=<lotr:tile.oreGlowstone>, top_image="assets/lotr/textures/blocks/oreGlowstone.png")
block(blockid=<lotr:tile.remains>, top_image="assets/lotr/textures/blocks/remains.png")
block(blockid=<lotr:tile.oreSulfur>, top_image="assets/lotr/textures/blocks/oreSulfur.png")
block(blockid=<lotr:tile.oreSaltpeter>, top_image="assets/lotr/textures/blocks/oreSaltpeter.png")
block(blockid=<lotr:tile.quagmire>, top_image="assets/lotr/textures/blocks/quagmire.png")
block(blockid=<lotr:tile.goran>, top_image="assets/lotr/textures/blocks/goran.png")
block(blockid=<lotr:tile.thatch>, top_image="assets/lotr/textures/blocks/thatch.png")
block(blockid=<lotr:tile.termiteMound>, top_image="assets/lotr/textures/blocks/termiteMound.png")
block(blockid=<lotr:tile.mordorDirt>, top_image="assets/lotr/textures/blocks/mordorDirt.png")
block(blockid=<lotr:tile.mordorGravel>, top_image="assets/lotr/textures/blocks/mordorGravel.png")
block(blockid=<lotr:tile.obsidianGravel>, top_image="assets/lotr/textures/blocks/obsidianGravel.png")
block(blockid=<lotr:tile.mud>, top_image="assets/lotr/textures/blocks/mud.png")
block(blockid=<lotr:tile.dwarvenDoor>, top_image="assets/minecraft/textures/blocks/stone.png")
block(blockid=<lotr:tile.planksRotten>, top_image="assets/lotr/textures/blocks/planksRotten_rotten.png")
block(blockid=<lotr:tile.scorchedStone>, top_image="assets/lotr/textures/blocks/scorchedStone.png")

################################################################################
# Opaque single-texture full blocks with data value: ###########################
################################################################################

@material(blockid=<lotr:tile.rock>, data=range(5), solid=True)
def rock_values(self, blockid, data):
    # Mordor Rock
    t =  self.load_image_texture("assets/lotr/textures/blocks/rock_mordor.png")
    if data == 1:  # Gondor Rock
        t =  self.load_image_texture("assets/lotr/textures/blocks/rock_gondor.png")
    elif data == 2:  # Rohan Rock
        t =  self.load_image_texture("assets/lotr/textures/blocks/rock_rohan.png")
    elif data == 3:  # Sarlluin
        t =  self.load_image_texture("assets/lotr/textures/blocks/rock_blue.png")
    elif data == 4:  # Sarncaran
        t =  self.load_image_texture("assets/lotr/textures/blocks/rock_red.png")
    return self.build_block(t, t)

@material(blockid=<lotr:tile.oreMorgulIron>, data=range(2), solid=True)
def oreMorgulIron_values(self, blockid, data):
    # Morgul Iron Ore
    t =  self.load_image_texture("assets/lotr/textures/blocks/oreMorgulIron.png")
    if data == 1:  # Morgul Iron Ore (Mordor) 
        t =  self.load_image_texture("assets/lotr/textures/blocks/oreMorgulIron_mordor.png")
    return self.build_block(t, t)

@material(blockid=<lotr:tile.oreGulduril>, data=range(2), solid=True)
def oreGulduril_values(self, blockid, data):
    # Gulduril Ore
    t =  self.load_image_texture("assets/lotr/textures/blocks/oreGulduril.png")
    if data == 1:  # Gulduril Ore (Mordor)
        t =  self.load_image_texture("assets/lotr/textures/blocks/oreGulduril_mordor.png")
    return self.build_block(t, t)

@material(blockid=<lotr:tile.oreStorage>, data=range(16), solid=True)
def oreStorage_values(self, blockid, data):
    # Block of Copper
    img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_copper.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_copper.png"))
    if data == 1:  # Block of Tin
        img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_tin.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_tin.png"))
    elif data == 2:  # Block of Bronze
        img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_bronze.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_bronze.png"))
    elif data == 3:  # Block of Silver
        img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_silver.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_silver.png"))
    elif data == 4:  # Block of Mithril
        img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_mithril.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_mithril.png"))
    elif data == 5:  # Block of Orc Steel
        img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_orcSteel.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_orcSteel_side.png"))
    elif data == 6:  # Block of Quendite
        img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_quendite.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_quendite.png"))
    elif data == 7:  # Block of Dwarven Steel
        img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_dwarfSteel.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_dwarfSteel.png"))
    elif data == 8:  # Block of Galvorn
        img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_galvorn.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_galvorn.png"))
    elif data == 9:  # Block of Uruk Steel
        img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_urukSteel.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_urukSteel.png"))
    elif data == 10:  # Block of Naurite
        img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_naurite.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_naurite.png"))
    elif data == 11:  # Block of Gulduril
        img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_gulduril.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_gulduril.png"))
    elif data == 12:  # Block of Morgul Steel
        img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_morgulSteel.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_morgulSteel_side.png"))
    elif data == 13:  # Block of Sulfur
        img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_sulfur.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_sulfur.png"))
    elif data == 14:  # Block of Salpeter
        img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_saltpeter.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_saltpeter.png"))
    elif data == 15:  # Block of Blue Dwarven Steel 
        img =  self.build_block(self.load_image_texture("assets/lotr/textures/blocks/oreStorage_blueDwarfSteel.png"), self.load_image_texture("assets/lotr/textures/blocks/oreStorage_blueDwarfSteel.png"))
    return img

@material(blockid=<lotr:tile.oreStorage2>, data=range(2), solid=True)
def oreStorage2_values(self, blockid, data):
    # Block of Black Uruk Steel
    t = self.load_image_texture("assets/lotr/textures/blocks/oreStorage2_blackUrukSteel.png")
    if data == 1:  # Block of Elven Steel 
        t = self.load_image_texture("assets/lotr/textures/blocks/oreStorage2_elfSteel.png")
    return self.build_block(t, t)

##### Caveat: The glowing effect of Gulduril bricks is not represented #####
@material(blockid=<lotr:tile.guldurilBrick>, data=range(6), solid=True)
def guldurilBrick_values(self, blockid, data):
    # Gulduril Mordor Brick
    t = self.load_image_texture("assets/lotr/textures/blocks/brick_mordor.png")
    if data == 1:  # Gulduril Cracked Mordor Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_mordorCracked.png")
    elif data == 2:  # Gulduril Angmar Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_angmar.png")
    elif data == 3:  # Gulduril Cracked Angmar Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_angmarCracked.png")
    elif data == 4:  # Gulduril Dol Guldur Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_dolGuldur.png")
    elif data == 5:  # Gulduril Cracked Dol Guldur Brick 
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_dolGuldurCracked.png")
    return self.build_block(t, t)

@material(blockid=[<lotr:tile.leaves>, <lotr:tile.leaves2>, <lotr:tile.leaves3>, <lotr:tile.leaves4>, <lotr:tile.leaves5>, <lotr:tile.fruitLeaves>], data=range(16), transparent=True, solid=True)
def lotr_leaves(self, blockid, data):
    # mask out the bits 4 and 8
    # they are used for player placed and check-for-decay blocks
    data = data & 0x7
    t = self.load_image_texture("assets/minecraft/textures/blocks/leaves_oak.png")
    if blockid == <lotr:tile.leaves>:
        if data == 0 or data == 4:  # Shire Pine Leaves
            t =  self.load_image_texture("assets/lotr/textures/blocks/leaves_shirePine_fancy.png")
        elif data == 1 or data == 5:  # Mallorn Leaves
            t =  self.load_image_texture("assets/lotr/textures/blocks/leaves_mallorn_fancy.png")
        elif data == 2 or data == 6:  # Mirk-oak Leaves
            t =  self.load_image_texture("assets/lotr/textures/blocks/leaves_mirkOak_fancy.png")
        elif data == 3 or data == 7:  # Red Mirk-oak Leaves
            t =  self.load_image_texture("assets/lotr/textures/blocks/leaves_mirkOakRed_fancy.png")
    elif blockid == <lotr:tile.leaves2>:
        if data == 0 or data == 4:  # Lebethron Leaves
            t = self.load_image_texture("assets/lotr/textures/blocks/leaves2_lebethron_fancy.png")
        elif data == 1 or data == 5:  # Beech Leaves
            t = self.load_image_texture("assets/lotr/textures/blocks/leaves2_beech_fancy.png")
        elif data == 2 or data == 6:  # Holly Leaves
            t = self.load_image_texture("assets/lotr/textures/blocks/leaves2_holly_fancy.png")
        elif data == 3 or data == 7:  # Banana Leaves 
            t = self.load_image_texture("assets/lotr/textures/blocks/leaves2_banana_fancy.png")
    elif blockid == <lotr:tile.leaves3>:
        if data == 0 or data == 4:  # Maple Leaves
            t = self.load_image_texture("assets/lotr/textures/blocks/leaves3_maple_fancy.png")
        elif data == 1 or data == 5:  # Larch Leaves
            t = self.load_image_texture("assets/lotr/textures/blocks/leaves3_larch_fancy.png")
        elif data == 2 or data == 6:  # Date Palm Leaves
            t = self.load_image_texture("assets/lotr/textures/blocks/leaves3_datePalm_fancy.png")
        elif data == 3 or data == 7:  # Mangrove Leaves 
            t = self.load_image_texture("assets/lotr/textures/blocks/leaves3_mangrove_fancy.png")
    elif blockid == <lotr:tile.leaves4>:
        if data == 0 or data == 4:  # Chestnut Leaves
            t = self.load_image_texture("assets/lotr/textures/blocks/leaves4_chestnut_fancy.png")
        elif data == 1 or data == 5:  # Baobab Leaves
            t = self.load_image_texture("assets/lotr/textures/blocks/leaves4_baobab_fancy.png")
        elif data == 2 or data == 6:  # Cedar Leaves
            t = self.load_image_texture("assets/lotr/textures/blocks/leaves4_cedar_fancy.png")
        elif data == 3 or data == 7:  # Fir Leaves 
            t = self.load_image_texture("assets/lotr/textures/blocks/leaves4_fir_fancy.png")
    elif blockid == <lotr:tile.leaves5>:
        if data == 0 or data == 4:  # Pine Leaves 
            t = self.load_image_texture("assets/lotr/textures/blocks/leaves5_pine_fancy.png")
    elif blockid == <lotr:tile.fruitLeaves>:
        if data == 0 or data == 4:  # Apple Leaves
            t = self.load_image_texture("assets/lotr/textures/blocks/fruitLeaves_apple_fancy.png")
        elif data == 1 or data == 5:  # Pear Leaves
            t = self.load_image_texture("assets/lotr/textures/blocks/fruitLeaves_pear_fancy.png")
        elif data == 2 or data == 6:  # Cherry Leaves
            t = self.load_image_texture("assets/lotr/textures/blocks/fruitLeaves_cherry_fancy.png")
        elif data == 3 or data == 7:  # Mango Leaves 
            t = self.load_image_texture("assets/lotr/textures/blocks/fruitLeaves_mango_fancy.png")
    return self.build_block(t, t)

@material(blockid=<lotr:tile.planks>, data=range(16), solid=True)
def planks_values(self, blockid, data):
    # Shire Pine Wood Planks
    t =  self.load_image_texture("assets/lotr/textures/blocks/planks_shirePine.png")
    if data == 1:  # Mallorn Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks_mallorn.png")
    elif data == 2:  # Mirk-oak Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks_mirkOak.png")
    elif data == 3:  # Charred Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks_charred.png")
    elif data == 4:  # Apple Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks_apple.png")
    elif data == 5:  # Pear Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks_pear.png")
    elif data == 6:  # Cherry Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks_cherry.png")
    elif data == 7:  # Mango Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks_mango.png")
    elif data == 8:  # Lebethron Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks_lebethron.png")
    elif data == 9:  # Beech Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks_beech.png")
    elif data == 10:  # Holly Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks_holly.png")
    elif data == 11:  # Banana Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks_banana.png")
    elif data == 12:  # Maple Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks_maple.png")
    elif data == 13:  # Larch Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks_larch.png")
    elif data == 14:  # Date Palm Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks_datePalm.png")
    elif data == 15:  # Mangrove Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks_mangrove.png")
    return self.build_block(t, t)

@material(blockid=<lotr:tile.planks2>, data=range(5), solid=True)
def planks2_values(self, blockid, data):
    # Chestnut Wood Planks
    t =  self.load_image_texture("assets/lotr/textures/blocks/planks2_chestnut.png")
    if data == 1:  # Baobab Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks2_baobab.png")
    elif data == 2:  # Cedar Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks2_cedar.png")
    elif data == 3:  # Fir Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks2_fir.png")
    elif data == 4:  # Pine Wood Planks
        t =  self.load_image_texture("assets/lotr/textures/blocks/planks2_pine.png")
    return self.build_block(t, t)

@material(blockid=<lotr:tile.brick>, data=range(16), solid=True)
def brick_values(self, blockid, data):
    # Mordor Brick
    t = self.load_image_texture("assets/lotr/textures/blocks/brick_mordor.png")
    if data == 1:  # Gondor Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_gondor.png")
    elif data == 2:  # Mossy Gondor Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_gondorMossy.png")
    elif data == 3:  # Cracked Gondor Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_gondorCracked.png")
    elif data == 4:  # Rohan Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_rohan.png")
    elif data == 5:  # Carved Gondor Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_gondorRuins.png")
    elif data == 6:  # Dwarven Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_dwarven.png")
    elif data == 7:  # Cracked Mordor Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_mordorCracked.png")
    elif data == 8:  # Silver-trimmed Dwarven Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_dwarvenSilver.png")
    elif data == 9:  # Gold-trimmed Dwarven Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_dwarvenGold.png")
    elif data == 10:  # Mithril-trimmed Dwarven Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_dwarvenMithril.png")
    elif data == 11:  # Galadhrim Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_galadhrim.png")
    elif data == 12:  # Mossy Galadhrim Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_galadhrimMossy.png")
    elif data == 13:  # Cracked Galadhrim Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_galadhrimCracked.png")
    elif data == 14:  # Sarlluin Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_blueRock.png")
    elif data == 15:  # Near Harad Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick_nearHarad.png")
    return self.build_block(t, t)

@material(blockid=<lotr:tile.brick2>, data=range(16), solid=True)
def brick2_values(self, blockid, data):
    # Angmar Brick
    t = self.load_image_texture("assets/lotr/textures/blocks/brick2_angmar.png")
    if data == 1:  # Cracked Angmar Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_angmarCracked.png")
    elif data == 2:  # Sarncaran Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_redRock.png")
    elif data == 3:  # Arnor Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_arnor.png")
    elif data == 4:  # Mossy Arnor Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_arnorMossy.png")
    elif data == 5:  # Cracked Arnor Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_arnorCracked.png")
    elif data == 6:  # Carved Arnor Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_arnorCarved.png")
    elif data == 7:  # Uruk Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_uruk.png")
    elif data == 8:  # Dol Guldur Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_dolGuldur.png")
    elif data == 9:  # Cracked Dol Guldur Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_dolGuldurCracked.png")
    elif data == 10:  # Carved Mordor Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_mordorCarved.png")
    elif data == 11:  # Black Gondor Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_blackGondor.png")
    elif data == 12:  # Carved Dwarven Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_dwarvenCarved.png")
    elif data == 13:  # Carved High Elven Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_highElvenCarved.png")
    elif data == 14:  # Carved Wood-elven Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_woodElvenCarved.png")
    elif data == 15:  # Carved Galadhrim Brick 
        t = self.load_image_texture("assets/lotr/textures/blocks/brick2_galadhrimCarved.png")
    return self.build_block(t, t)

@material(blockid=<lotr:tile.brick3>, data=range(13), solid=True)
def brick3_values(self, blockid, data):
    # Carved Sarlluin Brick
    t = self.load_image_texture("assets/lotr/textures/blocks/brick3_blueCarved.png")
    if data == 1:  # Carved Sarncaran Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick3_redCarved.png")
    elif data == 2:  # High Elven Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick3_highElven.png")
    elif data == 3:  # Mossy High Elven Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick3_highElvenMossy.png")
    elif data == 4:  # Cracked High Elven Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick3_highElvenCracked.png")
    elif data == 5:  # Wood-elven Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick3_woodElven.png")
    elif data == 6:  # Mossy Wood-elven Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick3_woodElvenMossy.png")
    elif data == 7:  # Cracked Wood-elven Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick3_woodElvenCracked.png")
    elif data == 8:  # Carved Near Harad Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick3_nearHaradCarved.png")
    elif data == 9:  # Dol Amroth Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick3_dolAmroth.png")
    elif data == 10:  # Moredain Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick3_moredain.png")
    elif data == 11:  # Cracked near Harad Brick
        t = self.load_image_texture("assets/lotr/textures/blocks/brick3_nearHaradCracked.png")
    elif data == 12:  # Glowing Dwarven Brick 
        t = self.load_image_texture("assets/lotr/textures/blocks/brick3_dwarvenGlowing.png")
    return self.build_block(t, t)

@material(blockid=<lotr:tile.utumnoBrick>, data=range(6), solid=True)
def utumnoBrick_values(self, blockid, data):
    t =  self.load_image_texture("assets/lotr/textures/blocks/utumnoBrick_fire.png")
    if data == 1:
        t =  self.load_image_texture("assets/lotr/textures/blocks/utumnoBrick_burning.png")
    elif data == 2:
        t =  self.load_image_texture("assets/lotr/textures/blocks/utumnoBrick_ice.png")
    elif data == 3:
        t =  self.load_image_texture("assets/lotr/textures/blocks/utumnoBrick_iceGlowing.png")
    elif data == 4:
        t =  self.load_image_texture("assets/lotr/textures/blocks/utumnoBrick_obsidian.png")
    elif data == 5:
        t =  self.load_image_texture("assets/lotr/textures/blocks/utumnoBrick_obsidianFire.png")
    return self.build_block(t, t)

################################################################################
# Opaque bi-texture full blocks: ###############################################
################################################################################

@material(blockid=<lotr:tile.angmarCraftingTable>, data=range(1), solid=True)
def angmarCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/angmarCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/angmarCraftingTable_side.png"))

@material(blockid=<lotr:tile.blueDwarvenCraftingTable>, data=range(1), solid=True)
def blueDwarvenCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/blueDwarvenCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/blueDwarvenCraftingTable_side.png"))

@material(blockid=<lotr:tile.dolAmrothCraftingTable>, data=range(1), solid=True)
def dolAmrothCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/dolAmrothCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/dolAmrothCraftingTable_side.png"))

@material(blockid=<lotr:tile.dolGuldurCraftingTable>, data=range(1), solid=True)
def dolGuldurCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/dolGuldurCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/dolGuldurCraftingTable_side.png"))

@material(blockid=<lotr:tile.dunlendingCraftingTable>, data=range(1), solid=True)
def dunlendingCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/dunlendingCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/dunlendingCraftingTable_side.png"))

@material(blockid=<lotr:tile.dwarvenCraftingTable>, data=range(1), solid=True)
def dwarvenCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/dwarvenCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/dwarvenCraftingTable_side.png"))

@material(blockid=<lotr:tile.elvenCraftingTable>, data=range(1), solid=True)
def elvenCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/elvenCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/elvenCraftingTable_side.png"))

@material(blockid=<lotr:tile.gondorianCraftingTable>, data=range(1), solid=True)
def gondorianCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/gondorianCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/gondorianCraftingTable_side.png"))

@material(blockid=<lotr:tile.gundabadCraftingTable>, data=range(1), solid=True)
def gundabadCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/gundabadCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/gundabadCraftingTable_side.png"))

@material(blockid=<lotr:tile.halfTrollCraftingTable>, data=range(1), solid=True)
def halfTrollCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/halfTrollCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/halfTrollCraftingTable_side.png"))

@material(blockid=<lotr:tile.highElvenCraftingTable>, data=range(1), solid=True)
def highElvenCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/highElvenCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/highElvenCraftingTable_side.png"))

@material(blockid=<lotr:tile.moredainCraftingTable>, data=range(1), solid=True)
def moredainCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/moredainCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/moredainCraftingTable_side.png"))

@material(blockid=<lotr:tile.morgulCraftingTable>, data=range(1), solid=True)
def morgulCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/morgulCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/morgulCraftingTable_side.png"))

@material(blockid=<lotr:tile.nearHaradCraftingTable>, data=range(1), solid=True)
def nearHaradCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/nearHaradCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/nearHaradCraftingTable_side.png"))

@material(blockid=<lotr:tile.rangerCraftingTable>, data=range(1), solid=True)
def rangerCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/rangerCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/rangerCraftingTable_side.png"))

@material(blockid=<lotr:tile.rohirricCraftingTable>, data=range(1), solid=True)
def rohirricCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/rohirricCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/rohirricCraftingTable_side.png"))

@material(blockid=<lotr:tile.tauredainCraftingTable>, data=range(1), solid=True)
def tauredainCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/tauredainCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/tauredainCraftingTable_side.png"))

@material(blockid=<lotr:tile.urukCraftingTable>, data=range(1), solid=True)
def urukCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/urukCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/urukCraftingTable_side.png"))

@material(blockid=<lotr:tile.woodElvenCraftingTable>, data=range(1), solid=True)
def woodElvenCraftingTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/woodElvenCraftingTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/woodElvenCraftingTable_side.png"))

@material(blockid=<lotr:tile.quenditeGrass>, data=range(1), solid=True)
def quenditeGrass(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/quenditeGrass_top.png"), self.load_image_texture("assets/lotr/textures/blocks/quenditeGrass_side.png"))

@material(blockid=<lotr:tile.mudGrass>, data=range(1), solid=True)
def mudGrass(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/mudGrass_top.png"), self.load_image_texture("assets/lotr/textures/blocks/mudGrass_side.png"))

@material(blockid=<lotr:tile.mudFarmland>, data=range(1), solid=True)
def mudFarmland(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/mudFarmland_top.png"), self.load_image_texture("assets/lotr/textures/blocks/mudFarmland_side.png"))

@material(blockid=<lotr:tile.hearth>, data=range(1), solid=True)
def hearth(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/hearth_top.png"), self.load_image_texture("assets/lotr/textures/blocks/hearth_side.png"))

@material(blockid=<lotr:tile.redSandstone>, data=range(1), solid=True)
def hearth(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/redSandstone_top.png"), self.load_image_texture("assets/lotr/textures/blocks/redSandstone.png"))

##### Caveat: the tap side is undistinguished from the other sides #####
@material(blockid=<lotr:tile.barrel>, data=range(1), solid=True)
def barrel(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/barrel_top.png"), self.load_image_texture("assets/lotr/textures/blocks/barrel_side.png"))

@material(blockid=<lotr:tile.entJar>, data=range(1), solid=True)
def entJar(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/entJar_top.png"), self.load_image_texture("assets/lotr/textures/blocks/entJar_side.png"))

##### Caveat: no color differences between bomb strengths and handles are not shown #####
@material(blockid=<lotr:tile.orcBomb>, data=range(16), solid=True)
def orcBomb(self, blockid, data):
    if data == 0 or data == 1 or data == 2:
        return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/orcBomb_top.png"), self.load_image_texture("assets/lotr/textures/blocks/orcBomb_side.png"))
    elif data == 8 or data == 9 or data == 10:
        return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/orcBomb_fire_top.png"), self.load_image_texture("assets/lotr/textures/blocks/orcBomb_fire_side.png"))

################################################################################
# Opaque bi-texture full blocks with orientation: ##############################
################################################################################

@material(blockid=[<lotr:tile.wood>,<lotr:tile.wood2>,<lotr:tile.wood3>,<lotr:tile.wood4>,<lotr:tile.wood5>,<lotr:tile.fruitWood>,<lotr:tile.rottenLog>], data=range(16), solid=True)
def lotr_wood(self, blockid, data):
    # extract orientation and wood type from data bits
    wood_type = data & 3
    wood_orientation = data & 12
    if self.rotation == 1:
        if wood_orientation == 4: wood_orientation = 8
        elif wood_orientation == 8: wood_orientation = 4
    elif self.rotation == 3:
        if wood_orientation == 4: wood_orientation = 8
        elif wood_orientation == 8: wood_orientation = 4
    # choose textures
    top = self.load_image_texture("assets/minecraft/textures/blocks/log_oak_top.png")
    side = self.load_image_texture("assets/minecraft/textures/blocks/log_oak.png")
    if blockid == <lotr:tile.wood>:
        if wood_type == 0: # Shire Pine Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood_shirePine_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood_shirePine_side.png")
        elif wood_type == 1: # Mallorn Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood_mallorn_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood_mallorn_side.png")
        elif wood_type == 2: # Mirk-oak Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood_mirkOak_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood_mirkOak_side.png")
        elif wood_type == 3: # Charred Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood_charred_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood_charred_side.png")
    elif blockid == <lotr:tile.wood2>:
        if wood_type == 0: # Lebethron Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood2_lebethron_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood2_lebethron_side.png")
        elif wood_type == 1: # Beech Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood2_beech_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood2_beech_side.png")
        elif wood_type == 2: # Holly Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood2_holly_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood2_holly_side.png")
        elif wood_type == 3: # Banana Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood2_banana_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood2_banana_side.png")
    elif blockid == <lotr:tile.wood3>:
        if wood_type == 0: # Maple Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood3_maple_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood3_maple_side.png")
        elif wood_type == 1: # Larch Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood3_larch_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood3_larch_side.png")
        elif wood_type == 2: # Date Palm Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood3_datePalm_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood3_datePalm_side.png")
        elif wood_type == 3: # Mangrove Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood3_mangrove_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood3_mangrove_side.png")
    elif blockid == <lotr:tile.wood4>:
        if wood_type == 0: # Chestnut Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood4_chestnut_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood4_chestnut_side.png")
        elif wood_type == 1: # Baobab Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood4_baobab_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood4_baobab_side.png")
        elif wood_type == 2: # Cedar Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood4_cedar_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood4_cedar_side.png")
        elif wood_type == 3: # Fir Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood4_fir_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood4_fir_side.png")
    elif blockid == <lotr:tile.wood5>:
        if wood_type == 0: # Pine Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/wood5_pine_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/wood5_pine_side.png")
    elif blockid == <lotr:tile.fruitWood>:
        if wood_type == 0: # Apple Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/fruitWood_apple_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/fruitWood_apple_side.png")
        elif wood_type == 1: # Pear Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/fruitWood_pear_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/fruitWood_pear_side.png")
        elif wood_type == 2: # Cherry Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/fruitWood_cherry_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/fruitWood_cherry_side.png")
        elif wood_type == 3: # Mango Wood
            top = self.load_image_texture("assets/lotr/textures/blocks/fruitWood_mango_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/fruitWood_mango_side.png")
    elif blockid == <lotr:tile.rottenLog>:
        if wood_type == 0: # 
            top = self.load_image_texture("assets/lotr/textures/blocks/rottenLog_rotten_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/rottenLog_rotten_side.png")
    # choose orientation and paste textures
    if wood_orientation == 0:
        return self.build_block(top, side)
    elif wood_orientation == 4: # east-west orientation
        return self.build_full_block(side.rotate(90), None, None, top, side.rotate(90))
    elif wood_orientation == 8: # north-south orientation
        return self.build_full_block(side, None, None, side.rotate(270), top)

##### Caveat: we don't distinguish from the top, middle and bottom of pillar's sides #####
@material(blockid=[<lotr:tile.pillar>, <lotr:tile.utumnoPillar>], data=range(14), solid=True)
def lotr_pillars(self, blockid, data):
    top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_dwarven_face.png")
    side = self.load_image_texture("assets/lotr/textures/blocks/pillar_dwarven_side.png")
    if blockid == <lotr:tile.pillar>:
        if data == 1:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_galadhrim_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_galadhrim_side.png")
        elif data == 2:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_galadhrimCracked_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_galadhrimCracked_side.png")
        elif data == 3:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_blueRock_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_blueRock_side.png")
        elif data == 4:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_redRock_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_redRock_side.png")
        elif data == 5:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_nearHarad_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_nearHarad_side.png")
        elif data == 6:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_gondor_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_gondor_side.png")
        elif data == 7:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_mordor_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_mordor_side.png")
        elif data == 8:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_rohan_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_rohan_side.png")
        elif data == 9:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_blackGondor_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_blackGondor_side.png")
        elif data == 10:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_highElven_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_highElven_side.png")
        elif data == 11:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_highElvenCracked_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_highElvenCracked_side.png")
        elif data == 12:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_woodElven_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_woodElven_side.png")
        elif data == 13:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_woodElvenCracked_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_woodElvenCracked_side.png")
    elif blockid == <lotr:tile.utumnoPillar>:
        if data == 0:
            top  = self.load_image_texture("assets/lotr/textures/blocks/utumnoPillar_fire_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/utumnoPillar_fire_side.png")
        elif data == 1:
            top  = self.load_image_texture("assets/lotr/textures/blocks/utumnoPillar_ice_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/utumnoPillar_ice_side.png")
        elif data == 2:
            top  = self.load_image_texture("assets/lotr/textures/blocks/utumnoPillar_obsidian_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/utumnoPillar_obsidian_side.png")
    return self.build_block(top, side)

################################################################################
# Opaque tri-texture full blocks with orientation: #############################
################################################################################

@material(blockid=[<lotr:tile.hobbitOven>, <lotr:tile.dwarvenForge>, <lotr:tile.elvenForge>, <lotr:tile.orcForge>, <lotr:tile.alloyForge], data=range(6), solid=True)
def threeSidesOpaqueItems(self, blockid, data):
    # first, do the rotation if needed
    if self.rotation == 1:
        if data == 2: data = 5
        elif data == 3: data = 4
        elif data == 4: data = 2
        elif data == 5: data = 3
    elif self.rotation == 2:
        if data == 2: data = 3
        elif data == 3: data = 2
        elif data == 4: data = 5
        elif data == 5: data = 4
    elif self.rotation == 3:
        if data == 2: data = 4
        elif data == 3: data = 5
        elif data == 4: data = 3
        elif data == 5: data = 2
    if blockid == <lotr:tile.hobbitOven>:
        top   = self.load_image_texture("assets/lotr/textures/blocks/hobbitOven_top.png")
        side  = self.load_image_texture("assets/lotr/textures/blocks/hobbitOven_side.png")
        front = self.load_image_texture("assets/lotr/textures/blocks/hobbitOven_front.png")
    elif blockid == <lotr:tile.dwarvenForge>:
        top   = self.load_image_texture("assets/lotr/textures/blocks/dwarvenForge_top.png")
        side  = self.load_image_texture("assets/lotr/textures/blocks/dwarvenForge_side.png")
        front = self.load_image_texture("assets/lotr/textures/blocks/dwarvenForge_front.png")
    elif blockid == <lotr:tile.elvenForge>:
        top   = self.load_image_texture("assets/lotr/textures/blocks/elvenForge_top.png")
        side  = self.load_image_texture("assets/lotr/textures/blocks/elvenForge_side.png")
        front = self.load_image_texture("assets/lotr/textures/blocks/elvenForge_front.png")
    elif blockid == <lotr:tile.orcForge>:
        top   = self.load_image_texture("assets/lotr/textures/blocks/orcForge_top.png")
        side  = self.load_image_texture("assets/lotr/textures/blocks/orcForge_side.png")
        front = self.load_image_texture("assets/lotr/textures/blocks/orcForge_front.png")
    elif blockid == <lotr:tile.alloyForge>:
        top   = self.load_image_texture("assets/lotr/textures/blocks/alloyForge_top.png")
        side  = self.load_image_texture("assets/lotr/textures/blocks/alloyForge_side.png")
        front = self.load_image_texture("assets/lotr/textures/blocks/alloyForge_front.png")
    if data == 3: # pointing west
        return self.build_full_block(top, None, None, side, front)
    elif data == 4: # pointing north
        return self.build_full_block(top, None, None, front, side)
    else: # in any other direction the front can't be seen
        return self.build_full_block(top, None, None, side, side)

################################################################################
# Transparent single-texture full blocks with data value: ######################
################################################################################

@material(blockid=<lotr:tile.berryBush>, data=range(16), solid=True, transparent=True)
def berryBush(self, blockid, data):
    t = self.load_image_texture("assets/lotr/textures/blocks/berryBush_blueberry_bare.png")
    if data == 0:     # Blueberry Bush Bare
        t = self.load_image_texture("assets/lotr/textures/blocks/berryBush_blueberry_bare.png")
    elif data == 1:   # Blackberry Bush Bare
        t = self.load_image_texture("assets/lotr/textures/blocks/berryBush_blackberry_bare.png")
    elif data == 2:   # Raspberry Bush Bare
        t = self.load_image_texture("assets/lotr/textures/blocks/berryBush_raspberry_bare.png")
    elif data == 3:   # Cranberry Bush Bare
        t = self.load_image_texture("assets/lotr/textures/blocks/berryBush_cranberry_bare.png")
    elif data == 4:   # Elderberry Bush Bare
        t = self.load_image_texture("assets/lotr/textures/blocks/berryBush_elderberry_bare.png")
    elif data == 8:   # Blueberry Bush
        t = self.load_image_texture("assets/lotr/textures/blocks/berryBush_blueberry.png")
    elif data == 9:   # Blackberry Bush
        t = self.load_image_texture("assets/lotr/textures/blocks/berryBush_blackberry.png")
    elif data == 10:  # Raspberry Bush
        t = self.load_image_texture("assets/lotr/textures/blocks/berryBush_raspberry.png")
    elif data == 11:  # Cranberry Bush
        t = self.load_image_texture("assets/lotr/textures/blocks/berryBush_cranberry.png")
    elif data == 12:  # Elderberry Bush
        t = self.load_image_texture("assets/lotr/textures/blocks/berryBush_elderberry.png")
    return self.build_block(t, t)

################################################################################
# Transparent single texture sprites: ##########################################
################################################################################

@material(blockid=[<lotr:tile.sapling>,<lotr:tile.sapling2>,<lotr:tile.sapling3>,<lotr:tile.sapling4>,<lotr:tile.sapling5>,<lotr:tile.fruitSapling>,<lotr:tile.corruptMallorn>], data=range(16), transparent=True)
def lotr_saplings(self, blockid, data):
    # default sapling
    tex = self.load_image_texture("assets/minecraft/textures/blocks/sapling_oak.png")
    if blockid == <lotr:tile.sapling>:
        if data & 0x3 == 0: # Shire Pine Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling_shirePine.png")
        elif data & 0x3 == 1: # Mallorn Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling_mallorn.png")
        elif data & 0x3 == 2: # Mirk-oak Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling_mirkOak.png")
        elif data & 0x3 == 3: # Red Mirk-oak Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling_mirkOakRed.png")
    elif blockid == <lotr:tile.sapling2>:
        if data & 0x3 == 0: # Lebethron Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling2_lebethron.png")
        elif data & 0x3 == 1: # Beech Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling2_beech.png")
        elif data & 0x3 == 2: # Holly Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling2_holly.png")
        elif data & 0x3 == 3: # Banana Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling2_banana.png")
    elif blockid == <lotr:tile.sapling3>:
        if data & 0x3 == 0: # Maple Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling3_maple.png")
        elif data & 0x3 == 1: # Larch Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling3_larch.png")
        elif data & 0x3 == 2: # Date Palm Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling3_datePalm.png")
        elif data & 0x3 == 3: # Mangrove Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling3_mangrove.png")
    elif blockid == <lotr:tile.sapling4>:
        if data & 0x3 == 0: # Chestnut Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling4_chestnut.png")
        elif data & 0x3 == 1: # Baobab Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling4_baobab.png")
        elif data & 0x3 == 2: # Cedar Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling4_cedar.png")
        elif data & 0x3 == 3: # Fir Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling4_fir.png")
    elif blockid == <lotr:tile.sapling5>:
        if data & 0x3 == 0: # Pine Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/sapling5_pine.png")
    elif blockid == <lotr:tile.fruitSapling>:
        if data & 0x3 == 0: # Apple Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/fruitSapling_apple.png")
        elif data & 0x3 == 1: # Pear Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/fruitSapling_pear.png")
        elif data & 0x3 == 2: # Cherry Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/fruitSapling_cherry.png")
        elif data & 0x3 == 3: # Mango Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/fruitSapling_mango.png")
    elif blockid == <lotr:tile.corruptMallorn>:
        if data & 0x3 == 0: # Corrupt Mallorn Sapling
            tex = self.load_image_texture("assets/lotr/textures/blocks/corruptMallorn.png")
    return self.build_sprite(tex)

sprite(blockid=<lotr:tile.asphodel>, imagename="assets/lotr/textures/blocks/asphodel.png")
sprite(blockid=<lotr:tile.aridGrass>, imagename="assets/lotr/textures/blocks/aridGrass.png")
sprite(blockid=<lotr:tile.athelas>, imagename="assets/lotr/textures/blocks/athelas.png")
sprite(blockid=<lotr:tile.bluebell>, imagename="assets/lotr/textures/blocks/bluebell.png")
sprite(blockid=<lotr:tile.deadMarshPlant>, imagename="assets/lotr/textures/blocks/deadMarshPlant.png")
sprite(blockid=<lotr:tile.dwarfHerb>, imagename="assets/lotr/textures/blocks/dwarfHerb.png")
sprite(blockid=<lotr:tile.elanor>, imagename="assets/lotr/textures/blocks/elanor.png")
sprite(blockid=<lotr:tile.flaxPlant>, imagename="assets/lotr/textures/blocks/flaxPlant.png")
sprite(blockid=<lotr:tile.mordorGrass>, imagename="assets/lotr/textures/blocks/mordorGrass.png")
sprite(blockid=<lotr:tile.mordorThorn>, imagename="assets/lotr/textures/blocks/mordorThorn.png")
sprite(blockid=<lotr:tile.morgulShroom>, imagename="assets/lotr/textures/blocks/morgulShroom.png")
sprite(blockid=<lotr:tile.niphredil>, imagename="assets/lotr/textures/blocks/niphredil.png")
sprite(blockid=<lotr:tile.pipeweedPlant>, imagename="assets/lotr/textures/blocks/pipeweedPlant.png")
sprite(blockid=<lotr:tile.shireHeather>, imagename="assets/lotr/textures/blocks/shireHeather.png")
sprite(blockid=<lotr:tile.simbelmyne>, imagename="assets/lotr/textures/blocks/simbelmyne.png")
sprite(blockid=<lotr:tile.webUngoliant>, imagename="assets/lotr/textures/blocks/webUngoliant.png")

##### Caveat: a bit ugly but will do... #####
sprite(blockid=<lotr:tile.mug>, imagename="assets/lotr/textures/items/mug.png")

@material(blockid=<lotr:tile.mordorMoss>, data=range(16), transparent=True)
def mordorMoss(self, blockid, data):
    texture = self.load_image_texture("assets/lotr/textures/blocks/mordorMoss.png")
    return self.build_full_block((texture,15),texture,texture,texture,texture)

@material(blockid=<lotr:tile.fangornRiverweed>, data=range(16), transparent=True)
def fangornRiverweed(self, blockid, data):
    texture = self.load_image_texture("assets/lotr/textures/blocks/fangornRiverweed.png")
    return self.build_full_block((texture,15),texture,texture,texture,texture)

@material(blockid=<lotr:tile.thatchFloor>, data=range(16), transparent=True)
def thatchFloor(self, blockid, data):
    texture = self.load_image_texture("assets/lotr/textures/blocks/thatchFloor.png")
    return self.build_full_block((texture,15),texture,texture,texture,texture)

##### Caveat: a bit ugly but will do... #####
@material(blockid=<lotr:tile.plate>, data=range(16), transparent=True)
def lotr_plate(self, blockid, data):
    texture = self.load_image_texture("assets/lotr/textures/blocks/plate_top.png")
    return self.build_full_block((texture,15),texture,texture,texture,texture)

@material(blockid=<lotr:tile.pipeweed>, data=range(16), transparent=True)
def pipeweed(self, blockid, data):
    if data == 0 or data == 1:
        tex = self.load_image_texture("assets/lotr/textures/blocks/pipeweed_0.png")
    elif data == 2 or data == 3:
        tex = self.load_image_texture("assets/lotr/textures/blocks/pipeweed_1.png")
    elif data == 4 or data == 5 or data == 6:
        tex = self.load_image_texture("assets/lotr/textures/blocks/pipeweed_2.png")
    else:
        tex = self.load_image_texture("assets/lotr/textures/blocks/pipeweed_3.png")
    return self.build_sprite(tex)

@material(blockid=<lotr:tile.lettuce>, data=range(16), transparent=True)
def lettuce(self, blockid, data):
    if data == 0 or data == 1:
        tex = self.load_image_texture("assets/lotr/textures/blocks/lettuce_0.png")
    elif data == 2 or data == 3:
        tex = self.load_image_texture("assets/lotr/textures/blocks/lettuce_1.png")
    elif data == 4 or data == 5 or data == 6:
        tex = self.load_image_texture("assets/lotr/textures/blocks/lettuce_2.png")
    else:
        tex = self.load_image_texture("assets/lotr/textures/blocks/lettuce_3.png")
    return self.build_sprite(tex)

@material(blockid=<lotr:tile.flax>, data=range(16), transparent=True)
def flax(self, blockid, data):
    if data == 0 or data == 1:
        tex = self.load_image_texture("assets/lotr/textures/blocks/flax_0.png")
    elif data == 2 or data == 3:
        tex = self.load_image_texture("assets/lotr/textures/blocks/flax_1.png")
    elif data == 4 or data == 5 or data == 6:
        tex = self.load_image_texture("assets/lotr/textures/blocks/flax_2.png")
    else:
        tex = self.load_image_texture("assets/lotr/textures/blocks/flaxPlant.png")
    return self.build_sprite(tex)

@material(blockid=<lotr:tile.fangornPlant>, data=range(6), transparent=True)
def fangornPlant(self, blockid, data):
    if data == 0:    # Tears of Yavanna
        tex = self.load_image_texture("assets/lotr/textures/blocks/fangornPlant_green.png")
    elif data == 1:  # Fangorn's Beard
        tex = self.load_image_texture("assets/lotr/textures/blocks/fangornPlant_brown.png")
    elif data == 2:  # Huorn Leaf
        tex = self.load_image_texture("assets/lotr/textures/blocks/fangornPlant_gold.png")
    elif data == 3:  # Elfsong
        tex = self.load_image_texture("assets/lotr/textures/blocks/fangornPlant_yellow.png")
    elif data == 4:  # Sunfruit
        tex = self.load_image_texture("assets/lotr/textures/blocks/fangornPlant_red.png")
    elif data == 5:  # Moonflower
        tex = self.load_image_texture("assets/lotr/textures/blocks/fangornPlant_silver.png")
    return self.build_sprite(tex)

@material(blockid=<lotr:tile.haradFlower>, data=range(4), transparent=True)
def haradFlower(self, blockid, data):
    if data == 0:    #  Red Sand Gem
        tex = self.load_image_texture("assets/lotr/textures/blocks/haradFlower_red.png")
    elif data == 1:  #  Yellow Sand Gem
        tex = self.load_image_texture("assets/lotr/textures/blocks/haradFlower_yellow.png")
    elif data == 2:  #  Harad Daisy
        tex = self.load_image_texture("assets/lotr/textures/blocks/haradFlower_daisy.png")
    elif data == 3:  # Southbells
        tex = self.load_image_texture("assets/lotr/textures/blocks/haradFlower_pink.png")
    return self.build_sprite(tex)

@material(blockid=[<lotr:tile.orcTorch>, <lotr:tile.tauredainDoubleTorch>], data=range(2), transparent=True)
def tallTorch(self, blockid, data):
    if blockid == <lotr:tile.orcTorch>:
        if data == 0:
            tex = self.load_image_texture("assets/lotr/textures/blocks/orcTorch_bottom.png")
        elif data == 1:
            tex = self.load_image_texture("assets/lotr/textures/blocks/orcTorch_top.png")
    elif blockid == <lotr:tile.tauredainDoubleTorch>:
        if data == 0:
            tex = self.load_image_texture("assets/lotr/textures/blocks/tauredainDoubleTorch_bottom.png")
        elif data == 1:
            tex = self.load_image_texture("assets/lotr/textures/blocks/tauredainDoubleTorch_top.png")
    return self.build_sprite(tex)

################################################################################
# Transparent bi texture sprites: ##############################################
################################################################################

##### Caveat: the top part of Flame of Harad and Hibiscus have the same data value than Yellow Iris, so they all have yellow tops #####
@material(blockid=<lotr:tile.doubleFlower>, data=range(16), transparent=True)
def lotr_double_flowers(self, blockid, data):
    if data & 0x8:
        part = "top"
    else:
        part = "bottom"
    if data == 1 or data == 8:
        plant = "yellowIris"
    elif data == 2 or data == 9:
        plant = "pink"
    elif data == 3 or data == 10:
        plant = "red"
    else: # error!
        plant = "red"
    png = "assets/lotr/textures/blocks/doubleFlower_%s_%s.png" % (plant,part)
    texture = self.load_image_texture(png)
    img = self.build_billboard(texture)
    return img

################################################################################
# Weirdoes ######################################################################
################################################################################

@material(blockid=[<lotr:tile.stairsPine>, <lotr:tile.stairsMordorBrick>, <lotr:tile.stairsGondorBrick>, <lotr:tile.stairsMallorn>, <lotr:tile.stairsGondorBrickMossy>, <lotr:tile.stairsGondorBrickCracked>, <lotr:tile.stairsRohanBrick>, <lotr:tile.stairsDwarvenBrick>, <lotr:tile.stairsApple>, <lotr:tile.stairsPear>, <lotr:tile.stairsCherry>, <lotr:tile.stairsMirkOak>, <lotr:tile.stairsCharred>, <lotr:tile.stairsLebethron>, <lotr:tile.stairsBeech>, <lotr:tile.stairsMordorBrickCracked>, <lotr:tile.stairsElvenBrick>, <lotr:tile.stairsElvenBrickMossy>, <lotr:tile.stairsElvenBrickCracked>, <lotr:tile.stairsHolly>, <lotr:tile.stairsBlueRockBrick>, <lotr:tile.stairsAngmarBrick>, <lotr:tile.stairsAngmarBrickCracked>, <lotr:tile.stairsMango>, <lotr:tile.stairsBanana>, <lotr:tile.stairsMaple>, <lotr:tile.stairsLarch>, <lotr:tile.stairsRedRockBrick>, <lotr:tile.stairsNearHaradBrick>, <lotr:tile.stairsDatePalm>, <lotr:tile.stairsThatch>, <lotr:tile.stairsArnorBrick>, <lotr:tile.stairsArnorBrickMossy>, <lotr:tile.stairsArnorBrickCracked>, <lotr:tile.stairsUrukBrick>, <lotr:tile.stairsDolGuldurBrick>, <lotr:tile.stairsDolGuldurBrickCracked>, <lotr:tile.stairsMangrove>, <lotr:tile.stairsChestnut>, <lotr:tile.stairsBaobab>, <lotr:tile.stairsCedar>, <lotr:tile.stairsBlackGondorBrick>, <lotr:tile.stairsHighElvenBrick>, <lotr:tile.stairsHighElvenBrickMossy>, <lotr:tile.stairsHighElvenBrickCracked>, <lotr:tile.stairsWoodElvenBrick>, <lotr:tile.stairsWoodElvenBrickMossy>, <lotr:tile.stairsWoodElvenBrickCracked>, <lotr:tile.stairsDolAmrothBrick>, <lotr:tile.stairsFir>, <lotr:tile.stairsPinePine>, <lotr:tile.stairsMoredainBrick>, <lotr:tile.stairsNearHaradBrickCracked>, <lotr:tile.stairsRedSandstone>, <lotr:tile.stairsRotten>, <lotr:tile.stairsScorchedStone>, <lotr:tile.stairsLemon>, <lotr:tile.stairsOrange>, <lotr:tile.stairsLime>, <lotr:tile.stairsTauredainBrick>, <lotr:tile.stairsTauredainBrickMossy>, <lotr:tile.stairsTauredainBrickCracked>, <lotr:tile.stairsTauredainBrickGold>, <lotr:tile.stairsTauredainBrickObsidian>, <lotr:tile.stairsMahogany>, <lotr:tile.stairsNearHaradBrickRedCracked>, <lotr:tile.stairsNearHaradBrickRed>, <lotr:tile.stairsDwarvenBrickCracked>, <lotr:tile.stairsReed>], data=range(128), transparent=True, solid=True, nospawn=True)
def lotr_stairs(self, blockid, data):
    # preserve the upside-down bit
    upside_down = data & 0x4

    # find solid quarters within the top or bottom half of the block
    #                   NW           NE           SE           SW
    quarters = [data & 0x8, data & 0x10, data & 0x20, data & 0x40]

    # rotate the quarters so we can pretend northdirection is always upper-left
    numpy.roll(quarters, [0,1,3,2][self.rotation])
    nw,ne,se,sw = quarters

    if blockid == <lotr:tile.stairsPine>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_shirePine.png").copy()
    elif blockid == <lotr:tile.stairsMordorBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick_mordor.png").copy()
    elif blockid == <lotr:tile.stairsGondorBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick_gondor.png").copy()
    elif blockid == <lotr:tile.stairsMallorn>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_mallorn.png").copy()
    elif blockid == <lotr:tile.stairsGondorBrickMossy>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick_gondorMossy.png").copy()
    elif blockid == <lotr:tile.stairsGondorBrickCracked>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick_gondorCracked.png").copy()
    elif blockid == <lotr:tile.stairsRohanBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick_rohan.png").copy()
    elif blockid == <lotr:tile.stairsDwarvenBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick_dwarven.png").copy()
    elif blockid == <lotr:tile.stairsApple>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_apple.png").copy()
    elif blockid == <lotr:tile.stairsPear>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_pear.png").copy()
    elif blockid == <lotr:tile.stairsCherry>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_cherry.png").copy()
    elif blockid == <lotr:tile.stairsMirkOak>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_mirkOak.png").copy()
    elif blockid == <lotr:tile.stairsCharred>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_charred.png").copy()
    elif blockid == <lotr:tile.stairsLebethron>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_lebethron.png").copy()
    elif blockid == <lotr:tile.stairsBeech>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_beech.png").copy()
    elif blockid == <lotr:tile.stairsMordorBrickCracked>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick_mordorCracked.png").copy()
    elif blockid == <lotr:tile.stairsElvenBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick_galadhrim.png").copy()
    elif blockid == <lotr:tile.stairsElvenBrickMossy>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick_galadhrimMossy.png").copy()
    elif blockid == <lotr:tile.stairsElvenBrickCracked>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick_galadhrimCracked.png").copy()
    elif blockid == <lotr:tile.stairsHolly>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_holly.png").copy()
    elif blockid == <lotr:tile.stairsBlueRockBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick_blueRock.png").copy()
    elif blockid == <lotr:tile.stairsAngmarBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick2_angmar.png").copy()
    elif blockid == <lotr:tile.stairsAngmarBrickCracked>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick2_angmarCracked.png").copy()
    elif blockid == <lotr:tile.stairsMango>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_mango.png").copy()
    elif blockid == <lotr:tile.stairsBanana>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_banana.png").copy()
    elif blockid == <lotr:tile.stairsMaple>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_maple.png").copy()
    elif blockid == <lotr:tile.stairsLarch>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_larch.png").copy()
    elif blockid == <lotr:tile.stairsRedRockBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick2_redRock.png").copy()
    elif blockid == <lotr:tile.stairsNearHaradBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick_nearHarad.png").copy()
    elif blockid == <lotr:tile.stairsDatePalm>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_datePalm.png").copy()
    elif blockid == <lotr:tile.stairsThatch>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/thatch.png").copy()
    elif blockid == <lotr:tile.stairsArnorBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick2_arnor.png").copy()
    elif blockid == <lotr:tile.stairsArnorBrickMossy>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick2_arnorMossy.png").copy()
    elif blockid == <lotr:tile.stairsArnorBrickCracked>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick2_arnorCracked.png").copy()
    elif blockid == <lotr:tile.stairsUrukBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick2_uruk.png").copy()
    elif blockid == <lotr:tile.stairsDolGuldurBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick2_dolGuldur.png").copy()
    elif blockid == <lotr:tile.stairsDolGuldurBrickCracked>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick2_dolGuldurCracked.png").copy()
    elif blockid == <lotr:tile.stairsMangrove>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks_mangrove.png").copy()
    elif blockid == <lotr:tile.stairsChestnut>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks2_chestnut.png").copy()
    elif blockid == <lotr:tile.stairsBaobab>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks2_baobab.png").copy()
    elif blockid == <lotr:tile.stairsCedar>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks2_cedar.png").copy()
    elif blockid == <lotr:tile.stairsBlackGondorBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick2_blackGondor.png").copy()
    elif blockid == <lotr:tile.stairsHighElvenBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick3_highElven.png").copy()
    elif blockid == <lotr:tile.stairsHighElvenBrickMossy>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick3_highElvenMossy.png").copy()
    elif blockid == <lotr:tile.stairsHighElvenBrickCracked>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick3_highElvenCracked.png").copy()
    elif blockid == <lotr:tile.stairsWoodElvenBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick3_woodElven.png").copy()
    elif blockid == <lotr:tile.stairsWoodElvenBrickMossy>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick3_woodElvenMossy.png").copy()
    elif blockid == <lotr:tile.stairsWoodElvenBrickCracked>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick3_woodElvenCracked.png").copy()
    elif blockid == <lotr:tile.stairsDolAmrothBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick3_dolAmroth.png").copy()
    elif blockid == <lotr:tile.stairsFir>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks2_fir.png").copy()
    elif blockid == <lotr:tile.stairsPinePine>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks2_pine.png").copy()
    elif blockid == <lotr:tile.stairsMoredainBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick3_moredain.png").copy()
    elif blockid == <lotr:tile.stairsNearHaradBrickCracked>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick3_nearHaradCracked.png").copy()
    elif blockid == <lotr:tile.stairsRedSandstone>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/redSandstone.png").copy()
    elif blockid == <lotr:tile.stairsRotten>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planksRotten_rotten.png").copy()
    elif blockid == <lotr:tile.stairsScorchedStone>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/scorchedStone.png").copy()
    elif blockid == <lotr:tile.stairsLemon>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks2_lemon.png").copy()
    elif blockid == <lotr:tile.stairsOrange>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks2_orange.png").copy()
    elif blockid == <lotr:tile.stairsLime>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks2_lime.png").copy()
    elif blockid == <lotr:tile.stairsTauredainBrick>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick4_tauredain.png").copy()
    elif blockid == <lotr:tile.stairsTauredainBrickCracked>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick4_tauredainCracked.png").copy()
    elif blockid == <lotr:tile.stairsTauredainBrickMossy>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick4_tauredainMossy.png").copy()
    elif blockid == <lotr:tile.stairsTauredainBrickGold>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick4_tauredainGold.png").copy()
    elif blockid == <lotr:tile.stairsTauredainBrickObsidian>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick4_tauredainObsidian.png").copy()
    elif blockid == <lotr:tile.stairsMahogany>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/planks2_mahogany.png").copy()
    elif blockid == <lotr:tile.stairsNearHaradBrickRed>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick3_nearHaradRed.png").copy()
    elif blockid == <lotr:tile.stairsNearHaradBrickRedCracked>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick3_nearHaradRedCracked.png").copy()
    elif blockid == <lotr:tile.stairsDwarvenBrickCracked>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/brick4_dwarvenCracked.png").copy()
    elif blockid == <lotr:tile.stairsReed>:
        texture = self.load_image_texture("assets/lotr/textures/blocks/thatch_reed.png").copy()

    outside_l = texture.copy()
    outside_r = texture.copy()
    inside_l = texture.copy()
    inside_r = texture.copy()

    slab_top = texture.copy()

    push = 8 if upside_down else 0

    def rect(tex,coords):
        ImageDraw.Draw(tex).rectangle(coords,outline=(0,0,0,0),fill=(0,0,0,0))

    # cut out top or bottom half from inner surfaces
    rect(inside_l, (0,8-push,15,15-push))
    rect(inside_r, (0,8-push,15,15-push))

    # cut out missing or obstructed quarters from each surface
    if not nw:
        rect(outside_l, (0,push,7,7+push))
        rect(texture, (0,0,7,7))
    if not nw or sw:
        rect(inside_r, (8,push,15,7+push)) # will be flipped
    if not ne:
        rect(texture, (8,0,15,7))
    if not ne or nw:
        rect(inside_l, (0,push,7,7+push))
    if not ne or se:
        rect(inside_r, (0,push,7,7+push)) # will be flipped
    if not se:
        rect(outside_r, (0,push,7,7+push)) # will be flipped
        rect(texture, (8,8,15,15))
    if not se or sw:
        rect(inside_l, (8,push,15,7+push))
    if not sw:
        rect(outside_l, (8,push,15,7+push))
        rect(outside_r, (8,push,15,7+push)) # will be flipped
        rect(texture, (0,8,7,15))

    img = Image.new("RGBA", (24,24), self.bgcolor)

    if upside_down:
        # top should have no cut-outs after all
        texture = slab_top
    else:
        # render the slab-level surface
        slab_top = self.transform_image_top(slab_top)
        alpha_over(img, slab_top, (0,6))

    # render inner left surface
    inside_l = self.transform_image_side(inside_l)
    # Darken the vertical part of the second step
    sidealpha = inside_l.split()[3]
    # darken it a bit more than usual, looks better
    inside_l = ImageEnhance.Brightness(inside_l).enhance(0.8)
    inside_l.putalpha(sidealpha)
    alpha_over(img, inside_l, (6,3))

    # render inner right surface
    inside_r = self.transform_image_side(inside_r).transpose(Image.FLIP_LEFT_RIGHT)
    # Darken the vertical part of the second step
    sidealpha = inside_r.split()[3]
    # darken it a bit more than usual, looks better
    inside_r = ImageEnhance.Brightness(inside_r).enhance(0.7)
    inside_r.putalpha(sidealpha)
    alpha_over(img, inside_r, (6,3))

    # render outer surfaces
    alpha_over(img, self.build_full_block(texture, None, None, outside_l, outside_r))

    return img

@material(blockid=[<lotr:tile.orcSteelBars>, <lotr:tile.bronzeBars>, <lotr:tile.goldBars>, <lotr:tile.silverBars>, <lotr:tile.mithrilBars>, <lotr:tile.urukBars>, <lotr:tile.highElfBars>, <lotr:tile.galadhrimBars>, <lotr:tile.woodElfBars>, <lotr:tile.dwarfBars>, <lotr:tile.blueDwarfBars>, <lotr:tile.highElfWoodBars>, <lotr:tile.galadhrimWoodBars>, <lotr:tile.woodElfWoodBars>], data=range(256), transparent=True, nospawn=True)
def lotr_bars(self, blockid, data):
    # no rotation, uses pseudo data
    if blockid == <lotr:tile.orcSteelBars>:
        t = self.load_image_texture("assets/lotr/textures/blocks/orcSteelBars.png")
    elif blockid == <lotr:tile.bronzeBars>:
        t = self.load_image_texture("assets/lotr/textures/blocks/bronzeBars.png")
    elif blockid == <lotr:tile.goldBars>:
        t = self.load_image_texture("assets/lotr/textures/blocks/goldBars.png")
    elif blockid == <lotr:tile.silverBars>:
        t = self.load_image_texture("assets/lotr/textures/blocks/silverBars.png")
    elif blockid == <lotr:tile.mithrilBars>:
        t = self.load_image_texture("assets/lotr/textures/blocks/mithrilBars.png")
    elif blockid == <lotr:tile.urukBars>:
        t = self.load_image_texture("assets/lotr/textures/blocks/urukBars.png")
    elif blockid == <lotr:tile.highElfBars>:
        t = self.load_image_texture("assets/lotr/textures/blocks/highElfBars.png")
    elif blockid == <lotr:tile.galadhrimBars>:
        t = self.load_image_texture("assets/lotr/textures/blocks/galadhrimBars.png")
    elif blockid == <lotr:tile.woodElfBars>:
        t = self.load_image_texture("assets/lotr/textures/blocks/woodElfBars.png")
    elif blockid == <lotr:tile.dwarfBars>:
        t = self.load_image_texture("assets/lotr/textures/blocks/dwarfBars.png")
    elif blockid == <lotr:tile.blueDwarfBars>:
        t = self.load_image_texture("assets/lotr/textures/blocks/blueDwarfBars.png")
    elif blockid == <lotr:tile.highElfWoodBars>:
        t = self.load_image_texture("assets/lotr/textures/blocks/highElfWoodBars.png")
    elif blockid == <lotr:tile.galadhrimWoodBars>:
        t = self.load_image_texture("assets/lotr/textures/blocks/galadhrimWoodBars.png")
    elif blockid == <lotr:tile.woodElfWoodBars>:
        t = self.load_image_texture("assets/lotr/textures/blocks/woodElfWoodBars.png")
    left = t.copy()
    right = t.copy()
    # generate the four small pieces of the glass pane
    ImageDraw.Draw(right).rectangle((0,0,7,15),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(left).rectangle((8,0,15,15),outline=(0,0,0,0),fill=(0,0,0,0))
    up_left = self.transform_image_side(left)
    up_right = self.transform_image_side(right).transpose(Image.FLIP_TOP_BOTTOM)
    dw_right = self.transform_image_side(right)
    dw_left = self.transform_image_side(left).transpose(Image.FLIP_TOP_BOTTOM)
    # Create img to compose the texture
    img = Image.new("RGBA", (24,24), self.bgcolor)
    # +x axis points top right direction
    # +y axis points bottom right direction
    # First compose things in the back of the image, 
    # then things in the front.
    # the lower 4 bits encode color, the upper 4 encode adjencies
    data = data >> 4
    if (data & 0b0001) == 1 or data == 0:
        alpha_over(img,up_left, (6,3),up_left)    # top left
    if (data & 0b1000) == 8 or data == 0:
        alpha_over(img,up_right, (6,3),up_right)  # top right
    if (data & 0b0010) == 2 or data == 0:
        alpha_over(img,dw_left, (6,3),dw_left)    # bottom left    
    if (data & 0b0100) == 4 or data == 0:
        alpha_over(img,dw_right, (6,3),dw_right)  # bottom right
    return img

@material(blockid=[<lotr:tile.woodSlabSingle>, <lotr:tile.woodSlabDouble>, <lotr:tile.woodSlabSingle2>, <lotr:tile.woodSlabDouble2>, <lotr:tile.woodSlabSingle3>, <lotr:tile.woodSlabDouble3>, <lotr:tile.slabSingle>, <lotr:tile.slabDouble>, <lotr:tile.slabSingle2>, <lotr:tile.slabDouble2>, <lotr:tile.slabSingle3>, <lotr:tile.slabDouble3>, <lotr:tile.slabSingle4>, <lotr:tile.slabDouble4>, <lotr:tile.slabSingle5>, <lotr:tile.slabDouble5>, <lotr:tile.slabSingle6>, <lotr:tile.slabDouble6>, <lotr:tile.slabSingle7>, <lotr:tile.slabDouble7>, <lotr:tile.slabSingleThatch>, <lotr:tile.slabDoubleThatch>, <lotr:tile.rottenSlabSingle>, <lotr:tile.rottenSlabDouble>, <lotr:tile.scorchedSlabSingle>, <lotr:tile.scorchedSlabDouble>], data=range(16), transparent=(44,), solid=True)
def lotr_slabs(self, blockid, data):
    t = data & 7
    top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_shirePine.png")
    if blockid == <lotr:tile.woodSlabSingle> or blockid == <lotr:tile.woodSlabDouble>:
        if t == 0:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_shirePine.png")
	elif t == 1:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_mallorn.png")
	elif t == 2:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_mirkOak.png")
	elif t == 3:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_charred.png")
	elif t == 4:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_apple.png")
	elif t == 5:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_pear.png")
	elif t == 6:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_cherry.png")
	elif t == 7:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_mango.png")
    elif blockid == <lotr:tile.woodSlabSingle2> or blockid == <lotr:tile.woodSlabDouble2>:
        if t == 0:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_lebethron.png")
	elif t == 1:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_beech.png")
	elif t == 2:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_holly.png")
	elif t == 3:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_banana.png")
	elif t == 4:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_maple.png")
	elif t == 5:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_larch.png")
	elif t == 6:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_datePalm.png")
	elif t == 7:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks_mangrove.png")
    elif blockid == <lotr:tile.woodSlabSingle3> or blockid == <lotr:tile.woodSlabDouble3>:
        if t == 0:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks2_chestnut.png")
	elif t == 1:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks2_baobab.png")
	elif t == 2:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks2_cedar.png")
	elif t == 3:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks2_fir.png")
	elif t == 4:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planks2_pine.png")
    elif blockid == <lotr:tile.slabSingle> or blockid == <lotr:tile.slabDouble>:
        if t == 0:
            top  = self.load_image_texture("assets/lotr/textures/blocks/slab_mordorRock_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/slab_mordorRock_side.png")
	elif t == 1:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick_mordor.png")
	elif t == 2:
            top  = self.load_image_texture("assets/lotr/textures/blocks/slab_gondorRock_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/slab_gondorRock_side.png")
	elif t == 3:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick_gondor.png")
	elif t == 4:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick_gondorMossy.png")
	elif t == 5:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick_gondorCracked.png")
	elif t == 6:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick_rohan.png")
	elif t == 7:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick_dwarven.png")
    elif blockid == <lotr:tile.slabSingle2> or blockid == <lotr:tile.slabDouble2>:
        if t == 0:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_dwarven_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_dwarven_sideBottom.png")
	elif t == 1:
            top  = self.load_image_texture("assets/lotr/textures/blocks/slab_rohanRock_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/slab_rohanRock_side.png")
	elif t == 2:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick_mordorCracked.png")
	elif t == 3:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick_galadhrim.png")
	elif t == 4:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick_galadhrimMossy.png")
	elif t == 5:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick_galadhrimCracked.png")
	elif t == 6:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_galadhrim_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_galadhrim_sideBottom.png")
	elif t == 7:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_galadhrimCracked_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_galadhrimCracked_sideBottom.png")
    elif blockid == <lotr:tile.slabSingle3> or blockid == <lotr:tile.slabDouble3>:
        if t == 0:
            top  = self.load_image_texture("assets/lotr/textures/blocks/slab_blueRock_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/slab_blueRock_side.png")
	elif t == 1:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick_blueRock.png")
	elif t == 2:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_blueRock_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_blueRock_sideBottom.png")
	elif t == 3:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick2_angmar.png")
	elif t == 4:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick2_angmarCracked.png")
	elif t == 5:
            top  = self.load_image_texture("assets/lotr/textures/blocks/slab_redRock_top.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/slab_redRock_side.png")
	elif t == 6:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick2_redRock.png")
	elif t == 7:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_redRock_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_redRock_sideBottom.png")
    elif blockid == <lotr:tile.slabSingle4> or blockid == <lotr:tile.slabDouble4>:
        if t == 0:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick_nearHarad.png")
	elif t == 1:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick2_arnor.png")
	elif t == 2:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick2_arnorMossy.png")
	elif t == 3:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick2_arnorCracked.png")
	elif t == 4:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick2_uruk.png")
	elif t == 5:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick2_dolGuldur.png")
	elif t == 6:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick2_dolGuldurCracked.png")
	elif t == 7:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_nearHarad_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_nearHarad_sideBottom.png")
    elif blockid == <lotr:tile.slabSingle5> or blockid == <lotr:tile.slabDouble5>:
        if t == 0:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_gondor_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_gondor_sideBottom.png")
	elif t == 1:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_mordor_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_mordor_sideBottom.png")
	elif t == 2:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_rohan_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_rohan_sideBottom.png")
	elif t == 3:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick2_blackGondor.png")
	elif t == 4:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_blackGondor_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_blackGondor_sideBottom.png")
	elif t == 5:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick3_highElven.png")
	elif t == 6:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick3_highElvenMossy.png")
	elif t == 7:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick3_highElvenCracked.png")
    elif blockid == <lotr:tile.slabSingle6> or blockid == <lotr:tile.slabDouble6>:
        if t == 0:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_highElven_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_highElven_sideBottom.png")
	elif t == 1:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_highElvenCracked_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_highElvenCracked_sideBottom.png")
	elif t == 2:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick3_woodElven.png")
	elif t == 3:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick3_woodElvenMossy.png")
	elif t == 4:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick3_woodElvenCracked.png")
	elif t == 5:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_woodElven_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_woodElven_sideBottom.png")
	elif t == 6:
            top  = self.load_image_texture("assets/lotr/textures/blocks/pillar_woodElvenCracked_face.png")
            side = self.load_image_texture("assets/lotr/textures/blocks/pillar_woodElvenCracked_sideBottom.png")
	elif t == 7:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick3_dolAmroth.png")
    elif blockid == <lotr:tile.slabSingle7> or blockid == <lotr:tile.slabDouble7>:
        if t == 0:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick3_moredain.png")
	elif t == 1:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/brick3_nearHaradCracked.png")
    elif blockid == <lotr:tile.slabSingleThatch> or blockid == <lotr:tile.slabDoubleThatch>:
        if t == 0:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/thatch.png")
    elif blockid == <lotr:tile.rottenSlabSingle> or blockid == <lotr:tile.rottenSlabDouble>:
        if t == 0:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/planksRotten_rotten.png")
    elif blockid == <lotr:tile.scorchedSlabSingle> or blockid == <lotr:tile.scorchedSlabDouble>:
        if t == 0:
            top = side = self.load_image_texture("assets/lotr/textures/blocks/scorchedStone.png")
    else:
        return None
    
    # double slabs:
    if blockid == <lotr:tile.woodSlabDouble> or blockid == <lotr:tile.woodSlabDouble2> or blockid == <lotr:tile.woodSlabDouble3> or blockid == <lotr:tile.slabDouble> or blockid == <lotr:tile.slabDouble2> or blockid == <lotr:tile.slabDouble3> or blockid == <lotr:tile.slabDouble4> or blockid == <lotr:tile.slabDouble5> or blockid == <lotr:tile.slabDouble6> or blockid == <lotr:tile.slabDouble7> or blockid == <lotr:tile.slabDoubleThatch> or blockid == <lotr:tile.rottenSlabDouble>:
        return self.build_block(top, side)
    
    # cut the side texture in half
    mask = side.crop((0,8,16,16))
    side = Image.new(side.mode, side.size, self.bgcolor)
    alpha_over(side, mask,(0,0,16,8), mask)
    
    # plain slab
    top = self.transform_image_top(top)
    side = self.transform_image_side(side)
    otherside = side.transpose(Image.FLIP_LEFT_RIGHT)
    
    sidealpha = side.split()[3]
    side = ImageEnhance.Brightness(side).enhance(0.9)
    side.putalpha(sidealpha)
    othersidealpha = otherside.split()[3]
    otherside = ImageEnhance.Brightness(otherside).enhance(0.8)
    otherside.putalpha(othersidealpha)
    
    # upside down slab
    delta = 0
    if data & 8 == 8:
        delta = 6
    
    img = Image.new("RGBA", (24,24), self.bgcolor)
    alpha_over(img, side, (0,12 - delta), side)
    alpha_over(img, otherside, (12,12 - delta), otherside)
    alpha_over(img, top, (0,6 - delta), top)
    
    return img

@material(blockid=[<lotr:tile.wallStone>, <lotr:tile.wallStone2>, <lotr:tile.wallStone3>, <lotr:tile.scorchedWall>], data=range(32), transparent=True, nospawn=True)
def lotr_walls(self, blockid, data):
    t = self.load_image_texture("assets/minecraft/textures/blocks/cobblestone.png").copy()
    if blockid == <lotr:tile.wallStone>:
        if data == 0:
            t = self.load_image_texture("assets/lotr/textures/blocks/rock_mordor.png").copy()
        elif data == 1:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick_mordor.png").copy()
        elif data == 2:
            t = self.load_image_texture("assets/lotr/textures/blocks/rock_gondor.png").copy()
        elif data == 3:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick_gondor.png").copy()
        elif data == 4:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick_gondorMossy.png").copy()
        elif data == 5:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick_gondorCracked.png").copy()
        elif data == 6:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick_rohan.png").copy()
        elif data == 7:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick_dwarven.png").copy()
        elif data == 8:
            t = self.load_image_texture("assets/lotr/textures/blocks/rock_rohan.png").copy()
        elif data == 9:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick_mordorCracked.png").copy()
        elif data == 10:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick_galadhrim.png").copy()
        elif data == 11:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick_galadhrimMossy.png").copy()
        elif data == 12:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick_galadhrimCracked.png").copy()
        elif data == 13:
            t = self.load_image_texture("assets/lotr/textures/blocks/rock_blue.png").copy()
        elif data == 14:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick_blueRock.png").copy()
        elif data == 15:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick_nearHarad.png").copy()
    elif blockid == <lotr:tile.wallStone2>:
        if data == 0:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick2_angmar.png").copy()
        elif data == 1:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick2_angmarCracked.png").copy()
        elif data == 2:
            t = self.load_image_texture("assets/lotr/textures/blocks/rock_red.png").copy()
        elif data == 3:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick2_redRock.png").copy()
        elif data == 4:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick2_arnor.png").copy()
        elif data == 5:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick2_arnorMossy.png").copy()
        elif data == 6:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick2_arnorCracked.png").copy()
        elif data == 7:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick2_uruk.png").copy()
        elif data == 8:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick2_dolGuldur.png").copy()
        elif data == 9:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick2_dolGuldurCracked.png").copy()
        elif data == 10:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick2_blackGondor.png").copy()
        elif data == 11:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick3_highElven.png").copy()
        elif data == 12:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick3_highElvenMossy.png").copy()
        elif data == 13:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick3_highElvenCracked.png").copy()
        elif data == 14:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick3_dolAmroth.png").copy()
        elif data == 15:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick3_moredain.png").copy()
    elif blockid == <lotr:tile.wallStone3>:
        if data == 0:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick3_woodElven.png").copy()
        elif data == 1:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick3_woodElvenMossy.png").copy()
        elif data == 2:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick3_woodElvenCracked.png").copy()
        elif data == 3:
            t = self.load_image_texture("assets/lotr/textures/blocks/brick3_nearHaradCracked.png").copy()
    elif blockid == <lotr:tile.scorchedWall>:
        t = self.load_image_texture("assets/lotr/textures/blocks/scorchedStone.png").copy()

    wall_pole_top = t.copy()
    wall_pole_side = t.copy()
    wall_side_top = t.copy()
    wall_side = t.copy()
    # _full is used for walls without pole
    wall_side_top_full = t.copy()
    wall_side_full = t.copy()

    # generate the textures of the wall
    ImageDraw.Draw(wall_pole_top).rectangle((0,0,3,15),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(wall_pole_top).rectangle((12,0,15,15),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(wall_pole_top).rectangle((0,0,15,3),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(wall_pole_top).rectangle((0,12,15,15),outline=(0,0,0,0),fill=(0,0,0,0))

    ImageDraw.Draw(wall_pole_side).rectangle((0,0,3,15),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(wall_pole_side).rectangle((12,0,15,15),outline=(0,0,0,0),fill=(0,0,0,0))

    # Create the sides and the top of the pole
    wall_pole_side = self.transform_image_side(wall_pole_side)
    wall_pole_other_side = wall_pole_side.transpose(Image.FLIP_LEFT_RIGHT)
    wall_pole_top = self.transform_image_top(wall_pole_top)

    # Darken the sides slightly. These methods also affect the alpha layer,
    # so save them first (we don't want to "darken" the alpha layer making
    # the block transparent)
    sidealpha = wall_pole_side.split()[3]
    wall_pole_side = ImageEnhance.Brightness(wall_pole_side).enhance(0.8)
    wall_pole_side.putalpha(sidealpha)
    othersidealpha = wall_pole_other_side.split()[3]
    wall_pole_other_side = ImageEnhance.Brightness(wall_pole_other_side).enhance(0.7)
    wall_pole_other_side.putalpha(othersidealpha)

    # Compose the wall pole
    wall_pole = Image.new("RGBA", (24,24), self.bgcolor)
    alpha_over(wall_pole,wall_pole_side, (3,4),wall_pole_side)
    alpha_over(wall_pole,wall_pole_other_side, (9,4),wall_pole_other_side)
    alpha_over(wall_pole,wall_pole_top, (0,0),wall_pole_top)
    
    # create the sides and the top of a wall attached to a pole
    ImageDraw.Draw(wall_side).rectangle((0,0,15,2),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(wall_side).rectangle((0,0,11,15),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(wall_side_top).rectangle((0,0,11,15),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(wall_side_top).rectangle((0,0,15,4),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(wall_side_top).rectangle((0,11,15,15),outline=(0,0,0,0),fill=(0,0,0,0))
    # full version, without pole
    ImageDraw.Draw(wall_side_full).rectangle((0,0,15,2),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(wall_side_top_full).rectangle((0,4,15,15),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(wall_side_top_full).rectangle((0,4,15,15),outline=(0,0,0,0),fill=(0,0,0,0))

    # compose the sides of a wall atached to a pole
    tmp = Image.new("RGBA", (24,24), self.bgcolor)
    wall_side = self.transform_image_side(wall_side)
    wall_side_top = self.transform_image_top(wall_side_top)

    # Darken the sides slightly. These methods also affect the alpha layer,
    # so save them first (we don't want to "darken" the alpha layer making
    # the block transparent)
    sidealpha = wall_side.split()[3]
    wall_side = ImageEnhance.Brightness(wall_side).enhance(0.7)
    wall_side.putalpha(sidealpha)

    alpha_over(tmp,wall_side, (0,0),wall_side)
    alpha_over(tmp,wall_side_top, (-5,3),wall_side_top)
    wall_side = tmp
    wall_other_side = wall_side.transpose(Image.FLIP_LEFT_RIGHT)

    # compose the sides of the full wall
    tmp = Image.new("RGBA", (24,24), self.bgcolor)
    wall_side_full = self.transform_image_side(wall_side_full)
    wall_side_top_full = self.transform_image_top(wall_side_top_full.rotate(90))

    # Darken the sides slightly. These methods also affect the alpha layer,
    # so save them first (we don't want to "darken" the alpha layer making
    # the block transparent)
    sidealpha = wall_side_full.split()[3]
    wall_side_full = ImageEnhance.Brightness(wall_side_full).enhance(0.7)
    wall_side_full.putalpha(sidealpha)

    alpha_over(tmp,wall_side_full, (4,0),wall_side_full)
    alpha_over(tmp,wall_side_top_full, (3,-4),wall_side_top_full)
    wall_side_full = tmp
    wall_other_side_full = wall_side_full.transpose(Image.FLIP_LEFT_RIGHT)

    # Create img to compose the wall
    img = Image.new("RGBA", (24,24), self.bgcolor)

    # Position wall imgs around the wall bit stick
    pos_top_left = (-5,-2)
    pos_bottom_left = (-8,4)
    pos_top_right = (5,-3)
    pos_bottom_right = (7,4)
    
    # +x axis points top right direction
    # +y axis points bottom right direction
    # There are two special cases for wall without pole.
    # Normal case: 
    # First compose the walls in the back of the image, 
    # then the pole and then the walls in the front.
    if (data == 0b1010) or (data == 0b11010):
        alpha_over(img, wall_other_side_full,(0,2), wall_other_side_full)
    elif (data == 0b0101) or (data == 0b10101):
        alpha_over(img, wall_side_full,(0,2), wall_side_full)
    else:
        if (data & 0b0001) == 1:
            alpha_over(img,wall_side, pos_top_left,wall_side)                # top left
        if (data & 0b1000) == 8:
            alpha_over(img,wall_other_side, pos_top_right,wall_other_side)    # top right

        alpha_over(img,wall_pole,(0,0),wall_pole)
            
        if (data & 0b0010) == 2:
            alpha_over(img,wall_other_side, pos_bottom_left,wall_other_side)      # bottom left    
        if (data & 0b0100) == 4:
            alpha_over(img,wall_side, pos_bottom_right,wall_side)                  # bottom right
    
    return img

@material(blockid=[<lotr:tile.fence>, <lotr:tile.fence2>, <lotr:tile.fenceRotten>], data=range(16), transparent=True, nospawn=True)
def lotr_fences(self, blockid, data):
    fence_top = self.load_image_texture("assets/lotr/textures/blocks/planks_shirePine.png").copy()
    fence_side = self.load_image_texture("assets/lotr/textures/blocks/planks_shirePine.png").copy()
    fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_shirePine.png").copy()
    if blockid == <lotr:tile.fence>:
        if data == 0:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_shirePine.png").copy()
        elif data == 1:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_mallorn.png").copy()
        elif data == 2:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_mirkOak.png").copy()
        elif data == 3:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_charred.png").copy()
        elif data == 4:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_apple.png").copy()
        elif data == 5:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_pear.png").copy()
        elif data == 6:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_cherry.png").copy()
        elif data == 7:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_mango.png").copy()
        elif data == 8:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_lebethron.png").copy()
        elif data == 9:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_beech.png").copy()
        elif data == 10:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_holly.png").copy()
        elif data == 11:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_banana.png").copy()
        elif data == 12:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_maple.png").copy()
        elif data == 13:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_larch.png").copy()
        elif data == 14:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_datePalm.png").copy()
        elif data == 15:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks_mangrove.png").copy()
    elif blockid == <lotr:tile.fence2>:
        if data == 0:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks2_chestnut.png").copy()
        elif data == 1:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks2_baobab.png").copy()
        elif data == 2:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks2_cedar.png").copy()
        elif data == 3:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks2_fir.png").copy()
        elif data == 4:
            fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planks2_pine.png").copy()
    elif blockid == <lotr:tile.fenceRotten>:
        fence_top = fence_side = fence_small_side = self.load_image_texture("assets/lotr/textures/blocks/planksRotten_rotten").copy()

    # generate the textures of the fence
    ImageDraw.Draw(fence_top).rectangle((0,0,5,15),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(fence_top).rectangle((10,0,15,15),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(fence_top).rectangle((0,0,15,5),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(fence_top).rectangle((0,10,15,15),outline=(0,0,0,0),fill=(0,0,0,0))

    ImageDraw.Draw(fence_side).rectangle((0,0,5,15),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(fence_side).rectangle((10,0,15,15),outline=(0,0,0,0),fill=(0,0,0,0))

    # Create the sides and the top of the big stick
    fence_side = self.transform_image_side(fence_side)
    fence_other_side = fence_side.transpose(Image.FLIP_LEFT_RIGHT)
    fence_top = self.transform_image_top(fence_top)

    # Darken the sides slightly. These methods also affect the alpha layer,
    # so save them first (we don't want to "darken" the alpha layer making
    # the block transparent)
    sidealpha = fence_side.split()[3]
    fence_side = ImageEnhance.Brightness(fence_side).enhance(0.9)
    fence_side.putalpha(sidealpha)
    othersidealpha = fence_other_side.split()[3]
    fence_other_side = ImageEnhance.Brightness(fence_other_side).enhance(0.8)
    fence_other_side.putalpha(othersidealpha)

    # Compose the fence big stick
    fence_big = Image.new("RGBA", (24,24), self.bgcolor)
    alpha_over(fence_big,fence_side, (5,4),fence_side)
    alpha_over(fence_big,fence_other_side, (7,4),fence_other_side)
    alpha_over(fence_big,fence_top, (0,0),fence_top)
    
    # Now render the small sticks.
    # Create needed images
    ImageDraw.Draw(fence_small_side).rectangle((0,0,15,0),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(fence_small_side).rectangle((0,4,15,6),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(fence_small_side).rectangle((0,10,15,16),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(fence_small_side).rectangle((0,0,4,15),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(fence_small_side).rectangle((11,0,15,15),outline=(0,0,0,0),fill=(0,0,0,0))

    # Create the sides and the top of the small sticks
    fence_small_side = self.transform_image_side(fence_small_side)
    fence_small_other_side = fence_small_side.transpose(Image.FLIP_LEFT_RIGHT)
    
    # Darken the sides slightly. These methods also affect the alpha layer,
    # so save them first (we don't want to "darken" the alpha layer making
    # the block transparent)
    sidealpha = fence_small_other_side.split()[3]
    fence_small_other_side = ImageEnhance.Brightness(fence_small_other_side).enhance(0.9)
    fence_small_other_side.putalpha(sidealpha)
    sidealpha = fence_small_side.split()[3]
    fence_small_side = ImageEnhance.Brightness(fence_small_side).enhance(0.9)
    fence_small_side.putalpha(sidealpha)

    # Create img to compose the fence
    img = Image.new("RGBA", (24,24), self.bgcolor)

    # Position of fence small sticks in img.
    # These postitions are strange because the small sticks of the 
    # fence are at the very left and at the very right of the 16x16 images
    pos_top_left = (2,3)
    pos_top_right = (10,3)
    pos_bottom_right = (10,7)
    pos_bottom_left = (2,7)
    
    # +x axis points top right direction
    # +y axis points bottom right direction
    # First compose small sticks in the back of the image, 
    # then big stick and thecn small sticks in the front.

    if (data & 0b0001) == 1:
        alpha_over(img,fence_small_side, pos_top_left,fence_small_side)                # top left
    if (data & 0b1000) == 8:
        alpha_over(img,fence_small_other_side, pos_top_right,fence_small_other_side)    # top right
        
    alpha_over(img,fence_big,(0,0),fence_big)
        
    if (data & 0b0010) == 2:
        alpha_over(img,fence_small_other_side, pos_bottom_left,fence_small_other_side)      # bottom left    
    if (data & 0b0100) == 4:
        alpha_over(img,fence_small_side, pos_bottom_right,fence_small_side)                  # bottom right
    
    return img

@material(blockid=[<lotr:tile.mallornLadder>, <lotr:tile.hithlainLadder>] data=[2, 3, 4, 5], transparent=True)
def mallornLadder(self, blockid, data):
    # first rotations
    if self.rotation == 1:
        if data == 2: data = 5
        elif data == 3: data = 4
        elif data == 4: data = 2
        elif data == 5: data = 3
    elif self.rotation == 2:
        if data == 2: data = 3
        elif data == 3: data = 2
        elif data == 4: data = 5
        elif data == 5: data = 4
    elif self.rotation == 3:
        if data == 2: data = 4
        elif data == 3: data = 5
        elif data == 4: data = 3
        elif data == 5: data = 2
    img = Image.new("RGBA", (24,24), self.bgcolor)
    if blockid=<lotr:tile.mallornLadder>:
        raw_texture = self.load_image_texture("assets/lotr/textures/blocks/mallornLadder.png")
    elif blockid=<lotr:tile.hithlainLadder>:
        raw_texture = self.load_image_texture("assets/lotr/textures/blocks/hithlainLadder.png")
    if data == 5:
        # normally this ladder would be obsured by the block it's attached to
        # but since ladders can apparently be placed on transparent blocks, we 
        # have to render this thing anyway.  same for data == 2
        tex = self.transform_image_side(raw_texture)
        alpha_over(img, tex, (0,6), tex)
        return img
    if data == 2:
        tex = self.transform_image_side(raw_texture).transpose(Image.FLIP_LEFT_RIGHT)
        alpha_over(img, tex, (12,6), tex)
        return img
    if data == 3:
        tex = self.transform_image_side(raw_texture).transpose(Image.FLIP_LEFT_RIGHT)
        alpha_over(img, tex, (0,0), tex)
        return img
    if data == 4:
        tex = self.transform_image_side(raw_texture)
        alpha_over(img, tex, (12,0), tex)
        return img

@material(blockid=[<lotr:tile.mallornTorch>, <lotr:tile.woodElvenTorch>, <lotr:tile.highElvenTorch>, <lotr:tile.morgulTorch>], data=[1, 2, 3, 4, 5], transparent=True)
def lotr_torches(self, blockid, data):
    # first, rotations
    if self.rotation == 1:
        if data == 1: data = 3
        elif data == 2: data = 4
        elif data == 3: data = 2
        elif data == 4: data = 1
    elif self.rotation == 2:
        if data == 1: data = 2
        elif data == 2: data = 1
        elif data == 3: data = 4
        elif data == 4: data = 3
    elif self.rotation == 3:
        if data == 1: data = 4
        elif data == 2: data = 3
        elif data == 3: data = 1
        elif data == 4: data = 2
    
    # choose the proper texture
    if blockid == <lotr:tile.mallornTorch>:
        small = self.load_image_texture("assets/lotr/textures/blocks/mallornTorch.png")
    elif blockid == <lotr:tile.woodElvenTorch>:
        small = self.load_image_texture("assets/lotr/textures/blocks/woodElvenTorch.png")
    elif blockid == <lotr:tile.highElvenTorch>:
        small = self.load_image_texture("assets/lotr/textures/blocks/highElvenTorch.png")
    elif blockid == <lotr:tile.morgulTorch>:
        small = self.load_image_texture("assets/lotr/textures/blocks/morgulTorch.png")

    # Misc/lotr244.blocks.textures.txt:orcTorch_bottom.png
    # Misc/lotr244.blocks.textures.txt:orcTorch_top.png
    # Misc/lotr244.items.textures.txt:orcTorch.png
        
    # compose a torch bigger than the normal
    # (better for doing transformations)
    torch = Image.new("RGBA", (16,16), self.bgcolor)
    alpha_over(torch,small,(-4,-3))
    alpha_over(torch,small,(-5,-2))
    alpha_over(torch,small,(-3,-2))
    
    # angle of inclination of the texture
    rotation = 15
    
    if data == 1: # pointing south
        torch = torch.rotate(-rotation, Image.NEAREST) # nearest filter is more nitid.
        img = self.build_full_block(None, None, None, torch, None, None)
        
    elif data == 2: # pointing north
        torch = torch.rotate(rotation, Image.NEAREST)
        img = self.build_full_block(None, None, torch, None, None, None)
        
    elif data == 3: # pointing west
        torch = torch.rotate(rotation, Image.NEAREST)
        img = self.build_full_block(None, torch, None, None, None, None)
        
    elif data == 4: # pointing east
        torch = torch.rotate(-rotation, Image.NEAREST)
        img = self.build_full_block(None, None, None, None, torch, None)
        
    elif data == 5: # standing on the floor
        # compose a "3d torch".
        img = Image.new("RGBA", (24,24), self.bgcolor)
        
        small_crop = small.crop((2,2,14,14))
        slice = small_crop.copy()
        ImageDraw.Draw(slice).rectangle((6,0,12,12),outline=(0,0,0,0),fill=(0,0,0,0))
        ImageDraw.Draw(slice).rectangle((0,0,4,12),outline=(0,0,0,0),fill=(0,0,0,0))
        
        alpha_over(img, slice, (7,5))
        alpha_over(img, small_crop, (6,6))
        alpha_over(img, small_crop, (7,6))
        alpha_over(img, slice, (7,7))
        
    return img

@material(blockid=[<lotr:tile.elvenBed>, <lotr:tile.woodElvenBed>, <lotr:tile.dwarvenBed>, <lotr:tile.orcBed>, <lotr:tile.lionBed>, <lotr:tile.highElvenBed>, <lotr:tile.strawBed>, <lotr:tile.wargFurBed>], data=range(12), transparent=True, nospawn=True)
def lotr_beds(self, blockid, data):
    # first get rotation done
    # Masked to not clobber block head/foot info
    if self.rotation == 1:
        if (data & 0b0011) == 0: data = data & 0b1100 | 1
        elif (data & 0b0011) == 1: data = data & 0b1100 | 2
        elif (data & 0b0011) == 2: data = data & 0b1100 | 3
        elif (data & 0b0011) == 3: data = data & 0b1100 | 0
    elif self.rotation == 2:
        if (data & 0b0011) == 0: data = data & 0b1100 | 2
        elif (data & 0b0011) == 1: data = data & 0b1100 | 3
        elif (data & 0b0011) == 2: data = data & 0b1100 | 0
        elif (data & 0b0011) == 3: data = data & 0b1100 | 1
    elif self.rotation == 3:
        if (data & 0b0011) == 0: data = data & 0b1100 | 3
        elif (data & 0b0011) == 1: data = data & 0b1100 | 0
        elif (data & 0b0011) == 2: data = data & 0b1100 | 1
        elif (data & 0b0011) == 3: data = data & 0b1100 | 2
 
    if blockid == <lotr:tile.elvenBed>:
        feetEnd  = "assets/lotr/textures/blocks/elvenBed_feet_end.png"
        feetSide = "assets/lotr/textures/blocks/elvenBed_feet_side.png"
        feetTop  = "assets/lotr/textures/blocks/elvenBed_feet_top.png"
        headEnd  = "assets/lotr/textures/blocks/elvenBed_head_end.png"
        headSide = "assets/lotr/textures/blocks/elvenBed_head_side.png"
        headTop  = "assets/lotr/textures/blocks/elvenBed_head_top.png"
    elif blockid == <lotr:tile.woodElvenBed>:
        feetEnd  = "assets/lotr/textures/blocks/woodElvenBed_feet_end.png"
        feetSide = "assets/lotr/textures/blocks/woodElvenBed_feet_side.png"
        feetTop  = "assets/lotr/textures/blocks/woodElvenBed_feet_top.png"
        headEnd  = "assets/lotr/textures/blocks/woodElvenBed_head_end.png"
        headSide = "assets/lotr/textures/blocks/woodElvenBed_head_side.png"
        headTop  = "assets/lotr/textures/blocks/woodElvenBed_head_top.png"
    elif blockid == <lotr:tile.dwarvenBed>:
        feetEnd  = "assets/lotr/textures/blocks/dwarvenBed_feet_end.png"
        feetSide = "assets/lotr/textures/blocks/dwarvenBed_feet_side.png"
        feetTop  = "assets/lotr/textures/blocks/dwarvenBed_feet_top.png"
        headEnd  = "assets/lotr/textures/blocks/dwarvenBed_head_end.png"
        headSide = "assets/lotr/textures/blocks/dwarvenBed_head_side.png"
        headTop  = "assets/lotr/textures/blocks/dwarvenBed_head_top.png"
    elif blockid == <lotr:tile.orcBed>:
        feetEnd  = "assets/lotr/textures/blocks/orcBed_feet_end.png"
        feetSide = "assets/lotr/textures/blocks/orcBed_feet_side.png"
        feetTop  = "assets/lotr/textures/blocks/orcBed_feet_top.png"
        headEnd  = "assets/lotr/textures/blocks/orcBed_head_end.png"
        headSide = "assets/lotr/textures/blocks/orcBed_head_side.png"
        headTop  = "assets/lotr/textures/blocks/orcBed_head_top.png"
    elif blockid == <lotr:tile.lionBed>:
        feetEnd  = "assets/lotr/textures/blocks/lionBed_feet_end.png"
        feetSide = "assets/lotr/textures/blocks/lionBed_feet_side.png"
        feetTop  = "assets/lotr/textures/blocks/lionBed_feet_top.png"
        headEnd  = "assets/lotr/textures/blocks/lionBed_head_end.png"
        headSide = "assets/lotr/textures/blocks/lionBed_head_side.png"
        headTop  = "assets/lotr/textures/blocks/lionBed_head_top.png"
    elif blockid == <lotr:tile.highElvenBed>:
        feetEnd  = "assets/lotr/textures/blocks/highElvenBed_feet_end.png"
        feetSide = "assets/lotr/textures/blocks/highElvenBed_feet_side.png"
        feetTop  = "assets/lotr/textures/blocks/highElvenBed_feet_top.png"
        headEnd  = "assets/lotr/textures/blocks/highElvenBed_head_end.png"
        headSide = "assets/lotr/textures/blocks/highElvenBed_head_side.png"
        headTop  = "assets/lotr/textures/blocks/highElvenBed_head_top.png"
    elif blockid == <lotr:tile.strawBed>:
        feetEnd  = "assets/lotr/textures/blocks/strawBed_feet_end.png"
        feetSide = "assets/lotr/textures/blocks/strawBed_feet_side.png"
        feetTop  = "assets/lotr/textures/blocks/strawBed_feet_top.png"
        headEnd  = "assets/lotr/textures/blocks/strawBed_head_end.png"
        headSide = "assets/lotr/textures/blocks/strawBed_head_side.png"
        headTop  = "assets/lotr/textures/blocks/strawBed_head_top.png"
    elif blockid == <lotr:tile.wargFurBed>:
        feetEnd  = "assets/lotr/textures/blocks/wargFurBed_feet_end.png"
        feetSide = "assets/lotr/textures/blocks/wargFurBed_feet_side.png"
        feetTop  = "assets/lotr/textures/blocks/wargFurBed_feet_top.png"
        headEnd  = "assets/lotr/textures/blocks/wargFurBed_head_end.png"
        headSide = "assets/lotr/textures/blocks/wargFurBed_head_side.png"
        headTop  = "assets/lotr/textures/blocks/wargFurBed_head_top.png"
    increment = 8
    left_face = None
    right_face = None
    if data & 0x8 == 0x8: # head of the bed
        top = self.load_image_texture(headTop)
        if data & 0x00 == 0x00: # head pointing to West
            top = top.copy().rotate(270)
            left_face = self.load_image_texture(headSide)
            right_face = self.load_image_texture(headEnd)
        if data & 0x01 == 0x01: # ... North
            top = top.rotate(270)
            left_face = self.load_image_texture(headEnd)
            right_face = self.load_image_texture(headSide)
        if data & 0x02 == 0x02: # East
            top = top.rotate(180)
            left_face = self.load_image_texture(headSide).transpose(Image.FLIP_LEFT_RIGHT)
            right_face = None
        if data & 0x03 == 0x03: # South
            right_face = None
            right_face = self.load_image_texture(headSide).transpose(Image.FLIP_LEFT_RIGHT)
    
    else: # foot of the bed
        top = self.load_image_texture(feetTop)
        if data & 0x00 == 0x00: # head pointing to West
            top = top.rotate(270)
            left_face = self.load_image_texture(feetSide)
            right_face = None
        if data & 0x01 == 0x01: # ... North
            top = top.rotate(270)
            left_face = None
            right_face = self.load_image_texture(feetSide)
        if data & 0x02 == 0x02: # East
            top = top.rotate(180)
            left_face = self.load_image_texture(feetSide).transpose(Image.FLIP_LEFT_RIGHT)
            right_face = self.load_image_texture(feetEnd).transpose(Image.FLIP_LEFT_RIGHT)
        if data & 0x03 == 0x03: # South
            left_face = self.load_image_texture(feetEnd)
            right_face = self.load_image_texture(feetSide).transpose(Image.FLIP_LEFT_RIGHT)
    
    top = (top, increment)
    return self.build_full_block(top, None, None, left_face, right_face)

@material(blockid=[<lotr:tile.pressurePlateMordorRock>, <lotr:tile.pressurePlateGondorRock>, <lotr:tile.pressurePlateRohanRock>, <lotr:tile.pressurePlateBlueRock>, <lotr:tile.pressurePlateRedRock>], data=[0,1], transparent=True)
def lotr_pressure_plates(self, blockid, data):
    if blockid == <lotr:tile.pressurePlateMordorRock>:
        t = self.load_image_texture("assets/lotr/textures/blocks/rock_mordor.png").copy()
    elif blockid == <lotr:tile.pressurePlateGondorRock>:
        t = self.load_image_texture("assets/lotr/textures/blocks/rock_gondor.png").copy()
    elif blockid == <lotr:tile.pressurePlateRohanRock>:
        t = self.load_image_texture("assets/lotr/textures/blocks/rock_rohan.png").copy()
    elif blockid == <lotr:tile.pressurePlateBlueRock>:
        t = self.load_image_texture("assets/lotr/textures/blocks/rock_blue.png").copy()
    elif blockid == <lotr:tile.pressurePlateRedRock>:
        t = self.load_image_texture("assets/lotr/textures/blocks/rock_red.png").copy()
    
    # cut out the outside border, pressure plates are smaller
    # than a normal block
    ImageDraw.Draw(t).rectangle((0,0,15,15),outline=(0,0,0,0))
    
    # create the textures and a darker version to make a 3d by 
    # pasting them with an offstet of 1 pixel
    img = Image.new("RGBA", (24,24), self.bgcolor)
    
    top = self.transform_image_top(t)
    
    alpha = top.split()[3]
    topd = ImageEnhance.Brightness(top).enhance(0.8)
    topd.putalpha(alpha)
    
    #show it 3d or 2d if unpressed or pressed
    if data == 0:
        alpha_over(img,topd, (0,12),topd)
        alpha_over(img,top, (0,11),top)
    elif data == 1:
        alpha_over(img,top, (0,12),top)
    
    return img

@material(blockid=[<lotr:tile.buttonMordorRock>, <lotr:tile.buttonGondorRock>, <lotr:tile.buttonRohanRock>, <lotr:tile.buttonBlueRock>, <lotr:tile.buttonRedRock>], data=range(16), transparent=True)
def lotr_buttons(self, blockid, data):

    # 0x8 is set if the button is pressed mask this info and render
    # it as unpressed
    data = data & 0x7

    if self.rotation == 1:
        if data == 1: data = 3
        elif data == 2: data = 4
        elif data == 3: data = 2
        elif data == 4: data = 1
    elif self.rotation == 2:
        if data == 1: data = 2
        elif data == 2: data = 1
        elif data == 3: data = 4
        elif data == 4: data = 3
    elif self.rotation == 3:
        if data == 1: data = 4
        elif data == 2: data = 3
        elif data == 3: data = 1
        elif data == 4: data = 2

    if blockid == <lotr:tile.buttonMordorRock>:
        t = self.load_image_texture("assets/lotr/textures/blocks/rock_mordor.png").copy()
    elif blockid == <lotr:tile.buttonGondorRock>:
        t = self.load_image_texture("assets/lotr/textures/blocks/rock_gondor.png").copy()
    elif blockid == <lotr:tile.buttonRohanRock>:
        t = self.load_image_texture("assets/lotr/textures/blocks/rock_rohan.png").copy()
    elif blockid == <lotr:tile.buttonBlueRock>:
        t = self.load_image_texture("assets/lotr/textures/blocks/rock_blue.png").copy()
    elif blockid == <lotr:tile.buttonRedRock>:
        t = self.load_image_texture("assets/lotr/textures/blocks/rock_red.png").copy()

    # generate the texture for the button
    ImageDraw.Draw(t).rectangle((0,0,15,5),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(t).rectangle((0,10,15,15),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(t).rectangle((0,0,4,15),outline=(0,0,0,0),fill=(0,0,0,0))
    ImageDraw.Draw(t).rectangle((11,0,15,15),outline=(0,0,0,0),fill=(0,0,0,0))

    img = Image.new("RGBA", (24,24), self.bgcolor)

    button = self.transform_image_side(t)
    
    if data == 1: # facing SOUTH
        # buttons can't be placed in transparent blocks, so this
        # direction can't be seen
        return None

    elif data == 2: # facing NORTH
        # paste it twice with different brightness to make a 3D effect
        alpha_over(img, button, (12,-1), button)

        alpha = button.split()[3]
        button = ImageEnhance.Brightness(button).enhance(0.9)
        button.putalpha(alpha)
        
        alpha_over(img, button, (11,0), button)

    elif data == 3: # facing WEST
        # paste it twice with different brightness to make a 3D effect
        button = button.transpose(Image.FLIP_LEFT_RIGHT)
        alpha_over(img, button, (0,-1), button)

        alpha = button.split()[3]
        button = ImageEnhance.Brightness(button).enhance(0.9)
        button.putalpha(alpha)
        
        alpha_over(img, button, (1,0), button)

    elif data == 4: # facing EAST
        # buttons can't be placed in transparent blocks, so this
        # direction can't be seen
        return None

    return img

################################################################################
# These don't work !!! #########################################################
################################################################################

@material(blockid=<lotr:tile.commandTable>, data=range(1), solid=True)
def commandTable(self, blockid, data):
    return self.build_block(self.load_image_texture("assets/lotr/textures/blocks/commandTable_top.png"), self.load_image_texture("assets/lotr/textures/blocks/commandTable_side.png"))

##### Caveat: clovers are not supported #####
#@material(blockid=<lotr:tile.clover>, data=range(2), transparent=True)
#def clover(self, blockid, data):
#    if data == 0:    # Clover
#        tex = self.load_image_texture("assets/lotr/textures/blocks/clover_petal.png")
#    elif data == 1:  # Four-leaves Clover
#        tex = self.load_image_texture("assets/lotr/textures/blocks/clover_stem.png")
#    return self.build_sprite(tex)

##### Caveat: tallGrass are not supported #####
#@material(blockid=<lotr:tile.tallGrass>, data=range(4), transparent=True)
#def tallGrass(self, blockid, data):
#    if data == 0:    # Short Grass
#        tex = self.load_image_texture("assets/lotr/textures/blocks/tallGrass_short.png")
#    elif data == 1:  # Flowery Grass
#        tex = self.load_image_texture("assets/lotr/textures/blocks/tallGrass_flower.png")
#    elif data == 2:  # Wheatgrass
#        tex = self.load_image_texture("assets/lotr/textures/blocks/tallGrass_wheat.png")
#    elif data == 3:  # Thistle
#        tex = self.load_image_texture("assets/lotr/textures/blocks/tallGrass_thistle.png")
#    return self.build_sprite(tex)

# } LotrSupportInOverviewer
