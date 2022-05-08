from .InterlinkSource import InterlinkSource
import logging

class InterlinkDebug:
    def __init__(self, settings_view_model, logger):
        self._settings = settings_view_model
        self._logger = logger

    def get_out_count(self):
        return 0

    def get_in_count(self):
        return 0

    def set_output(self, out_pin, level):
        self._logger.info("IO Interlink Debug driver: Set Output " + str(out_pin) + " to " + str(level))

    def get_input(self, out_pin, level):
        self._logger.info("IO Interlink Debug driver: Get Input")
        return False

    def start(self):
        self._logger.info("IO Interlink Debug driver: Startup")
        pass

    def stop(self):
        self._logger.info("IO Interlink Debug driver: Shutdown")
        pass

InterlinkSource.register(InterlinkDebug)
