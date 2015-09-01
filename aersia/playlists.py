import xml.etree.ElementTree as ET
import sys, os, os.path, requests, urllib2, struct, argparse, re


_playlist_data = {
    'normal': {
        'roster': 'http://vip.aersia.net/roster.xml',
        'changelog': 'http://vip.aersia.net/changelog.txt',
        'swf': 'http://vip.aersia.net/vip.swf',
        'offsets': (4, -1)
    },
    'source': {
        'roster': 'http://vip.aersia.net/roster-source.xml',
        'changelog': 'http://vip.aersia.net/changelog.txt',
        'swf': 'http://vip.aersia.net/vip-source.swf',
        'offsets': (4, -1)
    },
    'mellow': {
        'roster': 'http://vip.aersia.net/roster-mellow.xml',
        'changelog': 'http://vip.aersia.net/changelog-mellow.txt',
        'swf': 'http://vip.aersia.net/vip-mellow.swf',
        'offsets': (3, -2)
    },
    'exiled': {
        'roster': 'http://vip.aersia.net/roster-exiled.xml',
        'changelog': None,
        'swf': 'http://vip.aersia.net/vip-exiled.swf',
        'offsets': (1, None),
    },
    'anime': {
        'roster': 'http://wap.aersia.net/roster.xml',
        'changelog': 'http://wap.aersia.net/changelog.txt',
        'swf': 'http://wap.aersia.net/wap.swf',
        'offsets': (3, None)
    },
    'couchpotato': {
        'roster': 'http://cpp.aersia.net/roster.xml',
        'changelog': 'http://cpp.aersia.net/changelog.txt',
        'swf': 'http://cpp.aersia.net/cpp.swf',
        'offsets': (1, None)
    }
}


def blah():
    xmlroster = _playlist_data['normal']['roster']
    rosteroffsets = _playlist_data['normal']['offsets']

    roster = requests.get(xmlroster)
    treeroot = ET.fromstring(roster.text.replace('xmlns="http://xspf.org/ns/0/"',''))

    print treeroot.getchildren()[0][0].find('title').text
    print # "X Tracks (Last Update: M DD YY)" or something like that

    total_songs = int(treeroot.getchildren()[0][0].find('title').text.split(' ')[0])
    songlist = []
    numnamehacks = 0

    for track in treeroot.getchildren()[0][slice(*rosteroffsets)]: # Slightly less dirty hack then the last version, should probably find a clean way around it like filesize checking
        song_creator = track.find('creator').text
        song_title = track.find('title').text
        song_location = track.find('location').text

        song = Song(song_creator, song_title, song_location, verbose=clargs.verbose)

        if not clargs.dl_nonamehacks:
            oldfilename = song.filename
            song.filename = apply_namehacks(song.filename)

            if song.filename != oldfilename:
                if clargs.verbose:
                    print "Applied namehack:\n%s ->\n%s\n" % (oldfilename, song.filename)
                numnamehacks += 1

        songlist.append(song)



class AersiaPlaylist(object):
    class Track(object):
        def __init__(self, creator, title, location, index, playlist=None):
            self.creator = creator
            self.title = title
            self.location = location
            self.playlist = playlist

        def __repr__(self):
            return '<Track {}: {} - {}>'.format(self.title, self.creator)


    def __init__(self, rosterurl, offsets, changelog=None, swf=None):
        self.offsets = offsets or (None, None)
        self.changelog = changelog
        self.swf = swf

        r = requests.get(rosterurl).text
        self._treeroot = ET.fromstring(r.replace('xmlns="http://xspf.org/ns/0/"',''))

        songs = self._treeroot[0][0].findtext('title').split()[0]

    def get_track(self, tracknum):
        t = self._treeroot[0][slice(*self.offsets)][tracknum]
        return self.Track(t.findtext('creator'), t.findtext('title'), t.findtext('location'), tracknum, self)

    def get_all_tracks(self):
        r = []
        i = 0
        for t in self._treeroot[0][slice(*self.offsets)]:
            r.append(self.Track(t.findtext('creator'), t.findtext('title'), t.findtext('location'), i, self))
            i+=1


a = AersiaPlaylist(
    _playlist_data['normal']['roster'],
    _playlist_data['normal']['offsets'],
    _playlist_data['normal']['changelog'],
    _playlist_data['normal']['swf'])

