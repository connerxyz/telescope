"""telescope

Usage: telescope [--render=<render_type>] <dir>

Options:
    --render=<render_type>  What format telescope compiles results to [default: app].

"""

import sys
import logging
from docopt import docopt

if __name__ == "__main__":

    # Logging config
    args = docopt(__doc__)
    print(args)
    # Setup logging
    STDOUT_LEVEL = logging.DEBUG
    FILE_LEVEL = logging.DEBUG
    FORMAT_STRING = '%(asctime)s %(levelname)s %(module)s %(funcName)s :: %(message)s'

    # Logging to file
    fh = logging.FileHandler(args['<dir>'] + "log.log")
    fh.setLevel(FILE_LEVEL)
    fh.setFormatter(logging.Formatter(FORMAT_STRING))

    # Stdout/ipynb-output-cell
    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(STDOUT_LEVEL)
    sh.setFormatter(logging.Formatter(FORMAT_STRING))

    log = logging.getLogger()
    log.setLevel(logging.NOTSET)
    log.addHandler(fh)
    log.addHandler(sh)
    print(args)

    # CLI implementation
	# TODO
