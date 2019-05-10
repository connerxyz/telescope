from abc import abstractmethod
import logging
log = logging.getLogger()


class ProcessorInterface:

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def render(self):
        pass
