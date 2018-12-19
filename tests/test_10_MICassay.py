# -*- coding: utf-8 -*-
'''
Resuspension code

Script by Dani Martinez, Nov - 2018
Cabreiro Lab. 
'''

from opentrons import labware, instruments, robot


#### load labware

# load 1 different plates
plate1 = labware.load('96-flat', '2') # loads a 96-flat plate

# tip racks
tiprack1 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 

pipette = instruments.P300_Multi(mount = 'right', tip_racks = [tiprack1])

for i in range(12):
	pipette.pick_up_tip()
	pipette.mix(3, 150, plate1.cols(i))
	pipette.drop_tip()
