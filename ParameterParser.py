
class ParameterParser:
    def __init__(self, parameters):
        self.raw_parameters = parameters
        self.progress_update_interval = 30
        self.verbose = False
        self.torrent_file_path = ""
        self.save_dir_path = ""
        self.parse()

    def parse(self):
        if len(self.raw_parameters) < 2:
            raise ValueError("Usage : python btclient.py [options] path/to/torrent/file path/to/save/dir")
            return
        for p in self.raw_parameters:
            if p[:2] == "-t":
                self.progress_update_interval = int(p[2:])
            elif p == "-v":
                self.verbose = True
        self.torrent_file_path = self.raw_parameters[-2]
        self.save_dir_path = self.raw_parameters[-1]

    def get_progress_update_interval(self):
        return self.progress_update_interval

    def get_torrent_file_path(self):
        return self.torrent_file_path

    def get_save_dir_path(self):
        return self.save_dir_path

