from .interfaces.pipeline import PipelineInterface


class Pipeline(PipelineInterface):

    def transform(self, notebooks, *args, **kwargs):
        super().transform(notebooks, *args, **kwargs)

    def render(self):
        """
        Sequentially execute processors' rendering routines
        """
        pass
