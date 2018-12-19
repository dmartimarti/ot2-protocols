# -*- coding: utf-8 -*-
'''

This script will dispense 180 uL of NGM and NGM + Glu (two times!) into one plate.
Because of faulty P300, the script should be stopped after the first round of media dispensing. 
Second round of dispensing 20 uL of bacteria from column 6 to 12 in reservoir into column 3 to 9 
in 96-well plate.  

Script by Dani Martinez, Dec - 2018
Cabreiro Lab. 
'''

from opentrons import labware, instruments, robot


#### load labware

# load 6 different plates
plate1 = labware.load('96-flat', '1') # loads a 96-flat plate

# reservoirs
media_bac = labware.load('trough-12row', '2') # loads a trough-12row

# tip racks
tiprack1 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 

# pipette
p300 = instruments.P300_Multi(mount = 'right', tip_racks = [tiprack1])
p50 = instruments.P50_Multi(mount = 'left', tip_racks = [tiprack1])

p50.set_flow_rate(dispense = 250)



#### actions

### first step: pour media in the plate

## first half

# fill plate 1 (half 1)
p300.pick_up_tip()
for i in range(12):
	p300.transfer(180, media_bac.cols('1'), plate1.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
p300.drop_tip()

# fill plate 1 (half 2)
p300.pick_up_tip()
for i in range(12):
	p300.transfer(180, media_bac.cols('2'), plate1.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
p300.drop_tip()

## second half

# add the bacteria

p50.pick_up_tip()
for i in range(7):
	p50.transfer(20, media_bac.cols(i + 5), plate1.cols(i + 2).top(), 
		mix_before = (2, 50), new_tip = 'never')
p50.drop_tip()




