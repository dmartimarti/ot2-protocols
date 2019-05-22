# -*- coding: utf-8 -*-
'''
MIC experiment, two parts. 

The first part will add all the media1 to each plate. Each plate will have 4 columns
with a different drug concentration starting from 0, to 1024 uM of 5FU.

Script by Dani Martinez, May - 2019
'''

from opentrons import labware, instruments, robot


#### load labware

# load 4 different plates
plate1 = labware.load('96-flat', '4') # loads a 96-flat plate
plate2 = labware.load('96-flat', '7') # loads a 96-flat plate
plate3 = labware.load('96-flat', '8') # loads a 96-flat plate
plate4 = labware.load('96-flat', '10') # loads a 96-flat plate
plate5 = labware.load('96-flat', '11') # loads a 96-flat plate


# reservoir
bact = labware.load('96-deep-well', '1') # loads a 96-deep plate

# tiprack
tiprack1 = labware.load('tiprack-200ul', '2') # loads a tip rack of 200 uL 
tiprack2 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 
tiprack3 = labware.load('tiprack-200ul', '5') # loads a tip rack of 200 uL 
tiprack4 = labware.load('tiprack-200ul', '6') # loads a tip rack of 200 uL 
tiprack5 = labware.load('tiprack-200ul', '7') # loads a tip rack of 200 uL 


# pipette
pipette = instruments.P300_Multi(mount = 'left', 
	tip_racks = [tiprack1, tiprack2, tiprack3, tiprack4, tiprack5])



## Plate 1
for i in [0,4,8]:
	pipette.transfer(50, bact.cols('1'), plate1.cols(i).bottom(4))

for i in [1,5,9]:
	pipette.transfer(50, bact.cols('2'), plate1.cols(i).bottom(4))

for i in [2,6,10]:
	pipette.transfer(50, bact.cols('3'), plate1.cols(i).bottom(4))

for i in [3,7,11]:
	pipette.transfer(50, bact.cols('4'), plate1.cols(i).bottom(4))



## Plate 2
for i in [0,4,8]:
	pipette.transfer(50, bact.cols('1'), plate2.cols(i).bottom(4))

for i in [1,5,9]:
	pipette.transfer(50, bact.cols('2'), plate2.cols(i).bottom(4))

for i in [2,6,10]:
	pipette.transfer(50, bact.cols('3'), plate2.cols(i).bottom(4))

for i in [3,7,11]:
	pipette.transfer(50, bact.cols('4'), plate2.cols(i).bottom(4))


## Plate 3
for i in [0,4,8]:
	pipette.transfer(50, bact.cols('1'), plate3.cols(i).bottom(4))

for i in [1,5,9]:
	pipette.transfer(50, bact.cols('2'), plate3.cols(i).bottom(4))

for i in [2,6,10]:
	pipette.transfer(50, bact.cols('3'), plate3.cols(i).bottom(4))

for i in [3,7,11]:
	pipette.transfer(50, bact.cols('4'), plate3.cols(i).bottom(4))



## Plate 4
for i in [0,4,8]:
	pipette.transfer(50, bact.cols('1'), plate4.cols(i).bottom(4))

for i in [1,5,9]:
	pipette.transfer(50, bact.cols('2'), plate4.cols(i).bottom(4))

for i in [2,6,10]:
	pipette.transfer(50, bact.cols('3'), plate4.cols(i).bottom(4))

for i in [3,7,11]:
	pipette.transfer(50, bact.cols('4'), plate4.cols(i).bottom(4))



## Plate 5
for i in [0,4,8]:
	pipette.transfer(50, bact.cols('1'), plate5.cols(i).bottom(4))

for i in [1,5,9]:
	pipette.transfer(50, bact.cols('2'), plate5.cols(i).bottom(4))

for i in [2,6,10]:
	pipette.transfer(50, bact.cols('3'), plate5.cols(i).bottom(4))

for i in [3,7,11]:
	pipette.transfer(50, bact.cols('4'), plate5.cols(i).bottom(4))
