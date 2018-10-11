'''
This code should transfer 50 uL between two columns
'''
from opentrons import labware, instruments

plate = labware.load('96-flat', '1')

tiprack = labware.load('tiprack-200ul', '2')

pipette = instruments.P300_Multi(mount = 'left')

pipette.pick_up_tip(tiprack.cols('1'))

pipette.aspirate(50, plate.cols('3'))
pipette.dispense(50, plate.cols('4'))
pipette.blow_out()

pipette.drop_tip()   