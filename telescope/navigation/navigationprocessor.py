from ..core.interfaces import ProcessorInterface
from ..utils import notebooks
from .utils import *
from copy import deepcopy
import logging

log = logging.getLogger()


class NavigationProcessor(ProcessorInterface):

    def __init__(self, name="navigation"):
        super().__init__(name)

    def transform(self, notebook, *args, **kwargs):
        """
        Apply this processor's transformation to given notebook.

        # TODO implement limited heading depth

        :param notebook: The notebook to apply transformation to
        :type notebook: telescope.Notebook
        :return: A transformed notebook
        :rtype: telescope.Notebook
        """
        navsection = [
            '<a name="top"></a>\n',  # Allows generation of "back to top" links
            '## Navigation\n',  # Beginning of navigation section
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
                cell['source'] = "\n".join(scp)
        notebook.transformations[self.name] = navsection
        log.debug(navsection)
        return notebook
