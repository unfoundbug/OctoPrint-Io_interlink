import octoprint.plugin
import octoprint.events
import logging
from .Sources.pcf8574 import InterlinkPcf8574
from .Sources.debug import InterlinkDebug


class InterlinkControl:

    def __init__(self):
        self._settings = None
        self._logger = None
        self._active_driver = None

    def __on_connected(self):
        pass

    def __on_disconnected(self):
        pass

    def __on_print_start(self):
        pass

    def __on_print_end(self):
        pass

    def __on_user_login(self):
        pass

    def __on_user_logout(self):
        pass

    def setting_updated(self):
        driver = self._settings.get(['driver'])
        if self._active_driver is not None:
            self._logger.debug("Active driver, shutting down")
            self._active_driver.stop()
            self._active_driver = None
            self._logger.info("Stopped active driver.")

        if driver != 'none':
            self._logger.debug("Attempting to start new " + driver + " driver.")
            if driver == "pcf8574":
                self._active_driver = InterlinkPcf8574(self._settings, self._logger)
            elif driver == "debug":
                self._active_driver = InterlinkDebug(self._settings, self._logger)
            else:
                self._logger.warn("UNKNOWN DRIVER")

            self._logger.debug("Driver constructed")

        if driver != 'none':
            self._logger.info("Starting new driver.")
            self._active_driver.start()

    def start(self, settings_view_model, logger):
        self._settings = settings_view_model
        self._logger = logger

        self.setting_updated()

    def parse_event(self, event, params):
        if event == octoprint.events.Events.PRINT_STARTED:
            self.__on_print_start(params)
        elif event == octoprint.events.Events.PRINT_DONE:
            self.__on_print_end(params)
        elif event == octoprint.events.Events.USER_LOGGED_IN:
            self.__on_user_login(params)
        elif event == octoprint.events.Events.USER_LOGGED_IN:
            self.__on_user_logout(params)
        elif event == octoprint.events.Events.CONNECTED:
            self.__on_connected(params)
        elif event == octoprint.events.Events.DISCONNECTED:
            self.__on_disconnected(params)

    def driver_updated(self):
        self.start()
