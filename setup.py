from setuptools import setup, find_packages

setup(
    name="telescope",
    version="0.0.1",
    description="Improving knowledge capture and discovery across Jupyter "
                "notebooks.",
    url="", # TODO
    author="Conner Cowling",
    author_email="connercarl@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    install_requires=[
        'nbformat',
        'nbconvert',
        'docopt',
        'mkdocs',
        'mkdocs-material',
        'mkdocs-gitbook'
    ]
)
