from abc import ABC, abstractmethod

class Message(ABC):

    def __init__(self):
        pass

    @staticmethod
    def create_message(msg_config):
        return NotImplemented
    
