
class InfoDictParser:
    def __init__(self, info):
        self.SINGLE_FILE = 0
        self.MULTIPLE_FILES = 1
        self.info_type = self.SINGLE_FILE
        self.torrent_info = info
        if b"files" in self.torrent_info:
            self.info_type = self.MULTIPLE_FILES

    def is_single_file_info(self):
        return self.info_type == self.SINGLE_FILE

    def get_single_file_info(self):
        return self.torrent_info
        pass

    def get_file_list(self):
        return self.torrent_info[b"files"]

    def get_top_dir_name(self):
        return self.torrent_info[b"name"]

    def get_piece_length(self):
        return self.torrent_info[b"piece length"]

    def get_pieces(self):
        return self.torrent_info[b"pieces"]

    def get_file_size(self):
        if self.info_type == self.SINGLE_FILE:
            return self.torrent_info[b'length']
