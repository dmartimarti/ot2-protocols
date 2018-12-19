# -*- coding: utf-8 -*-
'''

This script has two different parts. On the first part, it distributes 
media from a single reservoir to the 5 different plates per columns. The 
first 6 columns will have one condition, and columns 7 to 12 will have another
condition. 

On the second part, it seeds the plates with the bacterial strains in the bacterial
reservoir.

Script by Dani Martinez, Nov - 2018
Cabreiro Lab. 
'''

from opentrons import labware, instruments, robot


#### load labware

# load 5 different plates
plate1 = labware.load('96-flat', '4') # loads a 96-flat plate
plate2 = labware.load('96-flat', '5') # loads a 96-flat plate
plate3 = labware.load('96-flat', '7') # loads a 96-flat plate
plate4 = labware.load('96-flat', '8') # loads a 96-flat plate
plate5 = labware.load('96-flat', '9') # loads a 96-flat plate


# bacteria
media = labware.load('trough-12row', '2') # loads a trough-12row
bacteria = labware.load('96-deep-well', '1') # loads a trough-12row

# tip racks
tiprack1 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 
tiprack2 = labware.load('tiprack-200ul', '6') # loads a tip rack of 200 uL 

# pipette
pipette = instruments.P300_Multi(mount = 'right', tip_racks = [tiprack1, tiprack2])

# set pipette dispense rate a bit higher to avoid contamination
pipette.set_flow_rate(dispense = 250)

#### actions

### first step: pour media in all plates 

## first half

# fill plate 1 (half 1)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media.cols('1'), plate1.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 2 (half 1)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media.cols('2'), plate2.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 3 (half 1)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media.cols('3'), plate3.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 4 (half 1)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media.cols('4'), plate4.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 5 (half 1)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media.cols('5'), plate5.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()



## second half

# fill plate 1 (half 2)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media.cols('7'), plate1.cols(i + 6), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 2 (half 2)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media.cols('8'), plate2.cols(i + 6), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 3 (half 2)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media.cols('9'), plate3.cols(i + 6), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 4 (half 2)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media.cols('10'), plate4.cols(i + 6), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 5 (half 2)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(180, media.cols('11'), plate5.cols(i + 6), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()





### second step: seed plates with bacteria

# BW1
# plate 1
pipette.pick_up_tip()
pipette.transfer(20, bacteria.cols('1'), plate1.cols('1').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('1'), plate1.cols('7').top(), mix_before = (2, 100), new_tip = 'never')
# plate 2
pipette.transfer(20, bacteria.cols('1'), plate2.cols('1').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('1'), plate2.cols('7').top(), mix_before = (2, 100), new_tip = 'never')
# plate 3
pipette.transfer(20, bacteria.cols('1'), plate3.cols('1').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('1'), plate3.cols('7').top(), mix_before = (2, 100), new_tip = 'never')
# plate 4
pipette.transfer(20, bacteria.cols('1'), plate4.cols('1').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('1'), plate4.cols('7').top(), mix_before = (2, 100), new_tip = 'never')
# plate 5
pipette.transfer(20, bacteria.cols('1'), plate5.cols('1').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('1'), plate5.cols('7').top(), mix_before = (2, 100), trash = True)

# BW2
# plate 1
pipette.pick_up_tip()
pipette.transfer(20, bacteria.cols('2'), plate1.cols('2').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('2'), plate1.cols('8').top(), mix_before = (2, 100), new_tip = 'never')
# plate 2
pipette.transfer(20, bacteria.cols('2'), plate2.cols('2').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('2'), plate2.cols('8').top(), mix_before = (2, 100), new_tip = 'never')
# plate 3
pipette.transfer(20, bacteria.cols('2'), plate3.cols('2').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('2'), plate3.cols('8').top(), mix_before = (2, 100), new_tip = 'never')
# plate 4
pipette.transfer(20, bacteria.cols('2'), plate4.cols('2').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('2'), plate4.cols('8').top(), mix_before = (2, 100), new_tip = 'never')
# plate 5
pipette.transfer(20, bacteria.cols('2'), plate5.cols('2').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('2'), plate5.cols('8').top(), mix_before = (2, 100), trash = True)

