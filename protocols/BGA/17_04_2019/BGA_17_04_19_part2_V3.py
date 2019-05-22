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

tiprack1 = labware.load('tiprack-200ul', '5') # loads a 96-flat plate
tiprack2 = labware.load('tiprack-200ul', '8') # loads a 96-flat plate
tiprack3 = labware.load('tiprack-200ul', '11') # loads a 96-flat plate

# reservoir
media1 = labware.load('96-deep-well', '1') # loads a 12 column reservoir

# pipette
pipette = instruments.P50_Multi(mount = 'right', tip_racks = [tiprack1, tiprack2, tiprack3])


## plate 1
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('1'), plate1.cols('2').bottom(4), mix_before = (1, 40))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('1'), plate1.cols('5').bottom(4))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('1'), plate1.cols('8').bottom(4))
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(20, media1.cols('2'), plate1.cols('3').bottom(4), mix_before = (1, 40))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('2'), plate1.cols('6').bottom(4))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('2'), plate1.cols('9').bottom(4))
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(20, media1.cols('3'), plate1.cols('4').bottom(4), mix_before = (1, 40))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('3'), plate1.cols('7').bottom(4))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('3'), plate1.cols('10').bottom(4))
pipette.drop_tip()


# plate 2

pipette.pick_up_tip()
pipette.transfer(20, media1.cols('1'), plate2.cols('2').bottom(4), mix_before = (1, 40))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('1'), plate2.cols('5').bottom(4))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('1'), plate2.cols('8').bottom(4))
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(20, media1.cols('2'), plate2.cols('3').bottom(4), mix_before = (1, 40))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('2'), plate2.cols('6').bottom(4))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('2'), plate2.cols('9').bottom(4))
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(20, media1.cols('3'), plate2.cols('4').bottom(4), mix_before = (1, 40))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('3'), plate2.cols('7').bottom(4))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('3'), plate2.cols('10').bottom(4))
pipette.drop_tip()



# plate 3


pipette.pick_up_tip()
pipette.transfer(20, media1.cols('1'), plate3.cols('2').bottom(4), mix_before = (1, 40))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('1'), plate3.cols('5').bottom(4))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('1'), plate3.cols('8').bottom(4))
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(20, media1.cols('2'), plate3.cols('3').bottom(4), mix_before = (1, 40))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('2'), plate3.cols('6').bottom(4))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('2'), plate3.cols('9').bottom(4))
pipette.drop_tip()

pipette.pick_up_tip()
pipette.transfer(20, media1.cols('3'), plate3.cols('4').bottom(4), mix_before = (1, 40))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('3'), plate3.cols('7').bottom(4))
pipette.drop_tip()
pipette.pick_up_tip()
pipette.transfer(20, media1.cols('3'), plate3.cols('10').bottom(4))
pipette.drop_tip()































