'''
This code should transfer 50 uL between two positions
'''
from opentrons import labware, instruments

# load labware
plate = labware.load('96-flat', '1') # loads a 96-flat plate
tiprack = labware.load('tiprack-200ul', '2') # loads a tip rack of 200 uL 
pipette = instruments.P300_Single(mount = 'right') # loads the P300 single on the right arm


#### actions

# pick up a tip from tip rack at position A2
pipette.pick_up_tip(tiprack.wells('A2'))
# aspirate 50 uL from position B1
pipette.aspirate(50, plate.wells('B1'))
# dispense 50 uL to position A1
pipette.dispense(50, plate.wells('A1'))
pipette.blow_out() # blow out the remaining liquid


# drop tip on trash
pipette.return_tip()