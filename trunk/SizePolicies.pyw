from PyQt4.QtCore import *
from PyQt4.QtGui import *

from collections import namedtuple

SizePolicies = \
    namedtuple('SizePolicies', 'Fixed Expanding Preferred')( \
    (QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)),
    (QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)), 
    (QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)))
