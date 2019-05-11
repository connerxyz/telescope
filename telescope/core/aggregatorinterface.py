import logging

log = logging.getLogger()


class AggregatorInterface:

    def __init__(self, parent):
        self.name = type(self).__name__
        self.parent = parent

    def __call__(self, notebooks):
        """
        Aggregates a processor's results across all notebooks.
        """
        pass
