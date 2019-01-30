# -*- coding: utf-8 -*-
'''
This script will add media from a 12-trough reservoir to 6 plates
for a BGA experiment. 
First part of the experiment. 

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
reservoir = labware.load('trough-12row', '2') # loads a 12 column reservoir
# tiprack
tiprack = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 
# pipette
pipette = instruments.P300_Multi(mount = 'right', tip_racks = [tiprack])

pipette.set_flow_rate(dispense = 300)


## actions
pipette.pick_up_tip()
for i in range(8):
	pipette.transfer(180, reservoir.cols('1'), plate1.cols(i + 2).bottom(7), 
		# mix_before = (1, 150), 
		new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
for i in range(8):
	pipette.transfer(180, reservoir.cols('2'), plate2.cols(i + 2).bottom(7), 
		# mix_before = (1, 150), 
		new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
for i in range(8):
	pipette.transfer(180, reservoir.cols('3'), plate3.cols(i + 2).bottom(7), 
		# mix_before = (1, 150), 
		new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
for i in range(8):
	pipette.transfer(180, reservoir.cols('4'), plate4.cols(i + 2).bottom(7), 
		# mix_before = (1, 150), 
		new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
for i in range(8):
	pipette.transfer(180, reservoir.cols('5'), plate5.cols(i + 2).bottom(7), 
		# mix_before = (1, 150), 
		new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
for i in range(8):
	pipette.transfer(180, reservoir.cols('6'), plate6.cols(i + 2).bottom(7), 
		# mix_before = (1, 150), 
		new_tip = 'never')
pipette.drop_tip()



