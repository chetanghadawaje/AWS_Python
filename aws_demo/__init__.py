import os

from six.moves import configparser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = configparser.SafeConfigParser(allow_no_value=True)

try:
    with open(os.path.join(BASE_DIR, 'local.cfg')) as configfile:
        config.read_file(configfile)
except Exception as e:
    print(e)
