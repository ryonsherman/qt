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


def main():
    """ Provides an example implementation of the widget """
    import sys

    # initialize application
    app = QtGui.QApplication(sys.argv)
    
    # initialize widget
    widget = LogWidget()
    widget.setFixedSize(600, 400)

    # initialize window with widget
    window = QtGui.QMainWindow()
    window.setCentralWidget(widget)
    window.show()

    # EXAMPLE START
    import time
    import random
    import logging

    from PyQt4 import QtCore

    # set root logging level
    log.setLevel(logging.DEBUG)
    # define log format
    log_format = "[%(asctime)s] (%(levelname)s) %(message)s"
    # get log handler
    log_handler = log.handlers[0]
    # set log handler format
    log_handler.setFormatter(logging.Formatter(log_format))

    # define example thread
    class Thread(QtCore.QThread):
        def run(self):
            # continuously log random messages
            while True:
                methods = ('debug', 'info', 'warning', 'error', 'critical')
                method = getattr(log, random.choice(methods))
                method("Example log message")
                time.sleep(1)
    thread = Thread()
    thread.start()
    # EXAMPLE END

    # execute application
    sys.exit(app.exec_())

if __name__ == '__main__':
    # execute example
    main()
