from PyQt4.QtCore import QDir
from PyQt4.QtGui import *

from Icons import icons_rc
from MimeIcons import mimeicons_rc

DefaultIconPath = './E5Icons/'

class IconSet(object):
    def Camera(): return QIcon(':/Misc/camera.png')
    def Metadata(): return QIcon(':/Edit/metadata.png')
    def Add(): return QIcon(':/Edit/add.png')
    def Remove(): return QIcon(':/Edit/remove.png')
    def AddBookmark(): return QIcon(':/Edit/addbookmark.png')
    def AddFolder(): return QIcon(':/Edit/addfolder.png')
    def RemoveBookmark(): return QIcon(':/Edit/removebookmark.png')
    def RemoveFolder(): return QIcon(':/Edit/removefolder.png')
    def Image(): return QIcon(':/Edit/editimage.png')
    def Close(): return QIcon(':/File/close.png')
    def EditImage(): return QIcon(':/Misc/editimage.png')    
    def Exit(): return QIcon(':/File/exit.png')
    def History(): return QIcon(':/File/history.png')
    def Print(): return QIcon(':/File/print.png')
    def Folder(): return QIcon(':/File/openfolder.png')
    def FavoritesFolder(): return QIcon(':/Misc/favoritesfolder.png')
    def ImageFolder(): return QIcon(':/Misc/imagefolder.png')
    def ImageInfo(): return QIcon(':/Misc/imageinfo.png')
    def Photo(): return QIcon(':/Misc/photo.png')
    def Favorite(): return QIcon(':/Misc/favorite.png')
    def QtLogo(): return QIcon(':/Misc/qtlogo.png')
    def CloseButton(): return QIcon(':/Misc/closebutton.png')    
    def CloseTab(): return QIcon(':/Misc/closetab.png')
    def Help(): return QIcon(':/Misc/help.png')
    def Display(): return QIcon(':/Settings/display.png')
    def Preferences(): return QIcon(':/Settings/preferences.png')
    def Shortcuts(): return QIcon(':/Settings/shortcuts.png')
    def ViewActualSize(): return QIcon(':/View/actualsize.png')
    def ViewEnd(): return QIcon(':/View/end.png')
    def ViewFit(): return QIcon(':/View/fit.png')
    def ViewFitHeight(): return QIcon(':/View/fitheight.png')
    def ViewFitWidth(): return QIcon(':/View/fitwidth.png')
    def ViewFullscreen(): return QIcon(':/View/fullscreen.png')
    def ViewNext(): return QIcon(':/View/next.png')
    def ViewPrevious(): return QIcon(':/View/previous.png')
    def ViewReload(): return QIcon(':/View/reload.png')
    def ViewSlideshow(): return QIcon(':/View/slideshow.png')
    def ViewStart(): return QIcon(':/View/start.png')
    def ViewZoomIn(): return QIcon(':/View/zoomin.png')
    def ViewZoomOut(): return QIcon(':/View/zoomout.png')
    def WinArchiveFolder(): return QIcon(':/Windows/win_archivefolder.png')
    def WinCDRom(): return QIcon(':/Windows/win_cdrom.png')
    def WinComputer(): return QIcon(':/Windows/win_computer.png')
    def WinClosedFolder(): return QIcon(':/Windows/win_closedfolder.png')
    def WinImageFile(): return QIcon(':/Windows/win_imagefile.png')
    def WinFavorites(): return QIcon(':Windows/win_favoritesfolder.png')
    def WinLibrary(): return QIcon(':/Windows/win_library.png')
    def WinLocalDrive(): return QIcon(':/Windows/win_localdrive.png')
    def WinOpenFolder(): return QIcon(':/Windows/win_openfolder.png')
    def WinNetwork(): return QIcon(':/Windows/win_network.png')
    def WinPhotoFolder(): return QIcon(':/Windows/win_photofolder.png')
    def WinRecentPlaces(): return QIcon(':/Windows/win_recentplaces.png')
    def WinUserFolder(): return QIcon(':/Windows/win_userfolder.png')
    def WindowDebugMode(): return QIcon(':/Window/debugmode.png')
    def WindowThumbnail(): return QIcon(':/Window/thumbnail.png')
    def WindowNewTab(): return QIcon(':/Window/newtab.png')
    def WindowRemoveTab(): return QIcon(':/Window/removetab.png')

class MimeIconSet(object):
    def Folder(): return QIcon(':/MimeFolder/folder_closed.png')
    def FolderShortcut(): return QIcon(':/MimeFolder/folder_shortcut.png')
    def Image(): return QIcon(':/MimeFile/file_image.png')
    def NoneType(): return QIcon(':/MimeFile/file_generic.png')
    def Compressed(): return QIcon(':/MimeFile/file_compressed.png')
    def UserDir(): return QIcon(':/MimeFolder/folder_user.png')
    def Computer(): return QIcon(':/MimeSystem/system_computer.png')
    def Network(): return QIcon(':/MimeSystem/system_network.png')
    
class SettingsIcons(object):
    def AddItem(): return QIcon(':/Misc/add.png')
    def RemoveItem(): return QIcon(':/Misc/remove.png')
    def MoveUp(): return QIcon(':/Settings/up.png')
    def MoveDown(): return QIcon(':/Settings/down.png')
    def Favorites16x16(): return QIcon(':/Settings/favoritesicon16x16.png')
    def Favorites22x22(): return QIcon(':/Settings/favoritesicon22x22.png')
    def Favorites32x32(): return QIcon(':/Settings/favoritesicon32x32.png')
    def Shortcuts(): return QIcon(':/Settings/shortcuts.png')
    def Preferences(): return QIcon(':/Settings/preferences.png')
    def Display(): return QIcon(':/Settings/display.png')
    
class E5Icons(object):
    def __init__(self, path = DefaultIconPath):
        self.setPath(path)
            
    def icon(self, name : str = None) -> QIcon:
        if name in self.cache:
            return QIcon(self.cache[name])
        return QIcon()
    
    def iconNames(self) -> [QIcon]:
        return self.dir.entryList()
    
    def pixmap(self, name : str = None) -> QPixmap:
        if name in self.cache:
            return self.cache[file]
        return QPixmap()
    
    def setPath(self, path):
        self.dir = QDir(path, '*.png', QDir.Name, QDir.Files)
        icons = self.dir.entryList()
        self.cache = {}
        for file in icons:
            self.cache[file] = QPixmap(path + file)
