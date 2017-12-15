import sys
from bencodepy import decode_from_file
from ParameterParser import ParameterParser
from InfoDictParser import InfoDictParser
import requests
import hashlib
from os import urandom
from bencodepy import encode


class btclient:
    def __init__(self, parameters):
        self.parameter_parser = ParameterParser(parameters)
        # self.torrent_file_dict = getcwd() + "/" + self.parameter_parser.get_torrent_file_path()
        self.torrent_file_dict = decode_from_file(self.parameter_parser.get_torrent_file_path())
        self.tracker = ""
        self.backup_trackers = []
        if b'announce-list' in self.torrent_file_dict:
            self.backup_trackers = self.torrent_file_dict[b'announce-list']
        self.tracker = self.torrent_file_dict[b'announce']
        # print(self.torrent_file_dict[b'info'])
        self.info_parser = InfoDictParser(self.torrent_file_dict[b'info'])
        if self.info_parser.is_single_file_info():
            self.total_size = self.info_parser.get_file_size()
            print(self.info_parser.get_single_file_info()[b'name'])
            print(self.tracker.decode())
        self.register_with_tracker()

    def register_with_tracker(self):
        request_parameters = {'info_hash': self.get_hash(encode(self.info_parser.torrent_info)), "peer_id": urandom(20),
                              "port": 2000, "uploaded": 0, "downloaded": 0, "left": self.total_size, "event": "started"}
        requests.get(self.tracker.decode(), request_parameters)

    def get_hash(self, bytes_info):
        m = hashlib.sha1()
        m.update(bytes_info)
        return m.digest()


if __name__ == "__main__":
    client = btclient(sys.argv[1:])
    pass

