#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

import logging

from StringIO import StringIO
from PyQt4 import QtCore, QtGui

# define qt log buffer object
class QLogBuffer(QtCore.QObject, StringIO):
    # define buffer signal
    signal = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        # initialize object
        QtCore.QObject.__init__(self)
        # initialize input/output buffer
        StringIO.__init__(self, *args, **kwargs)

    def write(self, data):
        # require data
        if not data: return
        # emit unicode data to signal
        self.signal.emit(unicode(data))
        # write buffer
        StringIO.write(self, data)

# get global logger
log = logging.getLogger()
# set root logging level
log.setLevel(logging.DEBUG)
# define log format
log_format = "[%(asctime)s] (%(levelname)s) %(message)s"
# initialize log buffer
log_buffer = QLogBuffer()
# initialize log handler
log_handler = logging.StreamHandler(log_buffer)
# set log handler format
log_handler.setFormatter(logging.Formatter(log_format))
# add buffer handler to logger
log.addHandler(log_handler)

# define log output widget
class LogWidget(QtGui.QPlainTextEdit):
    """ A QPlainTextEdit widget to provide logging output """
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QPlainTextEdit.__init__(self, *args, **kwargs)

        # connect to log buffer output
        log_buffer.signal.connect(self.onLogBufferChanged)
        # set output to read only
        self.setReadOnly(True)

    def onLogBufferChanged(self, data):
        """ Updates widget output on log buffer change """
        # scroll output to end of buffer
        self.moveCursor(QtGui.QTextCursor.End)
        # append log data to output
        self.insertPlainText(data)
