# Simple demo of of the LSM303 accelerometer & magnetometer library.
# Will print the accelerometer & magnetometer X, Y, Z axis values every half
# second.
# Author: Tony DiCola
# License: Public Domain
import time
import math

# Import the LSM303 module.
from libraries.Adafruit_LSM303 import LSM303

# Create a LSM303 instance.
lsm303 = LSM303()

# Alternatively you can specify the I2C bus with a bus parameter:
#lsm303 = Adafruit_LSM303.LSM303(busum=2)

print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_z, mag_y = mag
    pitch = math.atan(accel_x / math.sqrt(accel_y^2 + accel_z^2))
    roll = math.atan(accel_y / math.sqrt(accel_x^2 + accel_z^2))
    print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}, Pitch={6}, Roll={7}'.format(
          accel_x, accel_y, accel_z, mag_x, mag_y, mag_z, pitch, roll))
    # Wait half a second and repeat.
    time.sleep(0.5)
