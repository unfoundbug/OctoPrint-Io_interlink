import smbus
import time

address = 0x21

bus = smbus.SMBus(1)

start_value = bus.read_byte(address)
bus.write_byte(address,0x00)
after_first_set = bus.read_byte(address)
time.sleep(0.5)
after_first_sleep = bus.read_byte(address)
bus.write_byte(address,0x10)
after_second_set = bus.read_byte(address)
time.sleep(0.5)
after_second_sleep = bus.read_byte(address)

print("i2c Test complete. Results: " + str(start_value) + " " + str(after_first_set) + " " + str(after_second_set))