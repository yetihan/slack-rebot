from abc import ABC, abstractmethod

class IM(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def send_msg(self):
        return NotImplemented

    @abstractmethod
    def get_msg(self):
        return NotImplemented
    
