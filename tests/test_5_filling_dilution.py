# -*- coding: utf-8 -*-
'''
This code fills an entire 96-well plate with 100 uL, and then
it transfers 30 from row i to row i+1 to make a dilution. It 
mixes three times per column when transferring the liquid

Script by Dani Martinez, Oct - 2018
'''

from opentrons import labware, instruments


#### load labware

plate = labware.load('96-flat', '1') # loads a 96-flat plate
reservoir = labware.load('96-flat', '2') # loads a 96-flat plate
tiprack = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 

pipette = instruments.P300_Multi(mount = 'left')


#### actions

### pick up tips from col 1 from tip rack
pipette.pick_up_tip(tiprack.cols('1'))

### loop to transfer 100 uL to each well
for i in range(12):
	pipette.transfer(100, reservoir.cols('1'), plate.cols(i).bottom(7), new_tip = 'never')

### loop to transfer 30 uL from col i to col i+1
# for i in range(11):
# 	pipette.transfer(30, plate.cols(i), plate.cols(i + 1), new_tip = 'never', mix_after=(3, 75))

# return tips to the col 1
pipette.return_tip(tiprack.cols('1'))
