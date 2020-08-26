import smbus
import RPi.GPIO as gp

gp.setwarnings(False)
gp.setmode(gp.BCM)
gp.setup(17, gp.OUT)

i = input('Chip select:  1 or 2: ')

mode = True
if int(i) == 1:
    mode = True
else:
    mode = False

gp.output(17, mode)


BUS = 1
ADDRESS = 0x50

bus = smbus.SMBus(BUS)

def rd():
    addr = 0x00
    block = []
    for i in range((128)):
        
        block.append(bus.read_byte_data(ADDRESS, addr + i))

    print(block)

def wr(addr, val):
    bus.write_byte_data(ADDRESS, addr, val)

def change(i):
    mode = True
    if int(i) == 1:
        mode = True
    else:
        mode = False

    gp.output(17, mode)



    
    
    




##def write(ADDRESS, data):
##    bus.write_word_data(ADDRESS, 0x00, new_config)
##
##config = bus.read_i2c_block_data(ADDRESS, 0x00)
##
##print('Value : 0x' + format(config))
##
##new_config = 0b000000011
##
##write(0x50, new_config)
