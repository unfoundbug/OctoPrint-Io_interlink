import octoprint.plugin
import octoprint.events

from Sources.pcf8574 import InterlinkPcf8574
from Sources.debug import InterlinkDebug

class InterlinkControl:

    def __init__(self, settings_view_model, logger):
        self._settings = settings_view_model
        self._logger = logger

    def start(self):
        driver = self._settings.get_string('driver')
        if self.active_driver is not None:
            self.active_driver.stop()
            self.active_driver = None

        if driver != 'none':
            if driver == "pcf8574":
                self.active_driver = InterlinkPcf8574()
            elif driver == "debug":
                self.active_driver = InterlinkDebug()

        pass

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

    def setting_updated(self):
        pass

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
