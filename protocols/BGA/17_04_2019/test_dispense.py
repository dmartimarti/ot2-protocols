# -*- coding: utf-8 -*-
'''
This script will add media from a 12-trough reservoir to 6 plates
for a BGA experiment. 
First part of the experiment. 

Script by Dani Martinez, Apr - 2019
'''

from opentrons import labware, instruments, robot

#### load labware

# load 6 different plates
plate1 = labware.load('96-flat', '4') # loads a 96-flat plate

tiprack1 = labware.load('tiprack-200ul', '5') # loads a 96-flat plate

# reservoir
media1 = labware.load('96-deep-well', '1') # loads a 12 column reservoir

# pipette
pipette = instruments.P50_Multi(mount = 'right', 
	tip_racks = [tiprack1],
    dispense_flow_rate = 600)


## plate 1
pipette.pick_up_tip()
pipette.transfer(9, media1.cols('1'), plate1.cols('1').bottom(6), mix_before = (1, 40))
pipette.transfer(9, media1.cols('1'), plate1.cols('2').bottom(6))
pipette.transfer(9, media1.cols('1'), plate1.cols('3').bottom(6))
pipette.drop_tip()