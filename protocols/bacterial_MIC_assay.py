# -*- coding: utf-8 -*-
'''
This script has two different parts. On the first part, it distributes 
media from a single reservoir to the 6 different plates per columns, and an
aditional control plate which comes from the second reservoir. On the second 
part, it seeds columns 2, 3, 4, 5 and 8, 9, 10, 11 with the 4 different 
bacterial strains in the bacteria reservoir. 

Notice that it does not seed columns 1, 6, 7 and 12 because it seems that 
the external wells are kind of special and you don't have good readings 
from them. 

It's and ugly code, but it works (hopefully).

Script by Dani Martinez, Nov - 2018
Cabreiro Lab. 
'''

from opentrons import labware, instruments, robot


#### load labware

# load 7 different plates
plate1 = labware.load('96-flat', '4') # loads a 96-flat plate
plate2 = labware.load('96-flat', '5') # loads a 96-flat plate
plate3 = labware.load('96-flat', '7') # loads a 96-flat plate
plate4 = labware.load('96-flat', '8') # loads a 96-flat plate
plate5 = labware.load('96-flat', '9') # loads a 96-flat plate
plate6 = labware.load('96-flat', '10') # loads a 96-flat plate
control = labware.load('96-flat', '11') # loads a 96-flat plate


# bacteria
media = labware.load('trough-12row', '2') # loads a trough-12row
bacteria = labware.load('trough-12row', '1') # loads a trough-12row

# tip racks
tiprack1 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 
tiprack2 = labware.load('tiprack-200ul', '6') # loads a tip rack of 200 uL 

pipette = instruments.P300_Multi(mount = 'right', tip_racks = [tiprack1, tiprack2])



#### actions

### first step: pour media in all plates 

## first half

# fill plate 1 (half 1)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('1'), plate1.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 2 (half 1)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('2'), plate2.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 3 (half 1)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('3'), plate3.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 4 (half 1)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('4'), plate4.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 5 (half 1)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('5'), plate5.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 6 (half 1)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('6'), plate6.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

## second half

# fill plate 1 (half 2)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('7'), plate1.cols(i + 6), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 2 (half 2)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('8'), plate2.cols(i + 6), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 3 (half 2)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('9'), plate3.cols(i + 6), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 4 (half 2)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('10'), plate4.cols(i + 6), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 5 (half 2)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('11'), plate5.cols(i + 6), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 6 (half 2)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('12'), plate6.cols(i + 6), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()



# contol plates
# without glucose
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, bacteria.cols('11'), control.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# with glucose
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, bacteria.cols('12'), control.cols(i + 6), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()




### second step: seed plates with bacteria

# BW1

pipette.pick_up_tip()
# plate 1
pipette.transfer(50, bacteria.cols('1'), plate1.cols('2').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('1'), plate1.cols('8').top(), mix_before = (2, 100), new_tip = 'never')
# plate 2
pipette.transfer(50, bacteria.cols('1'), plate2.cols('2').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('1'), plate2.cols('8').top(), mix_before = (2, 100), new_tip = 'never')
# plate 3
pipette.transfer(50, bacteria.cols('1'), plate3.cols('2').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('1'), plate3.cols('8').top(), mix_before = (2, 100), new_tip = 'never')
# plate 4
pipette.transfer(50, bacteria.cols('1'), plate4.cols('2').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('1'), plate4.cols('8').top(), mix_before = (2, 100), new_tip = 'never')
# plate 5
pipette.transfer(50, bacteria.cols('1'), plate5.cols('2').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('1'), plate5.cols('8').top(), mix_before = (2, 100), new_tip = 'never')
# plate 6
pipette.transfer(50, bacteria.cols('1'), plate6.cols('2').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('1'), plate6.cols('8').top(), mix_before = (2, 100), new_tip = 'never')
# control plate
pipette.transfer(50, bacteria.cols('1'), control.cols('2').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('1'), control.cols('8').top(), mix_before = (2, 100), trash = True)


# BW2

