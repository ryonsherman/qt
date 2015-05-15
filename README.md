# Qt Resources
A collection of various PyQt4 resources.

## Utilities
```python
from qt import util
```

util.**hex2QColor**(*color*)

Converts a string hexadecimal value to a [QtGui.QColor](http://pyqt.sourceforge.net/Docs/PyQt4/qcolor.html) object.
```python
>>> util.hex2QColor('#112233')
<PyQt4.QtGui.QColor object at 0x7f16a5502668>
>>> c = util.hex2QColor('#112233')
>>> c.red(), c.green(), c.blue()
(17, 34, 51)
```

---

util.**scrollBuffer**(*buffer*, *position*)

util.**scrollBufferToStart**(*buffer*)

util.**scrollBufferToEnd**(*buffer*)

Scrolls a text buffer widget to a specified position.
```python
b = QtGui.QPlainTextEdit()
util.scrollToEnd(b)
b.insertPlainText(text)
```

## Widgets
* [widget.**LogWidget**](https://github.com/ryonsherman/qt/tree/master/widget/LogWidget) – provides real-time, auto-scrolling, Python [logging](https://docs.python.org/2/library/logging.html) output