from opentrons import labware, instruments, robot

"""
Specify what this script will do, with precission
"""

# creating a 24-well plate, because Opentrons sucks
plate_name = '24-well-plate'
if plate_name not in labware.list():
    custom_plate = labware.create(
        plate_name,
        grid = (4, 6),
        spacing = (19, 19),
        diameter = 17,
        depth = 20,
        volume = 2000)


#### load labware

# load 8 different plates
plate1 = labware.load(custom_plate, '4') # loads a 96-flat plate
plate2 = labware.load(custom_plate, '5') # loads a 96-flat plate
plate3 = labware.load(custom_plate, '6') # loads a 96-flat plate
plate4 = labware.load(custom_plate, '7') # loads a 96-flat plate
plate5 = labware.load(custom_plate, '8') # loads a 96-flat plate
plate6 = labware.load(custom_plate, '9') # loads a 96-flat plate
plate7 = labware.load(custom_plate, '10') # loads a 96-flat plate
plate8 = labware.load(custom_plate, '11') # loads a 96-flat plate

# reservoir
keio = labware.load('96-flat', '1') # loads a 96-flat plate
# tiprack
tiprack1 = labware.load('tiprack-200ul', '2') # loads a tip rack of 200 uL 
tiprack2 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 
# pipette
pipette = instruments.P300_Single(mount = 'right', tip_racks = [tiprack1, tiprack2])

# pipette.set_flow_rate(dispense = 300) 

#### actions

# first plate
pipette.distribute(50, keio.wells('A1'),  plate1.wells('A1', 'B1'))
pipette.distribute(50, keio.wells('A2'),  plate1.wells('A2', 'B2'))
pipette.distribute(50, keio.wells('A3'),  plate1.wells('A3', 'B3'))
pipette.distribute(50, keio.wells('A4'),  plate1.wells('A4', 'B4'))
pipette.distribute(50, keio.wells('A5'),  plate1.wells('A5', 'B5'))
pipette.distribute(50, keio.wells('A6'),  plate1.wells('A6', 'B6'))
pipette.distribute(50, keio.wells('A7'),  plate1.wells('C1', 'D1'))
pipette.distribute(50, keio.wells('A8'),  plate1.wells('C2', 'D2'))
pipette.distribute(50, keio.wells('A9'),  plate1.wells('C3', 'D3'))
pipette.distribute(50, keio.wells('A10'), plate1.wells('C4', 'D4'))
pipette.distribute(50, keio.wells('A11'), plate1.wells('C5', 'D5'))
pipette.distribute(50, keio.wells('A12'), plate1.wells('C6', 'D6'))

# second plate
pipette.distribute(50, keio.wells('B1'),  plate2.wells('A1', 'B1'))
pipette.distribute(50, keio.wells('B2'),  plate2.wells('A2', 'B2'))
pipette.distribute(50, keio.wells('B3'),  plate2.wells('A3', 'B3'))
pipette.distribute(50, keio.wells('B4'),  plate2.wells('A4', 'B4'))
pipette.distribute(50, keio.wells('B5'),  plate2.wells('A5', 'B5'))
pipette.distribute(50, keio.wells('B6'),  plate2.wells('A6', 'B6'))
pipette.distribute(50, keio.wells('B7'),  plate2.wells('C1', 'D1'))
pipette.distribute(50, keio.wells('B8'),  plate2.wells('C2', 'D2'))
pipette.distribute(50, keio.wells('B9'),  plate2.wells('C3', 'D3'))
pipette.distribute(50, keio.wells('B10'), plate2.wells('C4', 'D4'))
pipette.distribute(50, keio.wells('B11'), plate2.wells('C5', 'D5'))
pipette.distribute(50, keio.wells('B12'), plate2.wells('C6', 'D6'))

# third plate
pipette.distribute(50, keio.wells('C1'),  plate3.wells('A1', 'B1'))
pipette.distribute(50, keio.wells('C2'),  plate3.wells('A2', 'B2'))
pipette.distribute(50, keio.wells('C3'),  plate3.wells('A3', 'B3'))
pipette.distribute(50, keio.wells('C4'),  plate3.wells('A4', 'B4'))
pipette.distribute(50, keio.wells('C5'),  plate3.wells('A5', 'B5'))
pipette.distribute(50, keio.wells('C6'),  plate3.wells('A6', 'B6'))
pipette.distribute(50, keio.wells('C7'),  plate3.wells('C1', 'D1'))
pipette.distribute(50, keio.wells('C8'),  plate3.wells('C2', 'D2'))
pipette.distribute(50, keio.wells('C9'),  plate3.wells('C3', 'D3'))
pipette.distribute(50, keio.wells('C10'), plate3.wells('C4', 'D4'))
pipette.distribute(50, keio.wells('C11'), plate3.wells('C5', 'D5'))
pipette.distribute(50, keio.wells('C12'), plate3.wells('C6', 'D6'))

