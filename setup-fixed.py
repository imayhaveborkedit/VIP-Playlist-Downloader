from distutils.core import setup
import py2exe, sys, os
sys.argv.append('py2exe')
setup(
    options = {
        'py2exe': {
            'bundle_files': 1,
            'compressed': True,
            'optimize': 1,
            'dist_dir': '.',
            'excludes': ['pyreadline', 'doctest', 'gtk', 'glib', 'gobject', 'PyQt4.QtCore', 'PyQt4.QtGui'],
            'dll_excludes': ['msvcr71.dll', 'w9xpopen.exe']
            }},
    console = [{'script': "watcher.py"}],
    zipfile = None,
)
