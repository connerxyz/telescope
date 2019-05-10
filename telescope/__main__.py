"""telescope

Usage: telescope [--navigation --highlights --render=<render_type>] <src> <dest>

Options:
    --render=<render_type>  How should results be rendered? [default: app].
    --navigation Add markdown cell with navigation links to top of notebooks?
    --highlights Add markdown cell with highlights to top of notebooks?
"""

import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from docopt import docopt
import telescope

if __name__ == "__main__":

    # Logging config
    STDOUT_LEVEL = logging.DEBUG
    FILE_LEVEL = logging.DEBUG
    FORMAT_STRING = '%(asctime)s %(levelname)s %(module)s %(funcName)s :: %(' \
                    'message)s '

    # Logging to file
    fh = TimedRotatingFileHandler("log.log", when="midnight", interval=1)
    fh.setLevel(FILE_LEVEL)
    fh.setFormatter(logging.Formatter(FORMAT_STRING))

    # Stdout/ipynb-output-cell
    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(STDOUT_LEVEL)
    sh.setFormatter(logging.Formatter(FORMAT_STRING))

    log = logging.getLogger()
    log.setLevel(STDOUT_LEVEL)
    log.addHandler(fh)
    log.addHandler(sh)

    # CLI implementation
    args = docopt(__doc__)
    log.debug(args)

    # DETERMINE PROCESSORS

    # Which processors and in what order
    # processors = []
    #
    # optional_processors = {
    #     args['--navigation']: telescope.NavigationProcessor(),
    #     args['--highlights']: telescope.HighlightsProcessor(),
    # }
    #
    # for k, v in optional_processors:
    #     if k:
    #         processors.append(v)
    #
    # # Assume user always wants QA pair extraction and rendering
    # processors.append(telescope.QAPairProcessor())

    # TODO just develop the nav processor for now.
    processors = [
        telescope.NavigationProcessor()
    ]

    # ASSEMBLE PIPELINE
    pipeline = telescope.Pipeline(processors)

    # IDENTIFY NOTEBOOKS TO PROCESS
    notebooks = telescope.notebooks.paths(args['<src>'])

    # EXECUTE PIPELINE
    pipeline.transform(notebooks)

    # RENDER
    pipeline.render()

    # ALTERNATIVELY YOU CAN CHAIN
    # pipeline.transform(notebooks).render()

    # # RENDER
    #
    # pipeline.render(
    #     render=args['--render'],
    #     dest=args['--dest']
    # )

    # ALTERNATIVE TO ABOVE...
    # pipeline = telescope.Pipeline(
    #     processors,
    #     notebooks
    # )
    # pipeline.render()
