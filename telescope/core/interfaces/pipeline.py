from abc import abstractmethod
from ..notebook import Notebook
import logging

log = logging.getLogger()


class PipelineInterface:

    def __init__(self, pipeline):
        self.pipeline = pipeline

    @abstractmethod
    def fit(self, notebooks, *args, **kwargs):
        """
        Sequentially execute processors in the pipeline on the give notebooks

        :param notebooks: A list of paths to .ipynb files
        :type notebooks: list
        :return: None
        :rtype: None
        """
        for notebook in notebooks:
            notebook = Notebook(notebook)
            for processor in self.pipeline:
                log.debug("{} processor".format(processor.name))
                notebook = processor.transform(notebook)

    @abstractmethod
    def render(self):
        """
        Sequentially execute processors' rendering routines
        """
        pass
