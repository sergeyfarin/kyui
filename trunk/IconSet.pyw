from PyQt4.QtGui import *

from Icons import icons_rc
from MimeIcons import mimeicons_rc

class IconSet(object):
    @staticmethod
    def MainIcon(): return QIcon(':/Misc/camera.png')

    @staticmethod
    def EditMetadata(): return QIcon(':/Edit/metadata.png')
    @staticmethod
    def EditAdd(): return QIcon(':/Edit/add.png')
    @staticmethod
    def EditRemove(): return QIcon(':/Edit/remove.png')
    @staticmethod
    def EditAddBookmark(): return QIcon(':/Edit/addbookmark.png')
    @staticmethod
    def EditAddFolder(): return QIcon(':/Edit/addfolder.png')
    @staticmethod
    def EditRemoveBookmark(): return QIcon(':/Edit/removebookmark.png')
    @staticmethod
    def EditRemoveFolder(): return QIcon(':/Edit/removefolder.png')
    @staticmethod
    def EditImage(): return QIcon(':/Edit/editimage.png')

    @staticmethod
    def FileClose(): return QIcon(':/File/close.png')
    @staticmethod
    def FileEditImage(): return QIcon(':/Misc/editimage.png')
    @staticmethod
    def FileExit(): return QIcon(':/File/exit.png')
    @staticmethod
    def FileHistory(): return QIcon(':/File/history.png')
    @staticmethod
    def FilePrint(): return QIcon(':/File/print.png')
    @staticmethod
    def FileOpen(): return QIcon(':/File/openfolder.png')

    @staticmethod
    def FavoritesFolder(): return QIcon(':/Misc/favoritesfolder.png')
    @staticmethod
    def ImageFolder(): return QIcon(':/Misc/imagefolder.png')
    @staticmethod
    def ImageInfo(): return QIcon(':/Misc/imageinfo.png')
    @staticmethod
    def Photo(): return QIcon(':/Misc/photo.png')
    @staticmethod
    def Favorite(): return QIcon(':/Misc/favorite.png')
    @staticmethod
    def MiscQtLogo(): return QIcon(':/Misc/qtlogo.png')
    @staticmethod
    def CloseButton(): return QIcon(':/Misc/closebutton.png')
    @staticmethod
    def CloseTab(): return QIcon(':/Misc/closetab.png')
    @staticmethod
    def Help(): return QIcon(':/Misc/help.png')
    
    @staticmethod
    def SettingsDisplay(): return QIcon(':/Settings/display.png')
    @staticmethod
    def SettingsPreferences(): return QIcon(':/Settings/preferences.png')
    @staticmethod
    def SettingsShortcuts(): return QIcon(':/Settings/shortcuts.png')
    
    @staticmethod
    def ViewActualSize(): return QIcon(':/View/actualsize.png')
    @staticmethod
    def ViewEnd(): return QIcon(':/View/end.png')
    @staticmethod
    def ViewFit(): return QIcon(':/View/fit.png')
    @staticmethod
    def ViewFitHeight(): return QIcon(':/View/fitheight.png')
    @staticmethod
    def ViewFitWidth(): return QIcon(':/View/fitwidth.png')
    @staticmethod
    def ViewFullscreen(): return QIcon(':/View/fullscreen.png')
    @staticmethod
    def ViewNext(): return QIcon(':/View/next.png')
    @staticmethod
    def ViewPrevious(): return QIcon(':/View/previous.png')
    @staticmethod
    def ViewReload(): return QIcon(':/View/reload.png')
    @staticmethod
    def ViewSlideshow(): return QIcon(':/View/slideshow.png')
    @staticmethod
    def ViewStart(): return QIcon(':/View/start.png')
    @staticmethod
    def ViewZoomIn(): return QIcon(':/View/zoomin.png')
    @staticmethod
    def ViewZoomOut(): return QIcon(':/View/zoomout.png')
    
    @staticmethod
    def WinArchiveFolder(): return QIcon(':/Windows/win_archivefolder.png')
    @staticmethod
    def WinCDRom(): return QIcon(':/Windows/win_cdrom.png')
    @staticmethod
    def WinComputer(): return QIcon(':/Windows/win_computer.png')
    @staticmethod
    def WinClosedFolder(): return QIcon(':/Windows/win_closedfolder.png')
    @staticmethod
    def WinImageFile(): return QIcon(':/Windows/win_imagefile.png')
    @staticmethod
    def WinFavorites(): return QIcon(':Windows/win_favoritesfolder.png')
    @staticmethod
    def WinLibrary(): return QIcon(':/Windows/win_library.png')
    @staticmethod
    def WinLocalDrive(): return QIcon(':/Windows/win_localdrive.png')
    @staticmethod
    def WinOpenFolder(): return QIcon(':/Windows/win_openfolder.png')
    @staticmethod
    def WinNetwork(): return QIcon(':/Windows/win_network.png')
    @staticmethod
    def WinPhotoFolder(): return QIcon(':/Windows/win_photofolder.png')
    @staticmethod
    def WinRecentPlaces(): return QIcon(':/Windows/win_recentplaces.png')
    @staticmethod
    def WinUserFolder(): return QIcon(':/Windows/win_userfolder.png')
    @staticmethod
    def WindowDebugMode(): return QIcon(':/Window/debugmode.png')
    @staticmethod
    def WindowThumbnail(): return QIcon(':/Window/thumbnail.png')
    @staticmethod
    def WindowNewTab(): return QIcon(':/Window/newtab.png')
    @staticmethod
    def WindowRemoveTab(): return QIcon(':/Window/removetab.png')

class MimeIconSet(object):
    @staticmethod
    def Folder(): return QIcon(':/MimeFolder/folder_closed.png')
    @staticmethod
    def FolderShortcut(): return QIcon(':/MimeFolder/folder_shortcut.png')
    @staticmethod
    def Image(): return QIcon(':/MimeFile/file_image.png')
    @staticmethod
    def NoneType(): return QIcon(':/MimeFile/file_generic.png')
    @staticmethod
    def Compressed(): return QIcon(':/MimeFile/file_compressed.png')
    @staticmethod
    def UserDir(): return QIcon(':/MimeFolder/folder_user.png')
    @staticmethod
    def Computer(): return QIcon(':/MimeSystem/system_computer.png')
    @staticmethod
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
