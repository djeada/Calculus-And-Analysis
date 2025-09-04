#!/usr/bin/env python3
"""Small helper to execute a notebook (nbconvert) and save output."""
import sys
from nbconvert import NotebookExporter, HTMLExporter, exporters
from nbformat import read, write, NO_CONVERT
from nbclient import NotebookClient


def run_notebook(path):
    nb = read(open(path, 'r', encoding='utf-8'), as_version=4)
    client = NotebookClient(nb)
    client.execute()
    write(nb, open(path, 'w', encoding='utf-8'))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: run_notebook.py notebook.ipynb')
        sys.exit(2)
    run_notebook(sys.argv[1])
