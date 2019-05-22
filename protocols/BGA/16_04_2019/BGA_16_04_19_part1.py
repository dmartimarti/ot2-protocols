# -*- coding: utf-8 -*-
'''
This script will add media from a 12-trough reservoir to 6 plates
for a BGA experiment. 
First part of the experiment. 

Script by Dani Martinez, Apr - 2019
'''

from opentrons import labware, instruments, robot


#### load labware

# load 6 different plates
plate1 = labware.load('96-flat', '4') # loads a 96-flat plate
plate2 = labware.load('96-flat', '7') # loads a 96-flat plate
plate3 = labware.load('96-flat', '10') # loads a 96-flat plate

plate4 = labware.load('96-flat', '5') # loads a 96-flat plate
plate5 = labware.load('96-flat', '8') # loads a 96-flat plate
plate6 = labware.load('96-flat', '11') # loads a 96-flat plate

# reservoir
media1 = labware.load('trough-12row', '1') # loads a 12 column reservoir
media2 = labware.load('trough-12row', '2') # loads a 12 column reservoir
# tiprack
tiprack1 = labware.load('tiprack-200ul', '6') # loads a tip rack of 200 uL 
tiprack2 = labware.load('tiprack-200ul', '9') # loads a tip rack of 200 uL 

# pipette
pipette = instruments.P300_Multi(mount = 'right', tip_racks = [tiprack1, tiprack2])

pipette.set_flow_rate(dispense = 300)


## actions

## plate 1
# 0 uM - Media 1
pipette.pick_up_tip()
pipette.transfer(180, media1.cols('1'), plate1.cols('1'), new_tip = 'never')
pipette.transfer(180, media1.cols('1'), plate1.cols('2'), new_tip = 'never')
pipette.transfer(180, media1.cols('1'), plate1.cols('3'), new_tip = 'never')
pipette.transfer(180, media1.cols('1'), plate1.cols('4'), new_tip = 'never')
pipette.drop_tip()

# 1 uM - Media 1
pipette.pick_up_tip()
pipette.transfer(180, media1.cols('2'), plate1.cols('5'), new_tip = 'never')
pipette.transfer(180, media1.cols('2'), plate1.cols('6'), new_tip = 'never')
pipette.transfer(180, media1.cols('2'), plate1.cols('7'), new_tip = 'never')
pipette.drop_tip()

# 2 uM - Media 1
pipette.pick_up_tip()
pipette.transfer(180, media1.cols('3'), plate1.cols('8'), new_tip = 'never')
pipette.transfer(180, media1.cols('3'), plate1.cols('9'), new_tip = 'never')
pipette.transfer(180, media1.cols('3'), plate1.cols('10'), new_tip = 'never')
pipette.transfer(180, media1.cols('3'), plate1.cols('11'), new_tip = 'never')
pipette.transfer(180, media1.cols('3'), plate1.cols('12'), new_tip = 'never')
pipette.drop_tip()





## plate 2
# 4 uM - Media 2
pipette.pick_up_tip()
pipette.transfer(180, media1.cols('4'), plate2.cols('1'), new_tip = 'never')
pipette.transfer(180, media1.cols('4'), plate2.cols('2'), new_tip = 'never')
pipette.transfer(180, media1.cols('4'), plate2.cols('3'), new_tip = 'never')
pipette.transfer(180, media1.cols('4'), plate2.cols('4'), new_tip = 'never')
pipette.drop_tip()

# 8 uM - Media 2
pipette.pick_up_tip()
pipette.transfer(180, media1.cols('5'), plate2.cols('5'), new_tip = 'never')
pipette.transfer(180, media1.cols('5'), plate2.cols('6'), new_tip = 'never')
pipette.transfer(180, media1.cols('5'), plate2.cols('7'), new_tip = 'never')
pipette.drop_tip()

# 16 uM - Media 2
pipette.pick_up_tip()
pipette.transfer(180, media1.cols('6'), plate2.cols('8'), new_tip = 'never')
pipette.transfer(180, media1.cols('6'), plate2.cols('9'), new_tip = 'never')
pipette.transfer(180, media1.cols('6'), plate2.cols('10'), new_tip = 'never')
pipette.transfer(180, media1.cols('6'), plate2.cols('11'), new_tip = 'never')
pipette.transfer(180, media1.cols('6'), plate2.cols('12'), new_tip = 'never')
pipette.drop_tip()




## plate 3
# 32 uM - Media 3
pipette.pick_up_tip()
pipette.transfer(180, media1.cols('7'), plate3.cols('1'), new_tip = 'never')
pipette.transfer(180, media1.cols('7'), plate3.cols('2'), new_tip = 'never')
pipette.transfer(180, media1.cols('7'), plate3.cols('3'), new_tip = 'never')
pipette.transfer(180, media1.cols('7'), plate3.cols('4'), new_tip = 'never')
pipette.drop_tip()

# 64 uM - Media 3
pipette.pick_up_tip()
pipette.transfer(180, media1.cols('8'), plate3.cols('5'), new_tip = 'never')
pipette.transfer(180, media1.cols('8'), plate3.cols('6'), new_tip = 'never')
pipette.transfer(180, media1.cols('8'), plate3.cols('7'), new_tip = 'never')
pipette.drop_tip()

