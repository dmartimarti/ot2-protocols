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

# reservoir
media1 = labware.load('96-deep-well', '1') # loads a 12 column reservoir

# tiprack
tiprack1 = labware.load('tiprack-200ul', '2') # loads a tip rack of 200 uL 

# pipette
pipette = instruments.P50_Multi(mount = 'right', tip_racks = [tiprack1])



## test 1: aspirate higher volume

pipette.pick_up_tip()
pipette.aspirate(25, media1.cols('1'))  
pipette.dispense(20,plate1.cols('1'))
pipette.drop_tip()

## test 2: disposal volume

pipette.transfer(20, media1.cols('1'), plate1.cols('2').top(), mix_before = (1, 40), disposal_vol = 5)


## test 3: touching tips

pipette.transfer(20, media1.cols('1'), plate1.cols('3').bottom(8), mix_before = (1, 40), touch_tip = True)

## test 4: blow out

pipette.transfer(20, media1.cols('1'), plate1.cols('4').bottom(8), mix_before = (1, 40), blow_out=True)
