# -*- coding: utf-8 -*-
'''
This code should transfer 100 uL from the reservoir to the plate,
and then 50 uL from one well to the other

Script by Dani Martinez, Oct - 2018
'''
from opentrons import labware, instruments

# load labware
plate = labware.load('96-flat', '1') # loads a 96-flat plate
reservoir = labware.load('96-flat', '2') # loads a 96-flat plate
tiprack = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 

pipette = instruments.P300_Single(mount = 'right') # loads the P300 single on the right arm


#### actions
# pick up a tip
pipette.pick_up_tip(tiprack.wells('A1'))

### transfer 100 uL from reservoir to well A1
# aspirate 50 uL from position B1
pipette.aspirate(100, reservoir.wells('A1'))
# dispense 50 uL to position A1
pipette.dispense(100, plate.wells('A1'))

### transfer 50 uL from A1 to B1
# aspirate 50 uL from position A1 and dispense it to A2
pipette.transfer(50, plate.wells('A1'), plate.wells('A2'))

# return tip to tip rack
pipette.return_tip()