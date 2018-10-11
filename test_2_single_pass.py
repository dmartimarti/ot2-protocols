'''
This code should transfer 50 uL between two positions
'''
from opentrons import labware, instruments

plate = labware.load('96-flat', '1')

tiprack = labware.load('tiprack-200ul', '2')

pipette = instruments.P300_Single(mount = 'right')

pipette.pick_up_tip(tiprack.wells('A2'))

pipette.aspirate(50, plate.wells('B1'))

pipette.dispense(50, plate.wells('A1'))
pipette.blow_out()


# drop tip on trash
pipette.drop_tip()     
