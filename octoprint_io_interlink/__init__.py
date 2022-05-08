# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
from interlinkcontroller import InterlinkControl

class Io_interlinkPlugin(octoprint.plugin.SettingsPlugin,
    octoprint.plugin.AssetPlugin,
    octoprint.plugin.TemplatePlugin
):

    def __init__(self):
        self.io_controller = InterlinkControl(octoprint.plugin.SettingsPlugin, self._logger)

    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return dict(
            driver="None",
            pin_hook_user_logged_in="None",
            pin_state_user_logged_in="High",
            pin_hook_printer_connected="None",
            pin_state_printer_connected="High",
            pin_hook_printing="None",
            pin_state_printing="High",
            driver_pcf8574_addr="0x21",
        )

    def on_settings_save (self, data):
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
        self.io_controller.setting_updated()

    ##~~ TemplatePlugin mixin

    def get_template_vars(self):
        return dict(
            driver=self._settings.get(["driver"]),
            pin_hook_user_logged_in=self._settings.get(["pin_hook_user_logged_in"]),
            pin_state_user_logged_in=self._settings.get(["pin_state_user_logged_in"]),
            pin_hook_printer_connected=self._settings.get(["pin_hook_printer_connected"]),
            pin_state_printer_connected=self._settings.get(["pin_state_printer_connected"]),
            pin_hook_printing=self._settings.get(["pin_hook_printing"]),
            pin_state_printing=self._settings.get(["pin_state_printing"]),
            driver_pcf8574_addr=self._settings.get(["driver_pcf8574_addr"]),
        )

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False)
        ]

    def on_event(self, event, payload):
        self.io_controller.parse_event(event, payload)

    ##~~ StartupPlugin mixin

    def on_after_startup(self):
        self._logger.info("IO Interlink Initialising.")
        self.io_controller.start()

    ##~~ AssetPlugin mixin

    def get_assets(self):
        # Define your plugin's asset files to automatically include in the
        # core UI here.
        return {
            "js": ["js/settings.js"],
        }

    ##~~ Software Update hook

    def get_update_information(self):
        # Define the configuration for your plugin to use with the Software Update
        # Plugin here. See https://docs.octoprint.org/en/master/bundledplugins/softwareupdate.html
        # for details.
        return dict(
            calibrationtests=dict(
            displayName="Io_interlink Plugin",
            displayVersion=self._plugin_version,

            # version check: GitHub repository
            type="github_release",
            user="UnFoundBug",
            repo="OctoPrint-Io_interlink",
            current=self._plugin_version,

            # update method: pip
            pip="https://github.com/unfoundbug/OctoPrint-Io_interlink/archive/{target_version}.zip"
            )
        )


# Set the Python version your plugin is compatible with below. Recommended is Python 3 only for all new plugins.
# OctoPrint 1.4.0 - 1.7.x run under both Python 3 and the end-of-life Python 2.
# OctoPrint 1.8.0 onwards only supports Python 3.
__plugin_pythoncompat__ = ">=3,<4"  # Only Python 3

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = Io_interlinkPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
