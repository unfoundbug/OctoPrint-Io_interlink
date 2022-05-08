from ast import Import
import time
try:
    import smbus
except ImportError:
    pass

from InterlinkSource import InterlinkSource


def set_bit(value, bit):
    return value | (1 << bit)


def clear_bit(value, bit):
    return value & ~(1 << bit)


class InterlinkPcf8574:
    def __init__(self, bus, address, initial_state):
        self.bus = bus
        self.address = address

        bus.write_byte(address, initial_state)
        self.current_state = initial_state

    def set_output(self, out_pin, level):
        if level:
            self.current_state = set_bit(self.current_state, out_pin)
        else:
            self.current_state = clear_bit(self.current_state, out_pin)

        self.bus.write_byte(self.address, self.current_state)

    def get_input(self, out_pin):
        current_state = self.bus.read_byte(self.address)
        return current_state & (1 << out_pin) == (1 << out_pin)

InterlinkSource.register(InterlinkPcf8574)


