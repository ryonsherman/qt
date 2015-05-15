#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

import logging

from StringIO import StringIO
from PyQt4 import QtCore, QtGui


class QLogBuffer(QtCore.QObject, StringIO):
    """ A StringIO buffer that emits a pyqtSignal """
    # define buffer change signal
    signal = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        # initialize object
        QtCore.QObject.__init__(self)
        # initialize input/output buffer
        StringIO.__init__(self, *args, **kwargs)

    def write(self, data):
        # require data
        if not data: return
        # emit buffer change signal with unicoded data
        self.signal.emit(unicode(data))
        # write buffer
        StringIO.write(self, data)


class LogWidget(QtGui.QPlainTextEdit):
    """ A QPlainTextEdit widget to provide logging output """
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QPlainTextEdit.__init__(self, *args, **kwargs)

        # initialize log buffer
        self.buffer = QLogBuffer()
        # initialize log buffer handler
        self.handler = logging.StreamHandler(self.buffer)

        # add buffer handler to global logger
        logging.getLogger().addHandler(self.handler)

        # connect to log buffer output
        self.buffer.signal.connect(self.onLogBufferChanged)
        # set output to read only
        self.setReadOnly(True)

    def onLogBufferChanged(self, data):
        """ Updates widget output on log buffer change """
        # scroll output to end of buffer
        self.moveCursor(QtGui.QTextCursor.End)
        # append log data to output
        self.insertPlainText(data)
