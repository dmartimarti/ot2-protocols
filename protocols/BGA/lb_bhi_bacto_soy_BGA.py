# -*- coding: utf-8 -*-
'''
This script will add media from a 12-trough reservoir to 6 plates
for a BGA experiment. 
First part of the experiment. 

Script by Dani Martinez, Cabreiro Lab., Apr - 2019
'''

from opentrons import labware, instruments, robot


#### load labware

# load 6 different plates
lb_plate = labware.load('96-flat', '4') # loads a 96-flat plate
bhi_plate = labware.load('96-flat', '5') # loads a 96-flat plate
bacto_plate = labware.load('96-flat', '7') # loads a 96-flat plate
soy_plate = labware.load('96-flat', '8') # loads a 96-flat plate

# reservoir
media_res1 = labware.load('trough-12row', '1') # loads a 12 column reservoir
media_res2 = labware.load('trough-12row', '2') # loads a 12 column reservoir

# bacteria
bacteria = labware.load('96-flat', '9') # loads a 12 column reservoir


# tiprack
tiprack1 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 
tiprack2 = labware.load('tiprack-200ul', '6') # loads a tip rack of 200 uL 
tiprack3 = labware.load('tiprack-200ul', '11') # loads a tip rack of 200 uL 

# p300
p300 = instruments.P300_Multi(mount = 'right', tip_racks = [tiprack1, tiprack2])
p50 = instruments.P50_Multi(mount = 'left', tip_racks = [tiprack3])


p50.set_flow_rate(dispense = 300)



##############
### first set of actions: adding the media to the four plates 
##############


## LB medium

# 0 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res1.cols('1'), lb_plate.cols('1'), new_tip = 'never')
p300.transfer(180, media_res1.cols('1'), lb_plate.cols('2'), new_tip = 'never')
p300.transfer(180, media_res1.cols('1'), lb_plate.cols('3'), new_tip = 'never')
p300.drop_tip()

# 50 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res1.cols('2'), lb_plate.cols('4'), new_tip = 'never')
p300.transfer(180, media_res1.cols('2'), lb_plate.cols('5'), new_tip = 'never')
p300.drop_tip()

# 100 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res1.cols('3'), lb_plate.cols('6'), new_tip = 'never')
p300.transfer(180, media_res1.cols('3'), lb_plate.cols('7'), new_tip = 'never')
p300.drop_tip()


# 150 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res1.cols('4'), lb_plate.cols('8'), new_tip = 'never')
p300.transfer(180, media_res1.cols('4'), lb_plate.cols('9'), new_tip = 'never')
p300.drop_tip()

# 200 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res1.cols('5'), lb_plate.cols('10'), new_tip = 'never')
p300.transfer(180, media_res1.cols('5'), lb_plate.cols('11'), new_tip = 'never')
p300.transfer(180, media_res1.cols('5'), lb_plate.cols('12'), new_tip = 'never')
p300.drop_tip()


## BHI medium

# 0 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res1.cols('8'), bhi_plate.cols('1'), new_tip = 'never')
p300.transfer(180, media_res1.cols('8'), bhi_plate.cols('2'), new_tip = 'never')
p300.transfer(180, media_res1.cols('8'), bhi_plate.cols('3'), new_tip = 'never')
p300.drop_tip()

# 50 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res1.cols('9'), bhi_plate.cols('4'), new_tip = 'never')
p300.transfer(180, media_res1.cols('9'), bhi_plate.cols('5'), new_tip = 'never')
p300.drop_tip()

# 100 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res1.cols('10'), bhi_plate.cols('6'), new_tip = 'never')
p300.transfer(180, media_res1.cols('10'), bhi_plate.cols('7'), new_tip = 'never')
p300.drop_tip()


# 150 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res1.cols('11'), bhi_plate.cols('8'), new_tip = 'never')
p300.transfer(180, media_res1.cols('11'), bhi_plate.cols('9'), new_tip = 'never')
p300.drop_tip()

