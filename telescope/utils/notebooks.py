import json
import logging
import re
import nbformat
import glob

log = logging.getLogger()


def paths(directory):
    """Locate relevant .ipynb files in given directory"""
    pattern = directory + "/*.ipynb"
    log.debug(pattern)
    results = glob.glob(pattern)
    log.debug("{} notebook paths".format(len(results)))
    return results


def load(path):
    """
    Open and read the Jupyter notebook at the provided path.

    :param path: A filepath to the notebook.
    :type path: str
    :return: A dict-like object with notebook attribute access.
    :rtype: nbformat.NotebookNode
    """
    log.debug("Loading notebook at {}".format(path))
    with open(path) as f:
        # NO_CONVERT option
        # https://nbformat.readthedocs.io/en/latest/api.html
        notebook = nbformat.read(f, nbformat.NO_CONVERT)
    # Split the markdown cells' source attribute (see docstring)
    #
    # It's handy to be able to work with markdown cells' `source` attribute as
    # a list of strings. We do that here in the loading stage.
    #
    # This is necessary because...
    # "On disk, multi-line strings MAY be split into lists of strings.
    # When read with the nbformat Python API, these multi-line strings will
    # always be a single string."
    # See http://nbformat.readthedocs.io/en/latest/format_description.html#cell
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            cell['source'] = cell['source'].split("\n")
    return notebook


def fragmentid(text):
    """
    Create a normalized "fragment-identifier" URI from a string for intrapage
    linking.

    # TODO used to be called construct_anchor_name

    Example:
        "What is the distribution?" => 'what-is-the-distribution'

    :param text: Text to be transformed into normalized fragment-id.
    :type text: str
    :return: Normalized fragmentation-id for text argument
    :rtype: str
    """
    # TODO implement some uniqueness guarantee - possible name/link collisions
    result = text.lower()
    result = re.sub("[^a-z0-9\s\-]", "", result)
    result = result.strip()
    result = re.sub("[\s]+", "-", result)
    return result


def headinglevel(heading):
    """
    Determine the heading level (i.e. 1-6) of a given markdown heading.
    """
    result = 0
    while heading[result] == '#':
        result += 1
    return result


def dump(notebook, path: str) -> None:
    """
    Write notebook object to disk as JSON, i.e. .ipynb

    :param notebook: The notebook to write.
    :type notebook: telescope.Notebook
    :param path: Where to write notebook.
    :type path: str
    :return: None
    :rtype: None
    """
    with open(path, "w") as f:
        json.dump(notebook.node, f)
