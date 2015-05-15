#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

# define log format
LOG_FORMAT = "[%(asctime)s] (%(levelname)s) %(message)s"

import sys
import time
import random
import logging

from PyQt4 import QtCore, QtGui
from qt.widget.LogWidget import LogWidget

# get root logger
log = logging.getLogger()
# set root logging level
log.setLevel(logging.DEBUG)

# initialize application
app = QtGui.QApplication(sys.argv)

# initialize widget
widget = LogWidget()
widget.setFixedSize(600, 400)
widget.handler.setFormatter(logging.Formatter(LOG_FORMAT))

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