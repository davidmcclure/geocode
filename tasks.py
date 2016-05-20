

from invoke import task
from polyglot.text import Text

import csv


@task
def test(in_path, out_path):

    """
    Extract entities from a text file.

    Args:
        in_path (str)
        out_path (str)
    """

    with open(in_path, 'r') as fh:

        text = Text(fh.read())

        entities = [e for e in text.entities if e.tag == 'I-LOC']

        with open(out_path, 'w') as fh:
            for e in entities:
                print(' '.join(text.words[e.start:e.end]), file=fh)
