from PyQt4.QtCore import QSysInfo

from .PlastiqueStyle import KyPlastiqueStyle
from .WindowsStyle import KyWindowsStyle
from .WindowsXPStyle import KyWindowsXPStyle
from .WindowsVistaStyle import KyWindowsVistaStyle

class KyStyleFactory():
    @staticmethod
    def create(key : str = None):
        styles = ['Plastique', 'Windows']
        testWin = QSysInfo.WindowsVersion
        if testWin & QSysInfo.WV_NT_based:
            if testWin == QSysInfo.WV_WINDOWS7 or testWin == QSysInfo.WV_VISTA:
                styles.append('WindowsXP')
                styles.append('WindowsVista')
            elif testWin == QSysInfo.WV_XP or QSysInfo.WV_2003:
                styles.append('WindowsXP')
        
        if key in styles:
            if key == 'Plastique':
                return KyPlastiqueStyle()
            elif key == 'Windows':
                return KyWindowsStyle()
            elif key == 'WindowsXP':
                return KyWindowsXPStyle()
            elif key == 'WindowsVista':
                return KyWindowsVistaStyle()
    
    @staticmethod
    def keys():
        styles = ['Plastique', 'Windows']
        testWin = QSysInfo.WindowsVersion
        if testWin & QSysInfo.WV_NT_based:
            if testWin == QSysInfo.WV_WINDOWS7 or testWin == QSysInfo.WV_VISTA:
                styles.append('WindowsXP')
                styles.append('WindowsVista')
            elif testWin == QSysInfo.WV_XP or QSysInfo.WV_2003:
                styles.append('WindowsXP')
            
        return styles
