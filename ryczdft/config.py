
import argparse
import yaml
import pprint
from ase.io import read, write

class Config:
    """
    Class to handle YAML input and command line args.
    """
    def __init__(self):
        self.config = {
            'xc': 'pbe',
            'ions': 'coords.xsf',
            'grid': None,
            'dim': 3,
        }
        
        # variables that depend on other variables
        self.config['periodic'] = [True] * self.config['dim']
        
        self.init()
        self.printConfig()

    def init(self):
        self.args = self.parseArgs()
        self.this_config = self.parseConfig()
        self.config.update(this_config)

    def parseArgs(self):
        parser = argparse.ArgumentParser(description='ryczdft - A density functional theory package for Pythonic physicists. Allows for 1-3 dimensional systems, algorithm and data transparency. Get your hands dirty.')
        parser.add_argument('-in', '--infile', help='Name of configuration file.', dest='infile', default='input.yaml')

        return parser.parse_args()

    def parseConfig(self):
        return yaml.safe_load(open(self.args.infile, 'r'))


    def printConfig(self):
        """
        Print out the configuration.
        """
        pp = pprint.PrettyPrinter(indent=4)
        print()
        print('Here is your configuration:')
        pp.pprint(self.config)
        print()