# 128 uM - Media 3
pipette.pick_up_tip()
pipette.transfer(180, media1.cols('9'), plate3.cols('8'), new_tip = 'never')
pipette.transfer(180, media1.cols('9'), plate3.cols('9'), new_tip = 'never')
pipette.transfer(180, media1.cols('9'), plate3.cols('10'), new_tip = 'never')
pipette.transfer(180, media1.cols('9'), plate3.cols('11'), new_tip = 'never')
pipette.transfer(180, media1.cols('9'), plate3.cols('12'), new_tip = 'never')
pipette.drop_tip()


###############################

## plate 4
# 0 uM - Media 4
pipette.pick_up_tip()
pipette.transfer(180, media2.cols('1'), plate4.cols('1'), new_tip = 'never')
pipette.transfer(180, media2.cols('1'), plate4.cols('2'), new_tip = 'never')
pipette.transfer(180, media2.cols('1'), plate4.cols('3'), new_tip = 'never')
pipette.transfer(180, media2.cols('1'), plate4.cols('4'), new_tip = 'never')
pipette.drop_tip()

# 1 uM - Media 4
pipette.pick_up_tip()
pipette.transfer(180, media2.cols('2'), plate4.cols('5'), new_tip = 'never')
pipette.transfer(180, media2.cols('2'), plate4.cols('6'), new_tip = 'never')
pipette.transfer(180, media2.cols('2'), plate4.cols('7'), new_tip = 'never')
pipette.drop_tip()

# 2 uM - Media 4
pipette.pick_up_tip()
pipette.transfer(180, media2.cols('3'), plate4.cols('8'), new_tip = 'never')
pipette.transfer(180, media2.cols('3'), plate4.cols('9'), new_tip = 'never')
pipette.transfer(180, media2.cols('3'), plate4.cols('10'), new_tip = 'never')
pipette.transfer(180, media2.cols('3'), plate4.cols('11'), new_tip = 'never')
pipette.transfer(180, media2.cols('3'), plate4.cols('12'), new_tip = 'never')
pipette.drop_tip()





## plate 5
# 4 uM - Media 5
pipette.pick_up_tip()
pipette.transfer(180, media2.cols('4'), plate5.cols('1'), new_tip = 'never')
pipette.transfer(180, media2.cols('4'), plate5.cols('2'), new_tip = 'never')
pipette.transfer(180, media2.cols('4'), plate5.cols('3'), new_tip = 'never')
pipette.transfer(180, media2.cols('4'), plate5.cols('4'), new_tip = 'never')
pipette.drop_tip()

# 8 uM - Media 5
pipette.pick_up_tip()
pipette.transfer(180, media2.cols('5'), plate5.cols('5'), new_tip = 'never')
pipette.transfer(180, media2.cols('5'), plate5.cols('6'), new_tip = 'never')
pipette.transfer(180, media2.cols('5'), plate5.cols('7'), new_tip = 'never')
pipette.drop_tip()

# 16 uM - Media 5
pipette.pick_up_tip()
pipette.transfer(180, media2.cols('6'), plate5.cols('8'), new_tip = 'never')
pipette.transfer(180, media2.cols('6'), plate5.cols('9'), new_tip = 'never')
pipette.transfer(180, media2.cols('6'), plate5.cols('10'), new_tip = 'never')
pipette.transfer(180, media2.cols('6'), plate5.cols('11'), new_tip = 'never')
pipette.transfer(180, media2.cols('6'), plate5.cols('12'), new_tip = 'never')
pipette.drop_tip()




## plate 6
# 32 uM - Media 6
pipette.pick_up_tip()
pipette.transfer(180, media2.cols('7'), plate6.cols('1'), new_tip = 'never')
pipette.transfer(180, media2.cols('7'), plate6.cols('2'), new_tip = 'never')
pipette.transfer(180, media2.cols('7'), plate6.cols('3'), new_tip = 'never')
pipette.transfer(180, media2.cols('7'), plate6.cols('4'), new_tip = 'never')
pipette.drop_tip()

# 64 uM - Media 6
pipette.pick_up_tip()
pipette.transfer(180, media2.cols('8'), plate6.cols('5'), new_tip = 'never')
pipette.transfer(180, media2.cols('8'), plate6.cols('6'), new_tip = 'never')
pipette.transfer(180, media2.cols('8'), plate6.cols('7'), new_tip = 'never')
pipette.drop_tip()

# 128 uM - Media 6
pipette.pick_up_tip()
pipette.transfer(180, media2.cols('9'), plate6.cols('8'), new_tip = 'never')
pipette.transfer(180, media2.cols('9'), plate6.cols('9'), new_tip = 'never')
pipette.transfer(180, media2.cols('9'), plate6.cols('10'), new_tip = 'never')
pipette.transfer(180, media2.cols('9'), plate6.cols('11'), new_tip = 'never')
pipette.transfer(180, media2.cols('9'), plate6.cols('12'), new_tip = 'never')
pipette.drop_tip()











