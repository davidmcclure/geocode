

from invoke import task
from polyglot.text import Text
from geopy.geocoders import Nominatim

import csv


@task
def geocode(in_path, out_path):

    """
    Extract entities from a text file.

    Args:
        in_path (str)
        out_path (str)
    """

    with open(in_path, 'r') as fh:
        text = Text(fh.read())

    entities = [e for e in text.entities if e.tag == 'I-LOC']

    geocoder = Nominatim()

    with open(out_path, 'w') as fh:

        cols = ['toponym', 'latitude', 'longitude']
        writer = csv.DictWriter(fh, cols)
        writer.writeheader()

        for e in entities:

            query = ' '.join(text.words[e.start:e.end])

            loc = geocoder.geocode(query)

            if loc:

                print(query, loc.latitude, loc.longitude)

                writer.writerow(dict(
                    toponym=query,
                    latitude=loc.latitude,
                    longitude=loc.longitude,
                ))