# 200 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res1.cols('12'), bhi_plate.cols('10'), new_tip = 'never')
p300.transfer(180, media_res1.cols('12'), bhi_plate.cols('11'), new_tip = 'never')
p300.transfer(180, media_res1.cols('12'), bhi_plate.cols('12'), new_tip = 'never')
p300.drop_tip()









## Bacto medium

# 0 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res2.cols('1'), bacto_plate.cols('1'), new_tip = 'never')
p300.transfer(180, media_res2.cols('1'), bacto_plate.cols('2'), new_tip = 'never')
p300.transfer(180, media_res2.cols('1'), bacto_plate.cols('3'), new_tip = 'never')
p300.drop_tip()

# 50 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res2.cols('2'), bacto_plate.cols('4'), new_tip = 'never')
p300.transfer(180, media_res2.cols('2'), bacto_plate.cols('5'), new_tip = 'never')
p300.drop_tip()

# 100 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res2.cols('3'), bacto_plate.cols('6'), new_tip = 'never')
p300.transfer(180, media_res2.cols('3'), bacto_plate.cols('7'), new_tip = 'never')
p300.drop_tip()


# 150 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res2.cols('4'), bacto_plate.cols('8'), new_tip = 'never')
p300.transfer(180, media_res2.cols('4'), bacto_plate.cols('9'), new_tip = 'never')
p300.drop_tip()

# 200 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res2.cols('5'), bacto_plate.cols('10'), new_tip = 'never')
p300.transfer(180, media_res2.cols('5'), bacto_plate.cols('11'), new_tip = 'never')
p300.transfer(180, media_res2.cols('5'), bacto_plate.cols('12'), new_tip = 'never')
p300.drop_tip()


## Soy medium

# 0 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res2.cols('8'), soy_plate.cols('1'), new_tip = 'never')
p300.transfer(180, media_res2.cols('8'), soy_plate.cols('2'), new_tip = 'never')
p300.transfer(180, media_res2.cols('8'), soy_plate.cols('3'), new_tip = 'never')
p300.drop_tip()

# 50 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res2.cols('9'), soy_plate.cols('4'), new_tip = 'never')
p300.transfer(180, media_res2.cols('9'), soy_plate.cols('5'), new_tip = 'never')
p300.drop_tip()

# 100 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res2.cols('10'), soy_plate.cols('6'), new_tip = 'never')
p300.transfer(180, media_res2.cols('10'), soy_plate.cols('7'), new_tip = 'never')
p300.drop_tip()


# 150 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res2.cols('11'), soy_plate.cols('8'), new_tip = 'never')
p300.transfer(180, media_res2.cols('11'), soy_plate.cols('9'), new_tip = 'never')
p300.drop_tip()

# 200 uM of 5FU
p300.pick_up_tip()
p300.transfer(180, media_res2.cols('12'), soy_plate.cols('10'), new_tip = 'never')
p300.transfer(180, media_res2.cols('12'), soy_plate.cols('11'), new_tip = 'never')
p300.transfer(180, media_res2.cols('12'), soy_plate.cols('12'), new_tip = 'never')
p300.drop_tip()






##############
### second set of actions: seed bacteria 
##############

# seed LB media
p50.pick_up_tip()
p50.mix(2, 40,   bacteria.cols('1'))
p50.transfer(20, bacteria.cols('1'), lb_plate.cols('1').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('1'), lb_plate.cols('2').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('1'), lb_plate.cols('3').top(), new_tip = 'never')
p50.mix(2, 40,   bacteria.cols('2'))
p50.transfer(20, bacteria.cols('2'), lb_plate.cols('4').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('2'), lb_plate.cols('5').top(), new_tip = 'never')
p50.mix(1, 40,   bacteria.cols('2'))
p50.transfer(20, bacteria.cols('2'), lb_plate.cols('6').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('2'), lb_plate.cols('7').top(), new_tip = 'never')
p50.mix(1, 40,   bacteria.cols('2'))
p50.transfer(20, bacteria.cols('2'), lb_plate.cols('8').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('2'), lb_plate.cols('9').top(), new_tip = 'never')
p50.mix(2, 40,   bacteria.cols('3'))
p50.transfer(20, bacteria.cols('3'), lb_plate.cols('10').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('3'), lb_plate.cols('11').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('3'), lb_plate.cols('12').top(), new_tip = 'never')
p50.drop_tip()


