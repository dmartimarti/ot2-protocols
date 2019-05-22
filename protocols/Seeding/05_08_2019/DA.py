# -*- coding: utf-8 -*-
'''
MIC experiment, two parts. 

The first part will add all the media1 to each plate. Each plate will have 4 columns
with a different drug concentration starting from 0, to 1024 uM of 5FU.

Script by Dani Martinez, May - 2019
'''

from opentrons import labware, instruments, robot


#### load labware

# load 4 different plates
plate1 = labware.load('96-flat', '4') # loads a 96-flat plate

# reservoir
media = labware.load('trough-12row', '2')
bact = labware.load('96-deep-well', '1') # loads a 96-deep plate

# tiprack
tiprack1 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 
tiprack2 = labware.load('tiprack-200ul', '6') # loads a tip rack of 200 uL 

# pipette
pipette = instruments.P300_Multi(mount = 'left', 
	tip_racks = [tiprack1, tiprack2])


## add media
for i in range(12):
	pipette.transfer(150, media.cols(i), plate1.cols(i))


for i in range(12):
	pipette.transfer(50, bact.cols('1'), plate1.cols(i))
