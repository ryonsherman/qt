# Qt

## Utilities
util.**hex2QColor**(*color*)

Converts a string hexadecimal value to a [QtGui::QColor](http://pyqt.sourceforge.net/Docs/PyQt4/qcolor.html) object.
```python
>>> from util import hex2QColor

>>> hex2QColor('#112233')
<PyQt4.QtGui.QColor object at 0x7f16a5502668>

>>> c = hex2QColor('#112233')
>>> c.red(), c.green(), c.blue()
(17, 34, 51)
```