# seed BHI media
p50.pick_up_tip()
p50.mix(2, 40,   bacteria.cols('4'))
p50.transfer(20, bacteria.cols('4'), bhi_plate.cols('1').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('4'), bhi_plate.cols('2').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('4'), bhi_plate.cols('3').top(), new_tip = 'never')
p50.mix(2, 40,   bacteria.cols('5'))
p50.transfer(20, bacteria.cols('5'), bhi_plate.cols('4').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('5'), bhi_plate.cols('5').top(), new_tip = 'never')
p50.mix(1, 40,   bacteria.cols('5'))
p50.transfer(20, bacteria.cols('5'), bhi_plate.cols('6').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('5'), bhi_plate.cols('7').top(), new_tip = 'never')
p50.mix(1, 40,   bacteria.cols('5'))
p50.transfer(20, bacteria.cols('5'), bhi_plate.cols('8').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('5'), bhi_plate.cols('9').top(), new_tip = 'never')
p50.mix(2, 40,   bacteria.cols('6'))
p50.transfer(20, bacteria.cols('6'), bhi_plate.cols('10').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('6'), bhi_plate.cols('11').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('6'), bhi_plate.cols('12').top(), new_tip = 'never')
p50.drop_tip()



# seed Bacto media
p50.pick_up_tip()
p50.mix(2, 40,   bacteria.cols('7'))
p50.transfer(20, bacteria.cols('7'), bacto_plate.cols('1').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('7'), bacto_plate.cols('2').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('7'), bacto_plate.cols('3').top(), new_tip = 'never')
p50.mix(2, 40,   bacteria.cols('8'))
p50.transfer(20, bacteria.cols('8'), bacto_plate.cols('4').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('8'), bacto_plate.cols('5').top(), new_tip = 'never')
p50.mix(1, 40,   bacteria.cols('8'))
p50.transfer(20, bacteria.cols('8'), bacto_plate.cols('6').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('8'), bacto_plate.cols('7').top(), new_tip = 'never')
p50.mix(1, 40,   bacteria.cols('8'))
p50.transfer(20, bacteria.cols('8'), bacto_plate.cols('8').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('8'), bacto_plate.cols('9').top(), new_tip = 'never')
p50.mix(2, 40,   bacteria.cols('9'))
p50.transfer(20, bacteria.cols('9'), bacto_plate.cols('10').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('9'), bacto_plate.cols('11').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('9'), bacto_plate.cols('12').top(), new_tip = 'never')
p50.drop_tip()



# seed Soy media
p50.pick_up_tip()
p50.mix(2, 40,   bacteria.cols('10'))
p50.transfer(20, bacteria.cols('10'), soy_plate.cols('1').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('10'), soy_plate.cols('2').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('10'), soy_plate.cols('3').top(), new_tip = 'never')
p50.mix(2, 40,   bacteria.cols('11'))
p50.transfer(20, bacteria.cols('11'), soy_plate.cols('4').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('11'), soy_plate.cols('5').top(), new_tip = 'never')
p50.mix(1, 40,   bacteria.cols('11'))
p50.transfer(20, bacteria.cols('11'), soy_plate.cols('6').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('11'), soy_plate.cols('7').top(), new_tip = 'never')
p50.mix(1, 40,   bacteria.cols('11'))
p50.transfer(20, bacteria.cols('11'), soy_plate.cols('8').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('11'), soy_plate.cols('9').top(), new_tip = 'never')
p50.mix(2, 40,   bacteria.cols('12'))
p50.transfer(20, bacteria.cols('12'), soy_plate.cols('10').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('12'), soy_plate.cols('11').top(), new_tip = 'never')
p50.transfer(20, bacteria.cols('12'), soy_plate.cols('12').top(), new_tip = 'never')
p50.drop_tip()












