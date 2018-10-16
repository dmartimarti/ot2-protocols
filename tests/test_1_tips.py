# -*- coding: utf-8 -*-
'''
This code will do some basic tip movements: 
picking a tip, move it to trash, change tips positions

Script by Dani Martinez, Oct - 2018
'''

from opentrons import labware, instruments, robot

#### labware creation

# load tip rack in position 2
tiprack = labware.load('tiprack-200ul', '3')
# load single pipette
pipette = instruments.P300_Single(mount = 'right')


#### actions 

### pick up tip, move to trash
# pick up a tip on A1
pipette.pick_up_tip(tiprack.wells('A1'))
# drop tip on trash
pipette.drop_tip()

### pick up a tip, move it to different position
# pick up a tip on A2
pipette.pick_up_tip(tiprack.wells('A2'))
# return tip to A1
pipette.drop_tip(tiprack.wells('A1'))