# -*- coding: utf-8 -*-
'''
This script will add media from a 12-trough reservoir to 6 plates
for a BGA experiment. 
First part of the experiment. 

Script by Dani Martinez, Apr - 2019
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
media1 = labware.load('96-deep-well', '1') # loads a 12 column reservoir

# tiprack
tiprack1 = labware.load('tiprack-200ul', '2') # loads a tip rack of 200 uL 

# pipette
pipette = instruments.P50_Multi(mount = 'left', tip_racks = [tiprack1])

pipette.set_flow_rate(dispense = 300)


# Biological replicate 1
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('1'), plate1.cols('2').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('1'), plate1.cols('5').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('1'), plate1.cols('8').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('1'), plate2.cols('2').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('1'), plate2.cols('5').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('1'), plate2.cols('8').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('1'), plate3.cols('2').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('1'), plate3.cols('5').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('1'), plate3.cols('8').top(), new_tip = 'never')
pipette.drop_tip()

# Biological replicate 1
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('4'), plate4.cols('2').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('4'), plate4.cols('5').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('4'), plate4.cols('8').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('4'), plate5.cols('2').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('4'), plate5.cols('5').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('4'), plate5.cols('8').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('4'), plate6.cols('2').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('4'), plate6.cols('5').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('4'), plate6.cols('8').top(), new_tip = 'never')
pipette.drop_tip()


# Biological replicate 2
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('2'), plate1.cols('3').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('2'), plate1.cols('6').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('2'), plate1.cols('9').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('2'), plate2.cols('3').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('2'), plate2.cols('6').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('2'), plate2.cols('9').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('2'), plate3.cols('3').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('2'), plate3.cols('6').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('2'), plate3.cols('9').top(), new_tip = 'never')
pipette.drop_tip()

# Biological replicate 2
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('5'), plate4.cols('3').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('5'), plate4.cols('6').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('5'), plate4.cols('9').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('5'), plate5.cols('3').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('5'), plate5.cols('6').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('5'), plate5.cols('9').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('5'), plate6.cols('3').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('5'), plate6.cols('6').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('5'), plate6.cols('9').top(), new_tip = 'never')
pipette.drop_tip()


# Biological replicate 3
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('3'), plate1.cols('4').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('3'), plate1.cols('7').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('3'), plate1.cols('10').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('3'), plate2.cols('4').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('3'), plate2.cols('7').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('3'), plate2.cols('10').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('3'), plate3.cols('4').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('3'), plate3.cols('7').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('3'), plate3.cols('10').top(), new_tip = 'never')
pipette.drop_tip()

# Biological replicate 3
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('6'), plate4.cols('4').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('6'), plate4.cols('7').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('6'), plate4.cols('10').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('6'), plate5.cols('4').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('6'), plate5.cols('7').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('6'), plate5.cols('10').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('6'), plate6.cols('4').top(), mix_before = (1, 40), new_tip = 'never')
pipette.transfer(20, media1.cols('6'), plate6.cols('7').top(), new_tip = 'never')
pipette.transfer(20, media1.cols('6'), plate6.cols('10').top(), new_tip = 'never')
pipette.drop_tip()






