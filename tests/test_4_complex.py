# -*- coding: utf-8 -*-
'''
This code makes some complex transferences between positions

Script by Dani Martinez, Oct - 2018
'''

from opentrons import labware, instruments


#### load labware

plate = labware.load('96-flat', '1') # loads a 96-flat plate
reservoir = labware.load('96-flat', '2') # loads a 96-flat plate
tiprack = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 

pipette = instruments.P300_Single(
    mount='right',
    tip_racks=[tiprack])
pipette.min_volume = 20

#### actions

# this line will move 100 uL from every well in col 1 to every well in col 2
# pipette.transfer(100, plate.cols('1'), plate.cols('2'), new_tip = 'always', trash = False)

pipette.pick_up_tip(tiprack.wells('A1'))
pipette.transfer(100, reservoir.cols('1'), plate.cols('1'), new_tip = 'never', blow_out = True)
pipette.return_tip()


# this will pass different valumes to different wells
# pipette.transfer(
#	[20, 40, 60],
#	plate.wells('A1'),
#	plate.wells('B1', 'B2', 'B3'),
#	new_tip = 'never')

#  this will create a volume gradient from well A1 to every well in col 2
# pipette.transfer(
#	(100, 30),
#	plate.wells('A1'),
#	plate.rows('2'))

# this will ditribute from A1 and A2 to col 2, with a disposal vol of 10 uL.
# pipette.distribute(
#	30,
#	plate.wells('A1', 'A2'),
#	plate.rows('2'),
#	disposal_vol=10) 

# returns tip
# pipette.return_tip()