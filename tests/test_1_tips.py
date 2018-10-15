'''
This code transfer tips from one point to another
'''
from opentrons import labware, instruments, robot

# load tip rack
tiprack = labware.load('tiprack-200ul', '2')

# load pipette
pipette = instruments.P300_Single(mount = 'right')

# pick up a tip on A2
pipette.pick_up_tip(tiprack.wells('A2'))

# return tip to A1
pipette.drop_tip(tiprack.wells('A1'))

