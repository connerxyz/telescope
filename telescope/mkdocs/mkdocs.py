class MkDocsConfig:

    # TODO use an native python object + yml lib?
    BOILERPLATE = (
        "site_name: '{site_name}'\n"
        "theme: '{theme}'\n"
        # "theme_dir: 'theme'\n"
        "extra_css: [extra.css]\n"
        "extra_javascript: [extra.js]\n"
        "nav:\n"
        "  - '': 'index.md'\n"
    )

    def render(self) -> str:
        """
        Produce a string of
        """
        # TODO
        return ""

    def write(self) -> None:
        """
        Write mkdocs config to mkdocs.yml
        """
        # TODO
        pass
