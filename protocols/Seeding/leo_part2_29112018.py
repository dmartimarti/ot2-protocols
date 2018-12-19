# -*- coding: utf-8 -*-
'''
Protocol to fill plates with media. 
Part 2

Script by Dani Martinez, Nov - 2018
Cabreiro Lab. 
'''

from opentrons import labware, instruments, robot


#### load labware

# load 7 different plates
plate1 = labware.load('96-flat', '4') # loads a 96-flat plate
plate2 = labware.load('96-flat', '7') # loads a 96-flat plate
plate3 = labware.load('96-flat', '8') # loads a 96-flat plate
plate4 = labware.load('96-flat', '10') # loads a 96-flat plate
plate5 = labware.load('96-flat', '11') # loads a 96-flat plate

# media
bacteria = labware.load('96-deep-well', '1') # loads a trough-12row

# tip racks
tiprack1 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 


# pipette
pipette = instruments.P300_Multi(mount = 'right', 
	tip_racks = [tiprack1])


# actions

# new column
pipette.pick_up_tip()
pipette.transfer(50, bacteria.cols('1'), plate1.cols('1'), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('1'), plate2.cols('1'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('1'), plate3.cols('1'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('1'), plate4.cols('1'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('1'), plate5.cols('1'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# new column
pipette.pick_up_tip()
pipette.transfer(50, bacteria.cols('2'), plate1.cols('2'), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('2'), plate2.cols('2'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('2'), plate3.cols('2'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('2'), plate4.cols('2'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('2'), plate5.cols('2'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# new column
pipette.pick_up_tip()
pipette.transfer(50, bacteria.cols('3'), plate1.cols('3'), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('3'), plate2.cols('3'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('3'), plate3.cols('3'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('3'), plate4.cols('3'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('3'), plate5.cols('3'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# new column
pipette.pick_up_tip()
pipette.transfer(50, bacteria.cols('4'), plate1.cols('4'), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('4'), plate2.cols('4'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('4'), plate3.cols('4'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('4'), plate4.cols('4'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('4'), plate5.cols('4'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# new column
pipette.pick_up_tip()
pipette.transfer(50, bacteria.cols('5'), plate1.cols('5'), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('5'), plate2.cols('5'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('5'), plate3.cols('5'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('5'), plate4.cols('5'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('5'), plate5.cols('5'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# new column
pipette.pick_up_tip()
pipette.transfer(50, bacteria.cols('6'), plate1.cols('6'), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('6'), plate2.cols('6'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('6'), plate3.cols('6'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('6'), plate4.cols('6'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('6'), plate5.cols('6'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# new column
pipette.pick_up_tip()
pipette.transfer(50, bacteria.cols('7'), plate1.cols('7'), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('7'), plate2.cols('7'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('7'), plate3.cols('7'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('7'), plate4.cols('7'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('7'), plate5.cols('7'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# new column
pipette.pick_up_tip()
pipette.transfer(50, bacteria.cols('8'), plate1.cols('8'), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('8'), plate2.cols('8'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('8'), plate3.cols('8'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('8'), plate4.cols('8'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('8'), plate5.cols('8'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# new column
pipette.pick_up_tip()
pipette.transfer(50, bacteria.cols('9'), plate1.cols('9'), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('9'), plate2.cols('9'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('9'), plate3.cols('9'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('9'), plate4.cols('9'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('9'), plate5.cols('9'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# new column
pipette.pick_up_tip()
pipette.transfer(50, bacteria.cols('10'), plate1.cols('10'), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('10'), plate2.cols('10'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('10'), plate3.cols('10'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('10'), plate4.cols('10'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('10'), plate5.cols('10'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# new column
pipette.pick_up_tip()
pipette.transfer(50, bacteria.cols('11'), plate1.cols('11'), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('11'), plate2.cols('11'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('11'), plate3.cols('11'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('11'), plate4.cols('11'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('11'), plate5.cols('11'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# new column
pipette.pick_up_tip()
pipette.transfer(50, bacteria.cols('12'), plate1.cols('12'), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('12'), plate2.cols('12'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('12'), plate3.cols('12'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('12'), plate4.cols('12'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('12'), plate5.cols('12'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

