# eeprom-pi-communicator
i2c communicator between raspberry pi and i2c eeprom. 

Setup:
  - SDL and SDA connected to respective pins on pi, tied to ground through 10k resistors
  - 3.3v pin on pi to VCC
  - GND pin on pi to VSS

Tested on:
  - 1k i2c serial eeprom
  - raspberry pi 3B+

System Requirements:
  - Raspberry pi
  - i2c tools installed
  
System specific code changes:
  - change address to the address of the i2c eeprom chip
  - length of block output depending on size of eeprom or preference * note: larger eeproms have not been tested
  
EEPROM switching:
  - switching is achieved through pin 17 on pi connecting to VCC on one eeprom and the input to an inverter circuit
  - output of inverter circuit connected to VCC of second eeprom
  - scl of both chips tied together
  - sda of both chips tied together
