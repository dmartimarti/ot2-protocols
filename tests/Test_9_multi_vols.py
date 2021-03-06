# -*- coding: utf-8 -*-
'''
This script modifies robot's speed (to make its movements smoother), 
and distributes 5 uL to every well in a 96-plate from a higher height 
than usual (to avoid touching the agar)

Script by Dani Martinez, Oct - 2018
'''

from opentrons import labware, instruments, robot


#### load labware

plate = labware.load('96-deep-well', '1') # loads a 96-deep well plate
reservoir = labware.load('96-flat', '2') # loads a 96-flat plate
tiprack = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 

pipette = instruments.P300_Single(mount = 'right', 
	tip_racks = [tiprack])

pipette.pick_up_tip()

pipette.transfer(700, 
	reservoir.wells('A1'), plate.wells('A1'),
	mix_before = (2, 150))

pipette.drop_tip()