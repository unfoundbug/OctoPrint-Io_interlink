from ast import Import
import time
try:
    import smbus
except ImportError:
    pass

from InterlinkSource import InterlinkSource

class Interlink_Pcf8574:
    def ___init___(self, bus, address, initialstate):
        self.bus = bus
        self.address = address

        bus.write_byte(address,initialstate)
        self.current_state = initialstate

    def get_out_count(self):
        return 8

    def get_in_count(self):
        return 0

    def set_output(self, out_pin, level):
        if self.current_state&(1<<out_pin) != 0:
            self.current_state = self.current_state|(1<<out_pin)
        else:
            self.current_state = self.current_state^(1<<out_pin)
        self.bus.write_byte(self.address,self.current_state)

    def get_input(self, out_pin, level):
        return self.bus.read_byte(self.address)


InterlinkSource.register(Interlink_Pcf8574)


