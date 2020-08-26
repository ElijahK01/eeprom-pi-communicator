import smbus
import RPi.GPIO as gp

gp.setwarnings(False)
gp.setmode(gp.BCM)
gp.setup(17, gp.OUT) # comment out for single chip

i = input('Chip select:  1 or 2: ') # comment out for single chip

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
