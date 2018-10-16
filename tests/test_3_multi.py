# -*- coding: utf-8 -*-
'''
This code transfers 100 uL from reservoir to two columns,
and then 50 uL from col 1 to col 2

Script by Dani Martinez, Oct - 2018
'''

from opentrons import labware, instruments

#### load labware

plate = labware.load('96-flat', '1') # loads a 96-flat plate
reservoir = labware.load('96-flat', '2') # loads a 96-flat plate
tiprack = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 

pipette = instruments.P300_Multi(mount = 'left')

#### actions

# pick up a column of tips
pipette.pick_up_tip(tiprack.cols('1'))

### transfer 100 uL from reservoir, dispense it in two columns
pipette.aspirate(100, reservoir.cols('1'))
pipette.dispense(50, plate.cols('1'))
pipette.dispense(50, plate.cols('2'))
# pipette.blow_out()

### transfer 40 uL from col 1 to col 2
pipette.transfer(50, plate.cols('1'), plate.cols('2'))

pipette.return_tip()