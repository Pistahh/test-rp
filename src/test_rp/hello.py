import logging

from test_rp._version import version


def hello():
    logging.warn(f"Hello, world {version=}")
