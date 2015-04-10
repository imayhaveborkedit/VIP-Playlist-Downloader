from distutils.core import setup
import py2exe, sys, os
sys.argv.append('py2exe')
setup(
    options = {
        'py2exe': {
            'bundle_files': 1,
            'compressed': True,
            'optimize': 1
            }},
    console = [{'script': "VIP_playlist_downloader.py"}],
    zipfile = None,
    ascii=True,  # Exclude encodings
    excludes=['_ssl', 'pyreadline', 'difflib', 
        'doctest', 'locale', 'calendar'],
)
