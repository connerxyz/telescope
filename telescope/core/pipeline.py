from .pipelineinterface import PipelineInterface
import logging

log = logging.getLogger()


class Pipeline(PipelineInterface):

    def transform(self, notebooks, *args, **kwargs):
        super().transform(notebooks, *args, **kwargs)

    def render(self):
        super().render()
