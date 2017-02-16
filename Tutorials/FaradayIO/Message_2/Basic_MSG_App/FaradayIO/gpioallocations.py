"""
This module contains GPIO bitmask allocation definitions for use with the GPIO update commands.
"""
#Port 3
GPS_RESET = 0b00001000
GPS_STANDBY = 0b00010000
LED_1 = 0b01000000
LED_2 = 0b10000000

#Port 4
DIGITAL_IO_0 = 0b10000000
DIGITAL_IO_1 = 0b01000000
DIGITAL_IO_2 = 0b00100000
DIGITAL_IO_3 = 0b00010000
DIGITAL_IO_4 = 0b00001000
DIGITAL_IO_5 = 0b00000100
DIGITAL_IO_6 = 0b00000010
DIGITAL_IO_7 = 0b00000001

#Port 5
DIGITAL_IO_8 = 0b00000100
DIGITAL_IO_9 = 0b00001000
MOSFET_CNTL =  0b00010000
