import sys
from bencodepy import decode_from_file
from ParameterParser import ParameterParser
from os import getcwd


class btclient:
    def __init__(self, parameters):
        self.parameter_parser = ParameterParser(parameters)
        # self.torrent_file_dict = getcwd() + "/" + self.parameter_parser.get_torrent_file_path()
        self.torrent_file_dict = decode_from_file(self.parameter_parser.get_torrent_file_path())
        # print(self.torrent_file_dict)
        self.trackers = self.torrent_file_dict[b'announce-list']
        print(self.trackers)
        self.announced_tracker = self.torrent_file_dict[b'announce']
        print(self.announced_tracker)


if __name__ == "__main__":
    client = btclient(sys.argv[1:])
    pass

