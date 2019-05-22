# -*- coding: utf-8 -*-
'''
This script will add the bacteria to 3 plates. Run it twice if you have to add
6 plates instead of 3. 
Second part of the experiment. 

Script by Dani Martinez, May - 2019
'''

from opentrons import labware, instruments, robot


#### load labware

# load 6 different plates
plate1 = labware.load('96-flat', '4') # loads a 96-flat plate
plate2 = labware.load('96-flat', '7') # loads a 96-flat plate
plate3 = labware.load('96-flat', '10') # loads a 96-flat plate


# reservoir
bact = labware.load('96-flat', '1') # loads a 12 column reservoir

# tiprack
tiprack1 = labware.load('tiprack-200ul', '5') # loads a tip rack of 200 uL 
tiprack2 = labware.load('tiprack-200ul', '8') # loads a tip rack of 200 uL 
tiprack3 = labware.load('tiprack-200ul', '11') # loads a tip rack of 200 uL 

# pipette
pipette = instruments.P50_Multi(mount = 'right', tip_racks = [tiprack1, tiprack2, tiprack3])



for i in range(12):
	pipette.transfer(180, bact.cols(i), plate1.cols(i), mix_before = (1, 40))

for i in range(12):
	pipette.transfer(180, bact.cols(i), plate2.cols(i), mix_before = (1, 40))

for i in range(12):
	pipette.transfer(180, bact.cols(i), plate3.cols(i), mix_before = (1, 40))
