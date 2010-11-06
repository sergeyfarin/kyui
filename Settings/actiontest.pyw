from PyQt4.QtCore import *
from PyQt4.QtGui import *
from iconset import SettingsIcons, IconSet
from settings_default import DefaultSettings

###################################
#   Toolbars
#
# Static --
# object name
# allowed areas
# movable
# orientation
# windowtitle
# 
# Dynamic --
# floating
# orientation
# 
#
# User --
# floatable
# iconsize
# toolbuttonstyle
#
###################################

###################################
#   Actions
#
# Static --
# object name
# autorepeat
# #enabled
# checkable
# icon
# iconText
# #iconVisibileInMenu
# menu
# #priority
# shortcutcontext
# #statustip
# text
# tooltip
# #visible
# whatsthis

# User --
# shortcut
# toolbar
###################################

class ToolbarTestClass(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('toolbarTestClass')
        
        settings = DefaultSettings()
        settings.setupDefaults()
        
        self.toolbarList = []
        
        self.fileToolBar = QToolBar('File', self)
        self.fileToolBar.setObjectName('fileToolBar')
        
        self.navToolBar = QToolBar('Navigation', self)
        self.navToolBar.setObjectName('navToolBar')
        
        self.zoomToolBar = QToolBar('Zoom', self)
        self.zoomToolBar.setObjectName('zoomToolBar')
        
        self.windowToolBar = QToolBar('Window', self)
        self.windowToolBar.setObjectName('windowToolBar')
        
        self.helpToolBar = QToolBar('Help', self)
        self.helpToolBar.setObjectName('helpToolBar')
        
    def setupToolbars(self):
        atc = ActionTestClass()
        actionList = atc.getActionList()

class ActionTestClass(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('ActionTestClass')
        
        self.actionList = []
        
        self.__setupActions()
        self.loadSettings(self.actionList)
        
    def __setupActions(self):
        # File menu
        self.actionOpen = QAction(IconSet.FileOpen(), '&Open...', self)
        self.actionOpen.setObjectName('actionOpen')
        self.actionOpen.setAutoRepeat(False)
        self.actionOpen.setToolTip('Open a new image or folder')
        self.actionOpen.setData('Open File in Tab')
        
        self.actionClose = QAction(IconSet.FileClose(), '&Close', self)
        self.actionClose.setObjectName('actionClose')
        self.actionClose.setToolTip('Close the currently open file')
        self.actionClose.setData('Close File')
        
        self.actionPrint = QAction(IconSet.FilePrint(), '&Print...', self)
        self.actionPrint.setObjectName('actionPrint')
        self.actionPrint.setToolTip('Print the currently displayed image')
        self.actionPrint.setData('Print Image')
        
        self.actionExit = QAction(IconSet.FileExit(), 'E&xit', self)
        self.actionExit.setObjectName('actionExit')
        self.actionExit.setToolTip('Quit the image viewer')
        self.actionExit.setData('Exit Program')
        
        # Edit menu
        self.actionAddBookmark = QAction(IconSet.EditAddBookmark(), '&Add Bookmark...', self)
        self.actionAddBookmark.setObjectName('actionAddBookmark')
        self.actionAddBookmark.setEnabled(False)
        self.actionAddBookmark.setIconText('Bookmark')
        self.actionAddBookmark.setToolTip('Bookmark this folder')
        self.actionAddBookmark.setWhatsThis('Bookmarking a folder adds it to a list of folders for easy access in the future. To find your bookmarks, select Favorites from the dropdown box in the Browser Dock.')
        self.actionAddBookmark.setData('Add Bookmark')
        
        self.actionRemoveBookmark = QAction(IconSet.EditRemoveBookmark(), '&Remove Bookmark', self)
        self.actionRemoveBookmark.setObjectName('actionRemoveBookmark')
        self.actionRemoveBookmark.setAutoRepeat(False)
        self.actionRemoveBookmark.setData('Remove Bookmark')
        self.actionRemoveBookmark.setEnabled(False)
        self.actionRemoveBookmark.setIconText('UnBookmark')
        self.actionRemoveBookmark.setStatusTip('')
        self.actionRemoveBookmark.setToolTip('Remove a bookmark on this folder, if one exists')
        self.actionRemoveBookmark.setWhatsThis('This will remove the current folder from your bookmark list. This option is only available if the current folder is already in your bookmark list.')
        
        self.actionEditMetadata = QAction(IconSet.EditMetadata(), 'Edit &Metadata', self)
        self.actionEditMetadata.setObjectName('actionEditMetadata')
        self.actionEditMetadata.setIconText('Metadata')
        self.actionEditMetadata.setEnabled(False)
        self.actionEditMetadata.setToolTip('Modify the metadata stored in the current image')
        self.actionEditMetadata.setData('Edit Image Metadata')
        
        self.actionOpenExplorer = QAction(IconSet.WinLibrary(), 'Open in Windows &Explorer', self)
        self.actionOpenExplorer.setObjectName('actionOpenExplorer')
        self.actionOpenExplorer.setIconText('Explore')
        self.actionOpenExplorer.setToolTip('View the current folder in Windows Explorer')
        self.actionOpenExplorer.setEnabled(False)
        self.actionOpenExplorer.setData('Open Windows Explorer')
        
        self.actionOpenExternalViewer = QAction(IconSet.EditImage(), 'Open in External &Viewer', self)
        self.actionOpenExternalViewer.setObjectName('actionOpenExternalViewer')
        self.actionOpenExternalViewer.setIconText('External Viewer')
        self.actionOpenExternalViewer.setToolTip('Open the current image in an external viewer')
        self.actionOpenExternalViewer.setEnabled(False)
        self.actionOpenExternalViewer.setData('Open External Viewer')
        
        self.actionPreferences = QAction(IconSet.SettingsPreferences(), '&Preferences...', self)
        self.actionPreferences.setObjectName('actionPreferences')
        self.actionPreferences.setToolTip('Change how the program appears and behaves')
        self.actionPreferences.setData('Preferences')
       
        # View menu
        self.actionZoomIn = QAction(IconSet.ViewZoomIn(), 'Zoom &In', self)
        self.actionZoomIn.setObjectName('actionZoomIn')
        self.actionZoomIn.setToolTip('Increase the visible size of the current image')
        self.actionZoomIn.setData('Zoom In')
        
        
        self.actionZoomOut = QAction(IconSet.ViewZoomOut(), 'Zoom &Out', self)
        self.actionZoomOut.setObjectName('actionZoomOut')
        self.actionZoomOut.setToolTip('Make the current image appear smaller')
        self.actionZoomOut.setData('Zoom Out')
        
        
        self.actionActualSize = QAction(IconSet.ViewActualSize(), '&Actual Size', self)
        self.actionActualSize.setObjectName('actionActualSize')
        self.actionActualSize.setToolTip('View the current image at its actual size')
        self.actionActualSize.setData('View Image at Actual Size')
        
        
        self.actionFitScreen = QAction(IconSet.ViewFit(), '&Fit to Screen', self)
        self.actionFitScreen.setObjectName('actionFitScreen')
        self.actionFitScreen.setToolTip('Fit the current image within the available space of your screen')
        self.actionFitScreen.setIconText('Screen Fit')
        self.actionFitScreen.setData('Fit to Screen')
        
        
        self.actionFitScreenWidth = QAction(IconSet.ViewFitWidth(), 'Fit to Screen &Width', self)
        self.actionFitScreenWidth.setObjectName('actionFitScreenWidth')
        self.actionFitScreenWidth.setIconText('Width Fit')
        self.actionFitScreenWidth.setData('Fit to Screen Width')
        self.actionFitScreenWidth.setToolTip('Fit the image to the width of your screen')
        
        
        self.actionFitScreenHeight = QAction(IconSet.ViewFitHeight(), 'Fit to Screen &Height', self)
        self.actionFitScreenHeight.setObjectName('actionFitScreenHeight')
        self.actionFitScreenHeight.setIconText('Height Fit')
        self.actionFitScreenHeight.setData('Fit to Screen Height')
        self.actionFitScreenHeight.setToolTip('Fit the image within the height availabe on your screen')
        
        
        self.actionFullScreen = QAction(IconSet.ViewFullscreen(), 'F&ullscreen', self)
        self.actionFullScreen.setObjectName('actionFullScreen')
        self.actionFullScreen.setToolTip('Go to fullscreen mode; press F11 to exit')
        self.actionFullScreen.setData('Fullscreen Mode')
        self.actionFullScreen.setCheckable(True)
        

        self.actionSlideshow = QAction(IconSet.ViewSlideshow(), 'S&lideshow', self)
        self.actionSlideshow.setObjectName('actionSlideshow')
        self.actionSlideshow.setData('Slideshow Mode')
        self.actionSlideshow.setToolTip('Start a slideshow of the images in the current folder')
        
        
        self.actionPreviousImage = QAction(IconSet.ViewPrevious(), '&Previous Image', self)
        self.actionPreviousImage.setObjectName('actionPreviousImage')
        self.actionPreviousImage.setIconText('Previous')
        self.actionPreviousImage.setData('View Previous Image')
        self.actionPreviousImage.setToolTip('Go back to the previous image in the current folder')
        
        self.actionNextImage = QAction(IconSet.ViewNext(), '&Next Image', self)
        self.actionNextImage.setObjectName('actionNextImage')
        self.actionNextImage.setIconText('Next')
        self.actionNextImage.setData('View Next Image')
        self.actionNextImage.setToolTip('Go to the next image in the current folder')
        
        
        self.actionFirstImage = QAction(IconSet.ViewStart(), '&First Image', self)
        self.actionFirstImage.setObjectName('actionFirstImage')
        self.actionFirstImage.setIconText('First')
        self.actionFirstImage.setData('View First Image')
        self.actionFirstImage.setToolTip('Go to the first image in the current directory')
        
        self.actionLastImage = QAction(IconSet.ViewEnd(), '&Last Image', self)
        self.actionLastImage.setObjectName('actionLastImage')
        self.actionLastImage.setIconText('Last')
        self.actionLastImage.setToolTip('Go to the last image in the current folder')
        self.actionLastImage.setShortcut('PgUp')
        self.actionLastImage.setData('View Last Image')
        
        self.actionRefreshImage = QAction('&Reload', self)
        self.actionRefreshImage.setObjectName('actionRefreshImage')
        self.actionRefreshImage.setToolTip('Reload the currently displayed image')
        self.actionRefreshImage.setIcon(IconSet.ViewReload())
        self.actionRefreshImage.setShortcut('F5')
        self.actionRefreshImage.setData('Reload Image')

        #Window menu
        self.actionNewTab = QAction(IconSet.WindowNewTab(), '&New Tab', self)
        self.actionNewTab.setObjectName('actionNewTab')
        self.actionNewTab.setData('Open New Tab')
        self.actionNewTab.setShortcut('Ctrl+T')
        self.actionNewTab.setToolTip('Open a new tab for viewing images')
        
        self.actionRemoveTab = QAction(IconSet.WindowRemoveTab(), '&Close Tab', self)
        self.actionRemoveTab.setObjectName('actionRemoveTab')
        self.actionRemoveTab.setData('Close Tab')
        self.actionRemoveTab.setShortcut('Ctrl+F4')
        self.actionRemoveTab.setToolTip('Close the currently open tab')
        
#        self.actionInfoDock = QAction('&Image Info', self)
#        self.actionInfoDock.setObjectName('actionInfoDock')
#        self.actionInfoDock.setIcon(IconSet.ImageInfo())
#        self.actionInfoDock.setData('Toggle EXIF Data Dock')
#        self.actionInfoDock.setShortcut('I')
#        self.actionInfoDock.setToolTip('Open or close the image attribute display')
#        self.actionInfoDock.setCheckable(True)
        
#        self.actionIconDock = self.iconDock.toggleViewAction()
#        self.actionIconDock.setObjectName('actionIconDock')
#        self.actionIconDock.setText('&Thumbnail Viewer')
#        self.actionIconDock.setIcon(IconSet.WindowThumbnail())
#        self.actionIconDock.setIconText('Thumbnails')
#        self.actionIconDock.setToolTip('Open the thumbnail viewer')
#        self.actionIconDock.setData('Toggle Thumbnail Viewer')
#        self.actionIconDock.setShortcut('T')
#        self.actionIconDock.setCheckable(True)
#        
#        self.actionBrowserDock = self.browserDock.toggleViewAction()
#        self.actionBrowserDock.setObjectName('actionBrowserDock')
#        self.actionBrowserDock.setIcon(IconSet.WinPhotoFolder())
#        self.actionBrowserDock.setText('&Folder Browser')
#        self.actionBrowserDock.setIconText('Folders')
#        self.actionBrowserDock.setToolTip('Open or close the Folder Browser')
#        self.actionBrowserDock.setShortcut('D')
#        self.actionBrowserDock.setData('Toggle Folder Browser')
#        self.actionBrowserDock.setCheckable(True)
#        
#        self.actionDebugDock = self.debugDock.toggleViewAction()
#        self.actionDebugDock.setObjectName('actionDebugDock')
#        self.actionDebugDock.setIcon(IconSet.WindowDebugMode())
#        self.actionDebugDock.setText('&Debug Viewer')
#        self.actionDebugDock.setIconText('Debug')
#        self.actionDebugDock.setToolTip('Open the debug information window')
#        self.actionDebugDock.setData('Toggle Debug Dock')
#        self.actionDebugDock.setCheckable(True)


        # Help menu
        self.actionAbout = QAction(IconSet.Help(), '&About', self)
        self.actionAbout.setObjectName('actionAbout')
        self.actionAbout.setShortcut('F1')
        self.actionAbout.setData('About LIDS')
#        self.actionList.append[actionAbout]
        
        self.actionAboutQt = QAction(IconSet.MiscQtLogo(), 'About &Qt', self)
        self.actionAboutQt.setObjectName('actionAboutQt')
        self.actionAboutQt.setShortcut('About Qt')
        
        #NOTE: This should contain ALL the registered actions. It's handy that way.
        self.actionList = [ \
            self.actionOpen,
            self.actionClose,
            self.actionPrint,
            self.actionExit,
            self.actionAddBookmark,
            self.actionRemoveBookmark,
            self.actionEditMetadata, 
            self.actionOpenExternalViewer,
            self.actionOpenExplorer,
            self.actionPreferences, 
            self.actionZoomIn,
            self.actionZoomOut,
            self.actionActualSize, 
            self.actionFitScreen,
            self.actionFitScreenHeight, 
            self.actionFitScreenWidth,
            self.actionFullScreen, 
            self.actionSlideshow,
            self.actionFirstImage,
            self.actionPreviousImage, 
            self.actionNextImage,
            self.actionLastImage,
            self.actionRefreshImage,
#           self.actionInfoDock, 
#           self.actionIconDock,
#           self.actionBrowserDock, 
#           self.actionDebugDock,
            self.actionNewTab, 
            self.actionRemoveTab,
            self.actionAbout,
            self.actionAboutQt ]
        font = QFont('Segoe UI', 9, QFont.Normal, False)
        for action in self.actionList:
            action.setFont(font)
            
    def getActionList(self):
        return self.actionList
        
    def loadSettings(self, actionList):
        settings = DefaultSettings()
        settings.setupDefaults()
        settings.beginGroup('shortcuts')
        for i in range(0, len(actionList) - 1):
            action = actionList[i]
            shortcut = settings.value(action.objectName())
            action.setShortcut(shortcut)
        settings.endGroup()