# fourth plate
pipette.distribute(50, keio.wells('D1'),  plate4.wells('A1', 'B1'))
pipette.distribute(50, keio.wells('D2'),  plate4.wells('A2', 'B2'))
pipette.distribute(50, keio.wells('D3'),  plate4.wells('A3', 'B3'))
pipette.distribute(50, keio.wells('D4'),  plate4.wells('A4', 'B4'))
pipette.distribute(50, keio.wells('D5'),  plate4.wells('A5', 'B5'))
pipette.distribute(50, keio.wells('D6'),  plate4.wells('A6', 'B6'))
pipette.distribute(50, keio.wells('D7'),  plate4.wells('C1', 'D1'))
pipette.distribute(50, keio.wells('D8'),  plate4.wells('C2', 'D2'))
pipette.distribute(50, keio.wells('D9'),  plate4.wells('C3', 'D3'))
pipette.distribute(50, keio.wells('D10'), plate4.wells('C4', 'D4'))
pipette.distribute(50, keio.wells('D11'), plate4.wells('C5', 'D5'))
pipette.distribute(50, keio.wells('D12'), plate4.wells('C6', 'D6'))

# fifth plate
pipette.distribute(50, keio.wells('E1'),  plate5.wells('A1', 'B1'))
pipette.distribute(50, keio.wells('E2'),  plate5.wells('A2', 'B2'))
pipette.distribute(50, keio.wells('E3'),  plate5.wells('A3', 'B3'))
pipette.distribute(50, keio.wells('E4'),  plate5.wells('A4', 'B4'))
pipette.distribute(50, keio.wells('E5'),  plate5.wells('A5', 'B5'))
pipette.distribute(50, keio.wells('E6'),  plate5.wells('A6', 'B6'))
pipette.distribute(50, keio.wells('E7'),  plate5.wells('C1', 'D1'))
pipette.distribute(50, keio.wells('E8'),  plate5.wells('C2', 'D2'))
pipette.distribute(50, keio.wells('E9'),  plate5.wells('C3', 'D3'))
pipette.distribute(50, keio.wells('E10'), plate5.wells('C4', 'D4'))
pipette.distribute(50, keio.wells('E11'), plate5.wells('C5', 'D5'))
pipette.distribute(50, keio.wells('E12'), plate5.wells('C6', 'D6'))

# sixth plate
pipette.distribute(50, keio.wells('F1'),  plate6.wells('A1', 'B1'))
pipette.distribute(50, keio.wells('F2'),  plate6.wells('A2', 'B2'))
pipette.distribute(50, keio.wells('F3'),  plate6.wells('A3', 'B3'))
pipette.distribute(50, keio.wells('F4'),  plate6.wells('A4', 'B4'))
pipette.distribute(50, keio.wells('F5'),  plate6.wells('A5', 'B5'))
pipette.distribute(50, keio.wells('F6'),  plate6.wells('A6', 'B6'))
pipette.distribute(50, keio.wells('F7'),  plate6.wells('C1', 'D1'))
pipette.distribute(50, keio.wells('F8'),  plate6.wells('C2', 'D2'))
pipette.distribute(50, keio.wells('F9'),  plate6.wells('C3', 'D3'))
pipette.distribute(50, keio.wells('F10'), plate6.wells('C4', 'D4'))
pipette.distribute(50, keio.wells('F11'), plate6.wells('C5', 'D5'))
pipette.distribute(50, keio.wells('F12'), plate6.wells('C6', 'D6'))

# seventh plate
pipette.distribute(50, keio.wells('G1'),  plate7.wells('A1', 'B1'))
pipette.distribute(50, keio.wells('G2'),  plate7.wells('A2', 'B2'))
pipette.distribute(50, keio.wells('G3'),  plate7.wells('A3', 'B3'))
pipette.distribute(50, keio.wells('G4'),  plate7.wells('A4', 'B4'))
pipette.distribute(50, keio.wells('G5'),  plate7.wells('A5', 'B5'))
pipette.distribute(50, keio.wells('G6'),  plate7.wells('A6', 'B6'))
pipette.distribute(50, keio.wells('G7'),  plate7.wells('C1', 'D1'))
pipette.distribute(50, keio.wells('G8'),  plate7.wells('C2', 'D2'))
pipette.distribute(50, keio.wells('G9'),  plate7.wells('C3', 'D3'))
pipette.distribute(50, keio.wells('G10'), plate7.wells('C4', 'D4'))
pipette.distribute(50, keio.wells('G11'), plate7.wells('C5', 'D5'))
pipette.distribute(50, keio.wells('G12'), plate7.wells('C6', 'D6'))

# eight plate
pipette.distribute(50, keio.wells('H1'),  plate8.wells('A1', 'B1'))
pipette.distribute(50, keio.wells('H2'),  plate8.wells('A2', 'B2'))
pipette.distribute(50, keio.wells('H3'),  plate8.wells('A3', 'B3'))
pipette.distribute(50, keio.wells('H4'),  plate8.wells('A4', 'B4'))
pipette.distribute(50, keio.wells('H5'),  plate8.wells('A5', 'B5'))
pipette.distribute(50, keio.wells('H6'),  plate8.wells('A6', 'B6'))
pipette.distribute(50, keio.wells('H7'),  plate8.wells('C1', 'D1'))
pipette.distribute(50, keio.wells('H8'),  plate8.wells('C2', 'D2'))
pipette.distribute(50, keio.wells('H9'),  plate8.wells('C3', 'D3'))
pipette.distribute(50, keio.wells('H10'), plate8.wells('C4', 'D4'))
pipette.distribute(50, keio.wells('H11'), plate8.wells('C5', 'D5'))
pipette.distribute(50, keio.wells('H12'), plate8.wells('C6', 'D6'))



