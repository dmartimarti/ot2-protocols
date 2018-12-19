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

for i in range(12):
	pipette.pick_up_tip()
	pipette.transfer(7, reservoir.cols(i), plate1.cols(i).bottom(7), mix_before = (1, 100), new_tip = 'never')
	pipette.transfer(7, reservoir.cols(i), plate2.cols(i).bottom(7), mix_before = (1, 100), new_tip = 'never')
	pipette.transfer(7, reservoir.cols(i), plate3.cols(i).bottom(7), mix_before = (1, 100), new_tip = 'never')
	pipette.transfer(7, reservoir.cols(i), plate4.cols(i).bottom(7), mix_before = (1, 100), new_tip = 'never')
	pipette.transfer(7, reservoir.cols(i), plate5.cols(i).bottom(7), mix_before = (1, 100), new_tip = 'never')
	pipette.transfer(7, reservoir.cols(i), plate6.cols(i).bottom(7), mix_before = (1, 100), new_tip = 'never')
	pipette.transfer(7, reservoir.cols(i), plate7.cols(i).bottom(7), mix_before = (1, 100), new_tip = 'never')
	pipette.transfer(7, reservoir.cols(i), plate8.cols(i).bottom(7), mix_before = (1, 100), new_tip = 'never')
	pipette.drop_tip()
