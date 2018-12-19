# -*- coding: utf-8 -*-
'''

Mixing plates with only one column of tips. 
Remember to move tips to the first column of the tiprack
if you want to run this again¡ 

Script by Dani Martinez, Nov - 2018
Cabreiro Lab. 
'''

from opentrons import labware, instruments, robot

#### load labware

# load 7 different plates
plate1 = labware.load('96-flat', '2') # loads a 96-flat plate

# tip racks
tiprack1 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 

# pipette
pipette = instruments.P300_Multi(mount = 'right', tip_racks = [tiprack1])

pipette.pick_up_tip()
for i in range(12):
	pipette.mix(3, 100, plate1.cols(i))
pipette.drop_tip()