from abc import ABC, abstractmethod

class InterlinkSource(ABC):
    @abstractmethod
    def get_out_count(self):
        pass

    @abstractmethod
    def get_in_count(self):
        pass

    @abstractmethod
    def set_output(self, out_pin, level):
        pass

    @abstractmethod
    def get_input(self, out_pin, level):
        pass
