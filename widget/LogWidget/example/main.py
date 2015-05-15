#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

import sys
import time
import random
import logging

from qt.log import log
from qt.widget.LogWidget import LogWidget

# set root logging level
log.setLevel(logging.DEBUG)
# define log format
log_format = "[%(asctime)s] (%(levelname)s) %(message)s"
# get log handler
log_handler = log.handlers[0]
# set log handler format
log_handler.setFormatter(logging.Formatter(log_format))

from PyQt4 import QtCore, QtGui

# initialize application
app = QtGui.QApplication(sys.argv)

# initialize widget
widget = LogWidget()
widget.setFixedSize(600, 400)

# initialize window with widget
window = QtGui.QMainWindow()
window.setCentralWidget(widget)
window.show()

# define demo thread
class Thread(QtCore.QThread):
    def run(self):
        # continuously log random messages
        while True:
            methods = ('debug', 'info', 'warning', 'error', 'critical')
            method = getattr(log, random.choice(methods))
            method("Example log message")
            time.sleep(1)
# initialie and start demo thread
thread = Thread()
thread.start()

# execute application
sys.exit(app.exec_())