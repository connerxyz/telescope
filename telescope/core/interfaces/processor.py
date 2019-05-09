from abc import abstractmethod
import logging

log = logging.getLogger()


class ProcessorInterface:

    def __init__(self, name):
        self.name = name
