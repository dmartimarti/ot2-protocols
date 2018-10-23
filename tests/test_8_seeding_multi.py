# -*- coding: utf-8 -*-
'''
This script modifies robot's speed (to make its movements smoother), 
and distributes 5 uL to every well in a 96-plate from 7 mm from the 
botton (to avoid touching the agar)

Script by Dani Martinez, Oct - 2018
'''

from opentrons import labware, instruments, robot


#### load labware

plate = labware.load('96-flat', '1') # loads a 96-flat plate
reservoir = labware.load('96-flat', '2') # loads a 96-flat plate
tiprack = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 

pipette = instruments.P50_Multi(mount = 'left', tip_racks = [tiprack])

pipette.set_flow_rate(dispense = 250)

pipette.pick_up_tip()

for i in range(3):
	pipette.transfer(7, # uL to dispense
		reservoir.cols(i), plate.cols(i+3).bottom(7), 
		mix_before = (2, 30), 
		new_tip = 'always', 
		trash = True)

pipette.drop_tip()