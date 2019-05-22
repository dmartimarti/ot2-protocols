# -*- coding: utf-8 -*-
'''
This script will add media from a 12-trough reservoir to 6 plates
for a BGA experiment. 
First part of the experiment. 

Script by Dani Martinez, May - 2019
'''

from opentrons import labware, instruments, robot


#### load labware

# load 6 different plates
plate1 = labware.load('96-flat', '4') # loads a 96-flat plate
plate2 = labware.load('96-flat', '7') # loads a 96-flat plate
plate3 = labware.load('96-flat', '10') # loads a 96-flat plate

plate4 = labware.load('96-flat', '5') # loads a 96-flat plate
plate5 = labware.load('96-flat', '8') # loads a 96-flat plate
plate6 = labware.load('96-flat', '11') # loads a 96-flat plate

# reservoir
media1 = labware.load('trough-12row', '1') # loads a 12 column reservoir

# tiprack
tiprack1 = labware.load('tiprack-200ul', '2') # loads a tip rack of 200 uL 


# pipette
pipette = instruments.P300_Multi(mount = 'left', tip_racks = [tiprack1])



# actions

# plate 1
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media1.cols('1'), plate1.cols(i), new_tip = 'never')
pipette.drop_tip()

# plate 1
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media1.cols('2'), plate1.cols(i + 6), new_tip = 'never')
pipette.drop_tip()


# plate 2
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media1.cols('3'), plate2.cols(i), new_tip = 'never')
pipette.drop_tip()

# plate 2
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media1.cols('4'), plate2.cols(i + 6), new_tip = 'never')
pipette.drop_tip()


# plate 3
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media1.cols('5'), plate3.cols(i), new_tip = 'never')
pipette.drop_tip()

# plate 3
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media1.cols('6'), plate3.cols(i + 6), new_tip = 'never')
pipette.drop_tip()



# plate 4
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media1.cols('7'), plate4.cols(i), new_tip = 'never')
pipette.drop_tip()

# plate 4
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media1.cols('8'), plate4.cols(i + 6), new_tip = 'never')
pipette.drop_tip()



# plate 5
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media1.cols('9'), plate5.cols(i), new_tip = 'never')
pipette.drop_tip()

# plate 5
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media1.cols('10'), plate5.cols(i + 6), new_tip = 'never')
pipette.drop_tip()



# plate 1
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media1.cols('11'), plate6.cols(i), new_tip = 'never')
pipette.drop_tip()

# plate 1
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media1.cols('12'), plate6.cols(i + 6), new_tip = 'never')
pipette.drop_tip()




















