import re
import logging
import errno
import os
import shutil
import glob

log = logging.getLogger()


def get_paths(directory):
    paths = glob.glob(directory + "/*.ipynb")
    return paths


def mkdir(path):
    """Handles creating directory used for output results. Also eliminates
    old results if necessary.

    # TODO used to be called make_results_dir

    Args:
        path (str): The path of the output results directory
    Returns:
        None
    """
    if os.path.isdir(path):
        log.debug("{} already exists. Removing contents.".format(path))
        shutil.rmtree(path)
    try:
        log.debug("Creating {}".format(path))
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
        else:
            log.error("Results directory already exists. This should never "
                      "happen. It should have been removed.")
            raise
    else:
        log.debug("{} results directory created.".format(path))


def get_git_commit_hash():
    """Check for .git and the current commit hash."""
    # TODO
    pass
