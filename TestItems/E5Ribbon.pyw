# E5RibbonAction

from PyQt4.QtCore import *
from PyQt4.QtGui import *

E5Actions = ( \
    ('File', ( \
        'New', 
        'Open')
        ),
    ('Edit', ( \
        'Clipboard', 
        'Changes', 
        'Indentation', 
        'Editing',
        'Extras', 
        'Search')
        ), 
    ('Navigation',
        ()
        ),
    ('Run',
        ()
        ), 
    ('Project',
        ()
        ),
    ('VCS',
        ()
        ),
    ('View',
        ()
        ),
    ('Preferences',
        ()
        ),
    ('Help'
        ()
        )
    )
    
def generateEditActions() -> QToolBar:
    tb = QToolBar('Edit', None)
    pass
