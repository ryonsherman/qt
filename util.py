#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from PyQt4 import QtGui

def hex2QColor(c):
    """ Convert hex value to QColor object """
    # get hex color string
    c = str(c).lstrip('#')
    # parse color values
    r = int(c[0:2], 16)
    g = int(c[2:4], 16)
    b = int(c[4:6], 16)
    # return QColor object
    return QtGui.QColor(r, g, b)

def scrollBuffer(buf, pos):
    """ Scroll text buffer to position """
    # get current buffer text cursor
    cursor = buf.textCursor()
    # move cursor to specified position
    cursor.movePosition(pos)
    # set buffer text cursor
    buf.setTextCursor(cursor)
    # ensure buffer cursor is visible
    buf.ensureCursorVisible()

def scrollToStart(buf):
    """ Scroll to start of buffer """
    return scrollBuffer(buf, QtGui.QTextCursor.Start)

def scrollToEnd(buf):
    """ Scroll to end of buffer """
    return scrollBuffer(buf, QtGui.QTextCursor.End)