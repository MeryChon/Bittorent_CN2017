
class ParameterParser:
    def __init__(self, parameters):
        self.raw_parameters = parameters
        self.progress_update_interval = 0
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
        # print(self.progress_update_interval)
        # print(self.verbose)
        # print(self.torrent_file_path)
        # print(self.save_dir_path)

