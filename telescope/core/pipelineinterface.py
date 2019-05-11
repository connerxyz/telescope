from abc import abstractmethod
from telescope.core.notebook import Notebook
import logging

log = logging.getLogger()


class PipelineInterface:

    def __init__(self, pipeline, notebooks=None):
        if notebooks is None:
            notebooks = []
        self.pipeline = pipeline
        self.__notebooks = notebooks

    @property
    def notebooks(self):
        if not self.__notebooks:
            raise ValueError("You haven't provided notebooks to this pipeline.")
        else:
            return self.__notebooks

    @notebooks.setter
    def notebooks(self, notebooks):
        self.__notebooks = notebooks

    @abstractmethod
    def transform(self, notebooks, *args, **kwargs):
        """
        Sequentially execute processors in the pipeline on notebooks.

        :param notebooks: A list of paths to .ipynb files
        :type notebooks: list
        :return: None
        :rtype: None
        """
        # Get telescope.Notebook instances from each filepath
        self.notebooks = [Notebook(nb) for nb in notebooks]
        log.debug(self.notebooks)
        # Apply the processor to each Notebook instance
        for notebook in self.notebooks:
            for processor in self.pipeline:
                log.debug("{} processor".format(processor.name))
                notebook = processor.transform(notebook)
        # Return self to facilitate method chaining
        return self

    @abstractmethod
    def render(self):
        """
        Sequentially execute processors' rendering routines
        """
        # Employ each processor to render each notebook
        for processor in self.pipeline:
            for notebook in self.notebooks:
                log.debug("applying {} processor to {}".format(
                    processor.name,
                    notebook.source_path
                ))
                processor.render(notebook)
        # Employ the processor's aggregate renderer
        for processor in self.pipeline:
            log.debug("applying aggregator")
            processor.aggregate(self.notebooks)

