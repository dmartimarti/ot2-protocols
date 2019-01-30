# -*- coding: utf-8 -*-
'''
Seeding of controls to the 4 conditions. 
Only 3 columns will be seeded.

Type of experiment: KEIO seeding control plates

Script by Dani Martinez, Cabreiro Lab., Jan - 2019
'''

from opentrons import labware, instruments, robot


#### load labware

# load 6 different plates
plate1 = labware.load('96-flat', '4') # loads a 96-flat plate
plate2 = labware.load('96-flat', '5') # loads a 96-flat plate
plate3 = labware.load('96-flat', '6') # loads a 96-flat plate
plate4 = labware.load('96-flat', '7') # loads a 96-flat plate


# reservoir
reservoir1 = labware.load('96-flat', '2') # loads a 96-flat plate
# tiprack
tiprack1 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 
# pipette
pipette = instruments.P50_Multi(mount = 'left', tip_racks = [tiprack1])

pipette.set_flow_rate(dispense = 300)

#### actions

pipette.pick_up_tip()
for i in range(3):
	pipette.transfer(11, reservoir1.cols('1'), plate1.cols(i).bottom(7), mix_before = (2, 40), new_tip = 'never')
	pipette.transfer(11, reservoir1.cols('1'), plate2.cols(i).bottom(7), new_tip = 'never')
	pipette.transfer(11, reservoir1.cols('1'), plate3.cols(i).bottom(7), new_tip = 'never')
	pipette.transfer(11, reservoir1.cols('1'), plate4.cols(i).bottom(7), new_tip = 'never')
pipette.drop_tip()


