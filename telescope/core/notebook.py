import logging
from ..utils import notebooks
from .processorinterface import ProcessorInterface
from typing import Any


log = logging.getLogger()


class Notebook(object):
    """
    For parsing individual Jupyter Notebooks
    """

    def __init__(self, path):
        self.source_path = path
        self.node = notebooks.load(path)
        self.__processor_results = {}

    def set_processor_results(self, processor: ProcessorInterface, results) -> None:
        """
        Embed the given processor's results within this notebook instance
        """
        self.__processor_results[processor.name] = results

    def get_processor_results(self, processor: ProcessorInterface) -> Any:
        """
        Extract the given processor's results from this notebook instance
        """
        return self.__processor_results[processor.name]
