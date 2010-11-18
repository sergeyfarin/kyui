#utilities
from PyQt4.QtCore import *
from PyQt4.QtGui import *

filterReturns = {'JPEG' : 'JPG'}

imageTypes = ['JPG', 'JPEG', 'PNG']

strFromQSizeFormat = {
        'QSize(w, h)' : 'QSize({} ,{})',
        '(w, h)' : '({}, {})',
        'wxh' : '{}x{}',
        '(wxh)' : '({}x{})'}

def strFromQSize(size : QSize = None, format : strFromQSizeFormat = None) -> str:
    assert isinstance(size, QSize)
    assert format in strFromQSizeFormat.keys()
    w = size.width()
    h = size.height()
    return str.format(strFromQSizeFormat[format], w, h)
    

class Utilities():
    # Parses a file filter from an open file dialog, returning the file type
    # in all caps. Will search filterReturns for common file formats with the
    # most common variation unless returnFirstFilter is True
    # e.g. if we have '*.jpeg; *.jpg' as our filter, returns 'JPG' instead of 'JPEG'
    # when returnFirstFilter is False; if it is True, returns 'JPEG'
    @staticmethod
    def parseFileFilter(filter, returnFirstFilter = False):
        # Check if the file filter has a description, e.g. Adobe PDF (*.pdf)
        if '(' in filter and filter.endswith(')'):
            # Splits the string into the a list: [description, filters]
            stripped = filter.rstrip(')').split('(')
            
            # Eliminates all but the final portion of stripped. We could do:
            # filter = stripped[:len(stripped)]
            # but some jackass might have used a filter like this:
            # Adobe PDF (a document format) (*.pdf)
            filter = stripped[1]
            
        # Our filter should look something like this: '*.jpeg; *.jpg'
        # Make it all uppercase, and split it along the semicolons.
        parsed = filter.upper().split(';')
        
        # Remove all but the extensions and any whitespace
        i = 0
        for i in range(len(parsed)):
            parsed[i] = parsed[i].strip(' *.')
        # If nothing is found in filterReturns, falls through to returning the first
        # item in parsed
        if returnFirstFilter:
            for item in parsed:
                if item in filterReturns:
                    return filterReturns[item]
            return parsed[0]
        else:
            return parsed
    
    @staticmethod
    def isImage(fileInfo):
        suffix = fileInfo.suffix().upper()
        if suffix in imageTypes:
            return suffix
        return False
    
    def testFlag(f, i):
        if i & f == f:
            if f != 0 or i == int(f):
               return True
        return False
