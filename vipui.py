import sys, os, requests

from ui import ui

from PyQt4 import QtCore, QtGui
from PyQt4 import phonon

APP = UI = MainWindow = None

class CodeWindow(QtGui.QMainWindow):
    def testslot(self):
        print self

    def play_clicked(self):
        print 'play clicked'

    def pause_clicked(self):
        print 'pause clicked'

    def stop_clicked(self):
        print 'stop clicked'

    def playlist_download_clicked(self):
        print 'download button'

    def playlist_download_all_clicked(self):
        print 'download all button'



    def setup_tables(self):
        pass

    def setup_audio(self):
        pass

    def setup(self):
        setup_audio()




def setup():
    global UI, MainWindow, APP

    APP = QtGui.QApplication(sys.argv)
    MainWindow = CodeWindow()
    UI = ui.Ui_MainWindow()
    UI.setupUi(MainWindow)

def run():
    MainWindow.show()
    sys.exit(APP.exec_())

if __name__ == '__main__':
    setup()
    run()


'''
Useful code

Volume slider conenction:
    self.ui.volumeSlider.setAudioOutput(self.ui.videoPlayer.audioOutput())


'''