# BW3
# plate 1
pipette.pick_up_tip()
pipette.transfer(20, bacteria.cols('3'), plate1.cols('3').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('3'), plate1.cols('9').top(), mix_before = (2, 100), new_tip = 'never')
# plate 2
pipette.transfer(20, bacteria.cols('3'), plate2.cols('3').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('3'), plate2.cols('9').top(), mix_before = (2, 100), new_tip = 'never')
# plate 3
pipette.transfer(20, bacteria.cols('3'), plate3.cols('3').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('3'), plate3.cols('9').top(), mix_before = (2, 100), new_tip = 'never')
# plate 4
pipette.transfer(20, bacteria.cols('3'), plate4.cols('3').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('3'), plate4.cols('9').top(), mix_before = (2, 100), new_tip = 'never')
# plate 5
pipette.transfer(20, bacteria.cols('3'), plate5.cols('3').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('3'), plate5.cols('9').top(), mix_before = (2, 100), trash = True)

# pyrE1
# plate 1
pipette.pick_up_tip()
pipette.transfer(20, bacteria.cols('4'), plate1.cols('4').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('4'), plate1.cols('10').top(), mix_before = (2, 100), new_tip = 'never')
# plate 2
pipette.transfer(20, bacteria.cols('4'), plate2.cols('4').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('4'), plate2.cols('10').top(), mix_before = (2, 100), new_tip = 'never')
# plate 3
pipette.transfer(20, bacteria.cols('4'), plate3.cols('4').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('4'), plate3.cols('10').top(), mix_before = (2, 100), new_tip = 'never')
# plate 4
pipette.transfer(20, bacteria.cols('4'), plate4.cols('4').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('4'), plate4.cols('10').top(), mix_before = (2, 100), new_tip = 'never')
# plate 5
pipette.transfer(20, bacteria.cols('4'), plate5.cols('4').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('4'), plate5.cols('10').top(), mix_before = (2, 100), trash = True)


# pyrE2
# plate 1
pipette.pick_up_tip()
pipette.transfer(20, bacteria.cols('5'), plate1.cols('5').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('5'), plate1.cols('11').top(), mix_before = (2, 100), new_tip = 'never')
# plate 2
pipette.transfer(20, bacteria.cols('5'), plate2.cols('5').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('5'), plate2.cols('11').top(), mix_before = (2, 100), new_tip = 'never')
# plate 3
pipette.transfer(20, bacteria.cols('5'), plate3.cols('5').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('5'), plate3.cols('11').top(), mix_before = (2, 100), new_tip = 'never')
# plate 4
pipette.transfer(20, bacteria.cols('5'), plate4.cols('5').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('5'), plate4.cols('11').top(), mix_before = (2, 100), new_tip = 'never')
# plate 5
pipette.transfer(20, bacteria.cols('5'), plate5.cols('5').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('5'), plate5.cols('11').top(), mix_before = (2, 100), trash = True)


# pyrE3
# plate 1
pipette.pick_up_tip()
pipette.transfer(20, bacteria.cols('6'), plate1.cols('6').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('6'), plate1.cols('12').top(), mix_before = (2, 100), new_tip = 'never')
# plate 2
pipette.transfer(20, bacteria.cols('6'), plate2.cols('6').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('6'), plate2.cols('12').top(), mix_before = (2, 100), new_tip = 'never')
# plate 3
pipette.transfer(20, bacteria.cols('6'), plate3.cols('6').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('6'), plate3.cols('12').top(), mix_before = (2, 100), new_tip = 'never')
# plate 4
pipette.transfer(20, bacteria.cols('6'), plate4.cols('6').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('6'), plate4.cols('12').top(), mix_before = (2, 100), new_tip = 'never')
# plate 5
pipette.transfer(20, bacteria.cols('6'), plate5.cols('6').top(), mix_before = (2, 100), new_tip = 'never')
pipette.transfer(20, bacteria.cols('6'), plate5.cols('12').top(), mix_before = (2, 100), trash = True)










