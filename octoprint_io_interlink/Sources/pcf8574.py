from ast import Import
import time
try:
    import smbus
except ImportError:
    pass

from .InterlinkSource import InterlinkSource





class InterlinkPcf8574:

    @staticmethod
    def _set_bit(value, bit):
        return value | (1 << bit)

    @staticmethod
    def _clear_bit(value, bit):
        return value & ~(1 << bit)

    def __init__(self, settings, logger):
        self._settings = settings
        self._logger = logger
        self.bus = smbus(1)
        self.address = self._settings.settings.get(["driver_pcf8574_addr"])
        self._current_state = 0;
        self.bus.write_byte(self.address, self._current_state)

    def set_output(self, out_pin, level):
        if level:
            self._current_state = self._set_bit(self._current_state, out_pin)
        else:
            self._current_state = self._clear_bit(self._current_state, out_pin)

        self.bus.write_byte(self.address, self._current_state)

    def get_input(self, out_pin):
        current_state = self.bus.read_byte(self.address)
        return current_state & (1 << out_pin) == (1 << out_pin)

InterlinkSource.register(InterlinkPcf8574)


