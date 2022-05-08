$(function() {
    function IoInterlinkSettingsViewModel(parameters) {
        var self = this;
		
		self.settingsViewModel = parameters[0];


        self.availableDrivers = ko.observableArray([{
                name : 'None',
                value : 'none'
            }, {
                name : 'PCF8574',
                value : 'pcf8574'
            }, {
                name : 'Debug',
                value : 'debug'
            }
        ]);

        self.hook_pins = ko.observableArray([{
                name : 'None',
                value : 'none'
            }, {
                name : '0',
                value : '0'
            }, {
                name : '1',
                value : '1'
            }, {
                name : '2',
                value : '2'
            }, {
                name : '3',
                value : '3'
            }
            , {
                name : '4',
                value : '4'
            }
            , {
                name : '5',
                value : '5'
            }
            , {
                name : '6',
                value : '6'
            }
            , {
                name : '7',
                value : '7'
            }
        ]);

        self.hook_mode = ko.observableArray([{
            name : 'High',
            value : 'high'
        }, {
            name : 'Low',
            value : 'low'
        }
        ]);
        // This will get called before the HelloWorldViewModel gets bound to the DOM, but after its
        // dependencies have already been initialized. It is especially guaranteed that this method
        // gets called _after_ the settings have been retrieved from the OctoPrint backend and thus
        // the SettingsViewModel been properly populated.
        self.onBeforeBinding  = function() {
        }
    };

    // This is how our plugin registers itself with the application, by adding some configuration
    // information to the global variable OCTOPRINT_VIEWMODELS
    OCTOPRINT_VIEWMODELS.push({
        // This is the constructor to call for instantiating the plugin
        construct: IoInterlinkSettingsViewModel,

        // This is a list of dependencies to inject into the plugin, the order which you request
        // here is the order in which the dependencies will be injected into your view model upon
        // instantiation via the parameters argument
        dependencies: ["settingsViewModel"],

        // Finally, this is the list of selectors for all elements we want this view model to be bound to.
        elements: ["#settings_plugin_io_interlink_form"]
});
});