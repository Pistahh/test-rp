import logging

from test_rp.version import __version__ as version


def hello():
    logging.warn(f"Hi, world {version=}")
