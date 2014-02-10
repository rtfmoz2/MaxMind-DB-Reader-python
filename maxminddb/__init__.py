# pylint:disable=C0111

try:
    from maxminddb.extension import Reader, InvalidDatabaseError
except ImportError:
    from maxminddb.decoder import InvalidDatabaseError
    from maxminddb.reader import Reader


__title__ = 'maxminddb'
__version__ = '0.3.0'
__author__ = 'Gregory Oschwald'
__license__ = 'LGPLv2.1+'
__copyright__ = 'Copyright 2014 Maxmind, Inc.'
