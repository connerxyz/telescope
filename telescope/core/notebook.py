import logging
from ..utils import notebooks

log = logging.getLogger()


class Notebook(object):
    """
    For parsing individual Jupyter Notebooks
    """

    def __init__(self, path):
        self.source_path = path
        self.node = notebooks.load(path)
        self.transformations = {}
