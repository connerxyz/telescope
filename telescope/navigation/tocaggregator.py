from ..core import AggregatorInterface
import markdown
import logging

log = logging.getLogger()


class TableOfContentsAggregator(AggregatorInterface):

    # TODO Inherit from aggregator

    def __init__(self, parent):
        self.name = type(self).__name__
        self.parent = parent

    def __call__(self, notebooks):
        """
        Aggregates the navigation section for a collection of notebooks as a
        HTML rendered Jupyter notebook.

        :return:
        :rtype:
        """
        log.debug("executing aggregate rendering.")
        # Consolidate results across notebooks
        result = "# Table of Contents\n\n"
        for notebook in notebooks:
            result += "## {}\n\n{}\n".format(
                notebook.source_path,
                "".join(notebook.get_processor_result(self.parent))
            )
        # TODO establish dest
        # TODO ensure TOC links work
        # Write the results to HTML
        path = "./table-of-contents.html"
        with open(path, "w") as f:
            f.write(markdown.markdown(result))
            log.debug("Aggregated results written to {}".format(path))
