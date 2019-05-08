#!/usr/bin/env bash
conda env export > environment.yml
conda list -e > requirements.txt
