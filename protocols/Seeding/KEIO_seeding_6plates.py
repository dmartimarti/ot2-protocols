# -*- coding: utf-8 -*-
'''
Seeding of 8 96-well plates with 150 uL of NGM agar from
one reservoir (96-plate) of bacterial culture.

Type of experiment: KEIO seeding plates

Script by Dani Martinez, Cabreiro Lab., Jan - 2019
'''

from opentrons import labware, instruments, robot


#### load labware

# load 6 different plates
plate1 = labware.load('96-flat', '4') # loads a 96-flat plate
plate2 = labware.load('96-flat', '5') # loads a 96-flat plate
plate3 = labware.load('96-flat', '6') # loads a 96-flat plate
plate4 = labware.load('96-flat', '7') # loads a 96-flat plate
plate5 = labware.load('96-flat', '8') # loads a 96-flat plate
plate6 = labware.load('96-flat', '9') # loads a 96-flat plate

# reservoir
reservoir1 = labware.load('96-flat', '2') # loads a 96-flat plate
# tiprack
tiprack1 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 
# pipette
pipette = instruments.P50_Multi(mount = 'left', tip_racks = [tiprack1])

pipette.set_flow_rate(dispense = 300)

#### actions

for i in range(12):
	pipette.pick_up_tip()
	pipette.transfer(11, reservoir1.cols(i), plate1.cols(i).bottom(7), mix_before = (2, 40), new_tip = 'never')
	pipette.transfer(11, reservoir1.cols(i), plate2.cols(i).bottom(7), new_tip = 'never')
	pipette.transfer(11, reservoir1.cols(i), plate3.cols(i).bottom(7), new_tip = 'never')
	pipette.transfer(11, reservoir1.cols(i), plate4.cols(i).bottom(7), mix_before = (2, 40), new_tip = 'never')
	pipette.transfer(11, reservoir1.cols(i), plate5.cols(i).bottom(7), new_tip = 'never')
	pipette.transfer(11, reservoir1.cols(i), plate6.cols(i).bottom(7), new_tip = 'never')
	pipette.drop_tip()