# -*- coding: utf-8 -*-
'''
Distribution of siRNA plates. Script for Domhnall.

Script by Dani Martinez, Cabreiro Lab., Jan - 2019
'''

from opentrons import labware, instruments, robot


#### load labware

# load 6 different plates
plate1 = labware.load('96-flat', '4') # loads a 96-flat plate
plate2 = labware.load('96-flat', '5') # loads a 96-flat plate
plate3 = labware.load('96-flat', '6') # loads a 96-flat plate

# reservoir
reservoir1 = labware.load('96-flat', '2') # loads a 96-flat plate
# tiprack
tiprack1 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 
# pipette
pipette = instruments.P50_Multi(mount = 'left', tip_racks = [tiprack1])

pipette.set_flow_rate(dispense = 300)

#### actions
for i in range(3):
	pipette.pick_up_tip()
	pipette.mix(2, 40, reservoir1.cols(i))   
	pipette.aspirate(35, reservoir1.cols(i))
	pipette.dispense(11, plate1.cols(i).bottom(7))
	pipette.dispense(11, plate2.cols(i).bottom(7))
	pipette.dispense(11, plate3.cols(i).bottom(7))
	pipette.drop_tip()