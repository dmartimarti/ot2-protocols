'''
This code should transfer 50 uL between two columns
'''
from opentrons import labware, instruments

plate = labware.load('96-flat', '1')

tiprack = labware.load('tiprack-200ul', '2')

pipette = instruments.P300_Multi(mount = 'left')

# sets the speed of aspire and dispense
pipette.set_flow_rate(aspirate = 20, dispense = 40)

pipette.pick_up_tip(tiprack.cols('2'))

pipette.aspirate(20, plate.cols('4'))
pipette.dispense(20, plate.cols('3'))
# pipette.blow_out()

pipette.return_tip()


