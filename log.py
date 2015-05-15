#!/usr/bin/env python2

import logging

from PyQt4 import QtCore
from StringIO import StringIO

# define qt log buffer object
class QLogBuffer(QtCore.QObject, StringIO):
    # define buffer signal
    signal = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        # initialize object
        QtCore.QObject.__init__(self)
        # initialize buffer input/output
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
# initialize log buffer
log.buffer = QLogBuffer()
# add buffer handler to logger
log.addHandler(logging.StreamHandler(log.buffer))