pipette.pick_up_tip()
# plate 1
pipette.transfer(50, bacteria.cols('2'), plate1.cols('3').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('2'), plate1.cols('9').top(), mix_before = (2, 100), new_tip = 'never')
# plate 2
pipette.transfer(50, bacteria.cols('2'), plate2.cols('3').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('2'), plate2.cols('9').top(), mix_before = (2, 100), new_tip = 'never')
# plate 3
pipette.transfer(50, bacteria.cols('2'), plate3.cols('3').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('2'), plate3.cols('9').top(), mix_before = (2, 100), new_tip = 'never')
# plate 4
pipette.transfer(50, bacteria.cols('2'), plate4.cols('3').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('2'), plate4.cols('9').top(), mix_before = (2, 100), new_tip = 'never')
# plate 5
pipette.transfer(50, bacteria.cols('2'), plate5.cols('3').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('2'), plate5.cols('9').top(), mix_before = (2, 100), new_tip = 'never')
# plate 6
pipette.transfer(50, bacteria.cols('2'), plate6.cols('3').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('2'), plate6.cols('9').top(), mix_before = (2, 100), new_tip = 'never')
# control plate
pipette.transfer(50, bacteria.cols('2'), control.cols('3').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('2'), control.cols('9').top(), mix_before = (2, 100), trash = True)


# BW3

pipette.pick_up_tip()
# plate 1
pipette.transfer(50, bacteria.cols('3'), plate1.cols('4').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('3'), plate1.cols('10').top(), mix_before = (2, 100), new_tip = 'never')
# plate 2
pipette.transfer(50, bacteria.cols('3'), plate2.cols('4').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('3'), plate2.cols('10').top(), mix_before = (2, 100), new_tip = 'never')
# plate 3
pipette.transfer(50, bacteria.cols('3'), plate3.cols('4').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('3'), plate3.cols('10').top(), mix_before = (2, 100), new_tip = 'never')
# plate 4
pipette.transfer(50, bacteria.cols('3'), plate4.cols('4').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('3'), plate4.cols('10').top(), mix_before = (2, 100), new_tip = 'never')
# plate 5
pipette.transfer(50, bacteria.cols('3'), plate5.cols('4').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('3'), plate5.cols('10').top(), mix_before = (2, 100), new_tip = 'never')
# plate 6
pipette.transfer(50, bacteria.cols('3'), plate6.cols('4').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('3'), plate6.cols('10').top(), mix_before = (2, 100), new_tip = 'never')
# control plate
pipette.transfer(50, bacteria.cols('3'), control.cols('4').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('3'), control.cols('10').top(), mix_before = (2, 100), trash = True)

# BW4

pipette.pick_up_tip()
# plate 1
pipette.transfer(50, bacteria.cols('4'), plate1.cols('5').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('4'), plate1.cols('11').top(), mix_before = (2, 100), new_tip = 'never')
# plate 2
pipette.transfer(50, bacteria.cols('4'), plate2.cols('5').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('4'), plate2.cols('11').top(), mix_before = (2, 100), new_tip = 'never')
# plate 3
pipette.transfer(50, bacteria.cols('4'), plate3.cols('5').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('4'), plate3.cols('11').top(), mix_before = (2, 100), new_tip = 'never')
# plate 4
pipette.transfer(50, bacteria.cols('4'), plate4.cols('5').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('4'), plate4.cols('11').top(), mix_before = (2, 100), new_tip = 'never')
# plate 5
pipette.transfer(50, bacteria.cols('4'), plate5.cols('5').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('4'), plate5.cols('11').top(), mix_before = (2, 100), new_tip = 'never')
# plate 6
pipette.transfer(50, bacteria.cols('4'), plate6.cols('5').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('4'), plate6.cols('11').top(), mix_before = (2, 100), new_tip = 'never')
# control plate
pipette.transfer(50, bacteria.cols('4'), control.cols('5').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(50, bacteria.cols('4'), control.cols('11').top(), mix_before = (2, 100), trash = True)








