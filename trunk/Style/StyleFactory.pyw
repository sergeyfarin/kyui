from PyQt4.QtCore import QSysInfo

from .PlastiqueStyle import KyPlastiqueStyle
from .WindowsStyle import KyWindowsStyle
from .WindowsXPStyle import KyWindowsXPStyle
from .WindowsVistaStyle import KyWindowsVistaStyle
from .Windows7Style import KyWindows7Style

class KyStyleFactory():
    @staticmethod
    def create(key : str = None):
        styles = ['Plastique', 'Windows']
        testWin = QSysInfo.WindowsVersion
        if testWin & QSysInfo.WV_NT_based:
            if testWin == QSysInfo.WV_WINDOWS7 or testWin == QSysInfo.WV_VISTA:
                styles.append('WindowsXP')
                styles.append('WindowsVista')
                styles.append('Windows7')
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
            elif key == 'Windows7':
                return KyWindows7Style()
    
    @staticmethod
    def keys():
        styles = ['Plastique', 'Windows']
        testWin = QSysInfo.WindowsVersion
        if testWin & QSysInfo.WV_NT_based:
            if testWin == QSysInfo.WV_WINDOWS7 or testWin == QSysInfo.WV_VISTA:
                styles.append('WindowsXP')
                styles.append('WindowsVista')
                styles.append('Windows7')
            elif testWin == QSysInfo.WV_XP or QSysInfo.WV_2003:
                styles.append('WindowsXP')
            
        return styles
