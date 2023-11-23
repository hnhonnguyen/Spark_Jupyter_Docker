#!/bin/bash
export PATH="/.local/bin:$PATH"
pip install jupyterlab
jupyter lab --allow-root --ip 0.0.0.0 --port 8888