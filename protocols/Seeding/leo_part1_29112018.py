# -*- coding: utf-8 -*-
'''
Protocol to fill plates with media.
Part 1.

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
media1 = labware.load('trough-12row', '1') # loads a trough-12row
media2 = labware.load('trough-12row', '2') # loads a trough-12row
media3 = labware.load('trough-12row', '5') # loads a trough-12row

# tip racks
tiprack1 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 
tiprack2 = labware.load('tiprack-200ul', '6') # loads a tip rack of 200 uL 
tiprack3 = labware.load('tiprack-200ul', '9') # loads a tip rack of 200 uL 

# pipette
pipette = instruments.P300_Multi(mount = 'right', 
	tip_racks = [tiprack1, tiprack2, tiprack3])



#### actions
# plate 1 - media 1

pipette.pick_up_tip()
pipette.transfer(150, media1.cols('1'), plate1.cols('1'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media1.cols('1'), plate1.cols('2'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media1.cols('2'), plate1.cols('3'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media1.cols('2'), plate1.cols('4'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media1.cols('3'), plate1.cols('5'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media1.cols('3'), plate1.cols('6'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media1.cols('4'), plate1.cols('7'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media1.cols('4'), plate1.cols('8'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media1.cols('5'), plate1.cols('9'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media1.cols('5'), plate1.cols('10'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media1.cols('6'), plate1.cols('11'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media1.cols('6'), plate1.cols('12'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()



# plate 2 - media 1

pipette.pick_up_tip()
pipette.transfer(150, media1.cols('7'), plate2.cols('1'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media1.cols('7'), plate2.cols('2'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media1.cols('8'), plate2.cols('3'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media1.cols('8'), plate2.cols('4'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media1.cols('9'), plate2.cols('5'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media1.cols('9'), plate2.cols('6'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media1.cols('10'), plate2.cols('7'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media1.cols('10'), plate2.cols('8'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media1.cols('11'), plate2.cols('9'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media1.cols('11'), plate2.cols('10'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media1.cols('12'), plate2.cols('11'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media1.cols('12'), plate2.cols('12'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()


###
# plate 3 - media 2

pipette.pick_up_tip()
pipette.transfer(150, media2.cols('1'), plate3.cols('1'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media2.cols('1'), plate3.cols('2'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media2.cols('2'), plate3.cols('3'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media2.cols('2'), plate3.cols('4'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media2.cols('3'), plate3.cols('5'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media2.cols('3'), plate3.cols('6'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media2.cols('4'), plate3.cols('7'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media2.cols('4'), plate3.cols('8'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media2.cols('5'), plate3.cols('9'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media2.cols('5'), plate3.cols('10'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media2.cols('6'), plate3.cols('11'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media2.cols('6'), plate3.cols('12'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# plate 4 - media 2

pipette.pick_up_tip()
pipette.transfer(150, media2.cols('7'), plate4.cols('1'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media2.cols('7'), plate4.cols('2'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media2.cols('8'), plate4.cols('3'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media2.cols('8'), plate4.cols('4'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media2.cols('9'), plate4.cols('5'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media2.cols('9'), plate4.cols('6'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media2.cols('10'), plate4.cols('7'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media2.cols('10'), plate4.cols('8'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media2.cols('11'), plate4.cols('9'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media2.cols('11'), plate4.cols('10'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media2.cols('12'), plate4.cols('11'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media2.cols('12'), plate4.cols('12'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

####
# plate 5 - media 3

pipette.pick_up_tip()
pipette.transfer(150, media3.cols('1'), plate5.cols('1'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media3.cols('1'), plate5.cols('2'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media3.cols('2'), plate5.cols('3'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media3.cols('2'), plate5.cols('4'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media3.cols('3'), plate5.cols('5'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media3.cols('3'), plate5.cols('6'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media3.cols('4'), plate5.cols('7'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media3.cols('4'), plate5.cols('8'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media3.cols('5'), plate5.cols('9'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media3.cols('5'), plate5.cols('10'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(150, media3.cols('6'), plate5.cols('11'), mix_before = (1, 100), new_tip = 'never')
pipette.transfer(150, media3.cols('6'), plate5.cols('12'), mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

