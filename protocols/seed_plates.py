# -*- coding: utf-8 -*-
'''
Seeding of 8 96-well plates with 150 uL of NGM agar from
a single reservoir (96-plate) with 180 uL of bacterial culture.
It starts from column 2 to column 11

Type of experiment: Developmental assay

Script by Dani Martinez, Cabreiro Lab., Oct - 2018
'''

from opentrons import labware, instruments, robot


#### load labware

# load 8 different plates
plate1 = labware.load('96-flat', '1') # loads a 96-flat plate
plate2 = labware.load('96-flat', '4') # loads a 96-flat plate
plate3 = labware.load('96-flat', '5') # loads a 96-flat plate
plate4 = labware.load('96-flat', '6') # loads a 96-flat plate
plate5 = labware.load('96-flat', '7') # loads a 96-flat plate
plate6 = labware.load('96-flat', '8') # loads a 96-flat plate
plate7 = labware.load('96-flat', '9') # loads a 96-flat plate
plate8 = labware.load('96-flat', '10') # loads a 96-flat plate

reservoir = labware.load('96-flat', '2') # loads a 96-flat plate
tiprack = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 

pipette = instruments.P50_Multi(mount = 'left', tip_racks = [tiprack])

pipette.set_flow_rate(dispense = 250)

#### actions

## something is buggy here, it should start by cols(2), not cols(1) ##
# col 2
pipette.pick_up_tip()

pipette.transfer(7, reservoir.cols(1), plate1.cols(1).bottom(7), mix_before = (2, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(1), plate2.cols(1).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(1), plate3.cols(1).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(1), plate4.cols(1).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(1), plate5.cols(1).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(1), plate6.cols(1).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(1), plate7.cols(1).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(1), plate8.cols(1).bottom(7), mix_before = (1, 30), trash = True)

# col 3
pipette.pick_up_tip()

pipette.transfer(7, reservoir.cols(2), plate1.cols(2).bottom(7), mix_before = (2, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(2), plate2.cols(2).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(2), plate3.cols(2).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(2), plate4.cols(2).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(2), plate5.cols(2).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(2), plate6.cols(2).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(2), plate7.cols(2).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(2), plate8.cols(2).bottom(7), mix_before = (1, 30), trash = True)

# col 4
pipette.pick_up_tip()

pipette.transfer(7, reservoir.cols(3), plate1.cols(3).bottom(7), mix_before = (2, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(3), plate2.cols(3).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(3), plate3.cols(3).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(3), plate4.cols(3).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(3), plate5.cols(3).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(3), plate6.cols(3).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(3), plate7.cols(3).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(3), plate8.cols(3).bottom(7), mix_before = (1, 30), trash = True)

# col 5
pipette.pick_up_tip()

pipette.transfer(7, reservoir.cols(4), plate1.cols(4).bottom(7), mix_before = (2, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(4), plate2.cols(4).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(4), plate3.cols(4).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(4), plate4.cols(4).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(4), plate5.cols(4).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(4), plate6.cols(4).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(4), plate7.cols(4).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(4), plate8.cols(4).bottom(7), mix_before = (1, 30), trash = True)

# col 6
pipette.pick_up_tip()

pipette.transfer(7, reservoir.cols(5), plate1.cols(5).bottom(7), mix_before = (2, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(5), plate2.cols(5).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(5), plate3.cols(5).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(5), plate4.cols(5).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(5), plate5.cols(5).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(5), plate6.cols(5).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(5), plate7.cols(5).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(5), plate8.cols(5).bottom(7), mix_before = (1, 30), trash = True)

# col 7
pipette.pick_up_tip()

pipette.transfer(7, reservoir.cols(6), plate1.cols(6).bottom(7), mix_before = (2, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(6), plate2.cols(6).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(6), plate3.cols(6).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(6), plate4.cols(6).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(6), plate5.cols(6).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(6), plate6.cols(6).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(6), plate7.cols(6).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(6), plate8.cols(6).bottom(7), mix_before = (1, 30), trash = True)

# col 8
pipette.pick_up_tip()

pipette.transfer(7, reservoir.cols(7), plate1.cols(7).bottom(7), mix_before = (2, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(7), plate2.cols(7).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(7), plate3.cols(7).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(7), plate4.cols(7).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(7), plate5.cols(7).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(7), plate6.cols(7).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(7), plate7.cols(7).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(7), plate8.cols(7).bottom(7), mix_before = (1, 30), trash = True)

# col 9
pipette.pick_up_tip()

pipette.transfer(7, reservoir.cols(8), plate1.cols(8).bottom(7), mix_before = (2, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(8), plate2.cols(8).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(8), plate3.cols(8).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(8), plate4.cols(8).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(8), plate5.cols(8).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(8), plate6.cols(8).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(8), plate7.cols(8).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(8), plate8.cols(8).bottom(7), mix_before = (1, 30), trash = True)

# col 10
pipette.pick_up_tip()

pipette.transfer(7, reservoir.cols(9), plate1.cols(9).bottom(7), mix_before = (2, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(9), plate2.cols(9).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(9), plate3.cols(9).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(9), plate4.cols(9).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(9), plate5.cols(9).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(9), plate6.cols(9).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(9), plate7.cols(9).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(9), plate8.cols(9).bottom(7), mix_before = (1, 30), trash = True)

# col 11
pipette.pick_up_tip()

pipette.transfer(7, reservoir.cols(10), plate1.cols(10).bottom(7), mix_before = (2, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(10), plate2.cols(10).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(10), plate3.cols(10).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(10), plate4.cols(10).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(10), plate5.cols(10).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(10), plate6.cols(10).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(10), plate7.cols(10).bottom(7), mix_before = (1, 30), new_tip = 'never')
pipette.transfer(7, reservoir.cols(10), plate8.cols(10).bottom(7), mix_before = (1, 30), trash = True)

# drop last tips to trash
pipette.drop_tip()
