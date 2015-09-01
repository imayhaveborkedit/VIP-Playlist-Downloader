import requests
from utils import getPrettyFileSizes

class Song(object):

    def __init__(self, creator, title, location, getfsizes=False, verbose=False):
        self.verbose = verbose

        self.creator = creator
        self.title = title
        self.location = location

        self.filename = creator + ' - ' + title + '.m4a'
        self.raw_filename = self.filename
        self.vlog("Creating filename: %s ->\n %s" % (self.location, self.filename))

        self.filename = self.filename.replace('"',"'")
        self.filename = ''.join([c for c in self.filename if c not in '\/:*?<>|'])
        self.vlog("Sanitizing filename: %s ->\n %s\n" % (self.raw_filename, self.filename))

        self._filesize = None
        self._human_filesize = None

        if getfsizes:
            self._filesize = self.filesize
            self._human_filesize = self.human_filesize


    @property
    def filesize(self):
        if not self._filesize:
            self._filesize = int(requests.head(self.location).headers['content-length'])
            self.vlog("Got filesize for '%s': %s" % (self.filename, self._filesize))

        return self._filesize

    @property
    def human_filesize(self):
        if not self._human_filesize:
            self._human_filesize = str(getPrettyFileSizes(self.filesize, 'MB')) + ' MB'
            self.vlog("Got human filesize for '%s': %s" % (self.filename, self._human_filesize))

        return self._human_filesize

    @property
    def data(self):
        r = requests.get(self.location)
        self._filesize = int(r.headers['content-length'])
        self._human_filesize = str(getPrettyFileSizes(self._filesize, 'MB')) + ' MB'

        return r.content

    def vlog(self, text):
        if self.verbose:
            print text

    def download_to(self, location):
        pass
