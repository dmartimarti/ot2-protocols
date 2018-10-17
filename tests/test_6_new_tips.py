# -*- coding: utf-8 -*-
'''
This code fills an entire 96-well plate with 100 uL, and then
it transfers 30 from row i to row i+1 to make a dilution. It 
mixes three times per column when transferring the liquid

Script by Dani Martinez, Oct - 2018
'''

from opentrons import labware, instruments, robot


#### load labware

plate = labware.load('96-flat', '1') # loads a 96-flat plate
reservoir = labware.load('96-flat', '2') # loads a 96-flat plate
tiprack = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 

p300 = instruments.P300_Single(
	mount = 'right', 
	tip_racks = [tiprack]
	)


#### actions

p300.transfer(100, reservoir.wells('A1'), plate.cols('1'), new_tip = 'always')

for c in robot.commands():
    print(c)