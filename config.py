
import argparse
from ase.io import read, write

class Config:
    """
    Class to handle YAML input and command line args.
    """
    def __init__(self):
        self.init()

    def init(self):
        self.parser = self.parseArgs()

    def parseArgs(self):
        parser = argparse.ArgumentParser(description='ryczdft - A python density functional theory package for Pythonic physicists. Allows for 1-3 dimensional systems, algorithm and data transparency. Get your hands dirty.')
        parser.add_argument('-in', '--infile', help='Name of configuration file.', dest='infile', default='input.yaml')

        return parser.parse_args()