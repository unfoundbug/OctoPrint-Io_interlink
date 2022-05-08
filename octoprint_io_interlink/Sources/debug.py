from InterlinkSource import InterlinkSource


class InterlinkDebug:
    def __init__(self):
        pass

    def get_out_count(self):
        pass

    def get_in_count(self):
        pass

    def set_output(self, out_pin, level):
        pass

    def get_input(self, out_pin, level):
        pass

InterlinkSource.register(Interlink_Debug)
