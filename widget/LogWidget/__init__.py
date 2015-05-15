#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from PyQt4 import QtGui

from qt import util
from qt.log import log

# define log output widget
class LogWidget(QtGui.QPlainTextEdit):
    """ A QPlainTextEdit widget to provide logging output """
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QPlainTextEdit.__init__(self, *args, **kwargs)

        # connect to log buffer output
        log.buffer.signal.connect(self.onLogBufferChanged)
        # set output to read only
        self.setReadOnly(True)

    def onLogBufferChanged(self, data):
        """ Updates widget output on log buffer change """
        # scroll output to end of buffer
        util.scrollBufferToEnd(self)
        # append log data to output
        self.insertPlainText(data)
