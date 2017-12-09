import sys
import bencodepy
from ParameterParser import ParameterParser


class btclient:
    def __init__(self, parameters):
        self.parameter_parser = ParameterParser(parameters)



if __name__ == "__main__":
    client = btclient(sys.argv[1:])
    pass

