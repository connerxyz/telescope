from ..core import ProcessorInterface
from ..core import Notebook
from ..utils import notebooks
from .utils import *
from copy import deepcopy
from typing import Any
import logging

log = logging.getLogger()


class NavigationProcessor(ProcessorInterface):

    NAVTAG = "<telescope-nav></telescope-nav>"

    def __init__(self, name="navigation"):
        super().__init__(name)

    def transform(self, notebook: Notebook, *args, **kwargs) -> Notebook:
        """
        Generate navigation section for given notebook.
        # TODO implement limited heading depth
        """
        navsection = [
            self.NAVTAG, # Allows for detecting preexisting nav section
            '<a name="top">*Back to top*</a>\n',
            '## Navigation\n',
            '\n'
        ]
        for cell in notebook.node['cells']:
            # Look for markdown cells
            if cell['cell_type'] == 'markdown':
                # Copying the source avoids issues like infinite loops...
                scp = deepcopy(cell['source'])
                # ...However we still want to iterate over the original source
                for i, line in enumerate(cell['source']):
                    # Look for headings in markdown cells
                    if line.startswith("#"):
                        hlevel = notebooks.headinglevel(line)
                        fragid = notebooks.fragmentid(line)
                        # Map heading into navsection
                        navsection.append(navlink(hlevel, line, fragid))
                        # Insert anchor just before current line in source copy
                        scp.insert(i, anchorlink(fragid))
                # Overwrite the cell's source with the transformed source
                # TODO can/should transform have no side-effects on notebooks?
                # i.e. it would be cleaner if all changes to notebooks occurred
                # in render, and transform could guarantee no side-effects.
                cell['source'] = "\n".join(scp)
        notebook.set_processor_results(self, navsection)
        log.debug(navsection)
        return notebook

    def render(self, notebook: Notebook) -> Any:
        """
        Insert navigation section into notebook
        """
        # Create markdown cell for navigation section
        nav_cell = {
            "cell_type": "markdown",
            "metadata": {},
            "source": notebook.get_processor_results(self)
        }
        # Insert navigation section into notebook as first markdown cell
        # TODO implement more sophisticated handling of where to insert nav
        # e.g. detect and put after title/intro
        # e.g. detect existing navigation cell and overwrite it (upstream?)
        notebook.node['cells'].insert(0, nav_cell)
        log.warning("Overwriting notebook {}".format(notebook.source_path))
        notebooks.dump(notebook, notebook.source_path)
