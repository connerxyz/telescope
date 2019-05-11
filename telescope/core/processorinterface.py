from abc import abstractmethod
import logging
log = logging.getLogger()


class ProcessorInterface:

    def __init__(self, name, aggregator=None):
        self.name = name  # TODO can type(self).__name__ be used?
        self.__aggregator = aggregator

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def aggregate(self, notebooks):
        if self.__aggregator is not None:
            self.__aggregator(notebooks)
        else:
            # Aggregators don't have to exist.
            # Some processors may exist to only transform individual notebooks
            # and have no purpose for aggregating those transformations.
            log.debug("No aggregator provided. Doing nothing.")
            pass
