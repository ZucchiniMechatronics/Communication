#RPi Pinouts

#I2C Pins 
#GPIO2 -> SDA
#GPIO3 -> SCL

#Import the Library Requreid 
import smbus
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
#bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
#Slave Address 1
#address = 0x04

# for RPI version 1, use "bus = smbus.SMBus(0)"	
bus = smbus.SMBus(1)

	# This is the address we setup in the Arduino Program
	#Slave Address 1
address = 0x04


def writeNumber(value):
    bus.write_byte(address, value)

    # bus.write_byte_data(address, 0, value)
    return -1

def readarduino():
	
    # number = bus.read_byte(address)
    number = bus.read_i2c_block_data(address,0,16)
    print("reading information from arduino")
    print(number)
    time.sleep(.01)
    return number
 
def listen():
	DEC=0
	while (DEC==0):
		dec=readarduino()
		print (dec[0])
		if dec[0]==49:
			DEC=dec
			print 'works'
		else: 
			print 'not yet'
		

def speakpi(data):

		#Receives the data from the User
		#data = raw_input("Enter the data to be sent : ")
	data_list = list(data)
	for i in data_list:
		#Sends to the Slaves 
		writeNumber(int(ord(i)))
		time.sleep(.1)
		writeNumber(int(0x0A))

	return 1
