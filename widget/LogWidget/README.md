LogWidget is a [QtGui.QPlainTextEdit](http://pyqt.sourceforge.net/Docs/PyQt4/qplaintextedit.html) widget that provides real-time, auto-scrolling, Python [logging](https://docs.python.org/2/library/logging.html) output.

1. [log.QLogBuffer](https://github.com/ryonsherman/qt/blob/master/log.py) provides a [StringIO](https://docs.python.org/2/library/stringio.html) buffer handled by [logging.StreamHandler](https://docs.python.org/2/library/logging.handlers.html#streamhandler).
2. StringIO.write() emits a [QtCore.pyqtSignal](http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html#defining-new-signals-with-pyqtsignal) containing the unicode log data.
3. LogWidget.onLogBufferChanged() listens to this signal and updates the widget output.

**Example**
```python
#!/usr/bin/env python2

import sys
from qt.widget.LogWidget import LogWidget

app = QtGui.QApplication(sys.argv)

widget = LogWidget()
widget.setFixedSize(600, 400)
widget.show()

sys.exit(app.exec_())
```

![LogWidget](https://github.com/ryonsherman/qt/blob/master/widget/LogWidget/widget.png)