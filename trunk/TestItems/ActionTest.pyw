from PyQt4.QtCore import *
from PyQt4.QtGui import *
from .Icons import SettingsIcons, IconSet
#from settings_default import DefaultSettings

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
        actionList = atc.actionList()

class ActionTestClass(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('ActionTestClass')
        
        actionList = []
        
        # File menu
        actionOpen = QAction(IconSet.Folder(), '&Open...', self)
        actionOpen.setObjectName('actionOpen')
        actionOpen.setAutoRepeat(False)
        actionOpen.setToolTip('Open a new image or folder')
        actionOpen.setData('Open File in Tab')
        
        actionClose = QAction(IconSet.Close(), '&Close', self)
        actionClose.setObjectName('actionClose')
        actionClose.setToolTip('Close the currently open file')
        actionClose.setData('Close File')
        
        actionPrint = QAction(IconSet.Print(), '&Print...', self)
        actionPrint.setObjectName('actionPrint')
        actionPrint.setToolTip('Print the currently displayed image')
        actionPrint.setData('Print Image')
        
        actionExit = QAction(IconSet.Exit(), 'E&xit', self)
        actionExit.setObjectName('actionExit')
        actionExit.setToolTip('Quit the image viewer')
        actionExit.setData('Exit Program')
        
        # Edit menu
        actionAddBookmark = QAction(IconSet.AddBookmark(), '&Add Bookmark...', self)
        actionAddBookmark.setObjectName('actionAddBookmark')
        actionAddBookmark.setEnabled(False)
        actionAddBookmark.setIconText('Bookmark')
        actionAddBookmark.setToolTip('Bookmark this folder')
        actionAddBookmark.setWhatsThis('Bookmarking a folder adds it to a list of folders for easy access in the future. To find your bookmarks, select Favorites from the dropdown box in the Browser Dock.')
        actionAddBookmark.setData('Add Bookmark')
        
        actionRemoveBookmark = QAction(IconSet.RemoveBookmark(), '&Remove Bookmark', self)
        actionRemoveBookmark.setObjectName('actionRemoveBookmark')
        actionRemoveBookmark.setAutoRepeat(False)
        actionRemoveBookmark.setData('Remove Bookmark')
        actionRemoveBookmark.setEnabled(False)
        actionRemoveBookmark.setIconText('UnBookmark')
        actionRemoveBookmark.setStatusTip('')
        actionRemoveBookmark.setToolTip('Remove a bookmark on this folder, if one exists')
        actionRemoveBookmark.setWhatsThis('This will remove the current folder from your bookmark list. This option is only available if the current folder is already in your bookmark list.')
        
        actionEditMetadata = QAction(IconSet.Metadata(), 'Edit &Metadata', self)
        actionEditMetadata.setObjectName('actionEditMetadata')
        actionEditMetadata.setIconText('Metadata')
        actionEditMetadata.setEnabled(False)
        actionEditMetadata.setToolTip('Modify the metadata stored in the current image')
        actionEditMetadata.setData('Edit Image Metadata')
        
        actionOpenExplorer = QAction(IconSet.WinLibrary(), 'Open in Windows &Explorer', self)
        actionOpenExplorer.setObjectName('actionOpenExplorer')
        actionOpenExplorer.setIconText('Explore')
        actionOpenExplorer.setToolTip('View the current folder in Windows Explorer')
        actionOpenExplorer.setEnabled(False)
        actionOpenExplorer.setData('Open Windows Explorer')
        
        actionOpenExternalViewer = QAction(IconSet.EditImage(), 'Open in External &Viewer', self)
        actionOpenExternalViewer.setObjectName('actionOpenExternalViewer')
        actionOpenExternalViewer.setIconText('External Viewer')
        actionOpenExternalViewer.setToolTip('Open the current image in an external viewer')
        actionOpenExternalViewer.setEnabled(False)
        actionOpenExternalViewer.setData('Open External Viewer')
        
        actionPreferences = QAction(IconSet.Preferences(), '&Preferences...', self)
        actionPreferences.setObjectName('actionPreferences')
        actionPreferences.setToolTip('Change how the program appears and behaves')
        actionPreferences.setData('Preferences')
       
        # View menu
        actionZoomIn = QAction(IconSet.ViewZoomIn(), 'Zoom &In', self)
        actionZoomIn.setObjectName('actionZoomIn')
        actionZoomIn.setToolTip('Increase the visible size of the current image')
        actionZoomIn.setData('Zoom In')
        
        
        actionZoomOut = QAction(IconSet.ViewZoomOut(), 'Zoom &Out', self)
        actionZoomOut.setObjectName('actionZoomOut')
        actionZoomOut.setToolTip('Make the current image appear smaller')
        actionZoomOut.setData('Zoom Out')
        
        
        actionActualSize = QAction(IconSet.ViewActualSize(), '&Actual Size', self)
        actionActualSize.setObjectName('actionActualSize')
        actionActualSize.setToolTip('View the current image at its actual size')
        actionActualSize.setData('View Image at Actual Size')
        
        
        actionFitScreen = QAction(IconSet.ViewFit(), '&Fit to Screen', self)
        actionFitScreen.setObjectName('actionFitScreen')
        actionFitScreen.setToolTip('Fit the current image within the available space of your screen')
        actionFitScreen.setIconText('Screen Fit')
        actionFitScreen.setData('Fit to Screen')
        
        
        actionFitScreenWidth = QAction(IconSet.ViewFitWidth(), 'Fit to Screen &Width', self)
        actionFitScreenWidth.setObjectName('actionFitScreenWidth')
        actionFitScreenWidth.setIconText('Width Fit')
        actionFitScreenWidth.setData('Fit to Screen Width')
        actionFitScreenWidth.setToolTip('Fit the image to the width of your screen')
        
        
        actionFitScreenHeight = QAction(IconSet.ViewFitHeight(), 'Fit to Screen &Height', self)
        actionFitScreenHeight.setObjectName('actionFitScreenHeight')
        actionFitScreenHeight.setIconText('Height Fit')
        actionFitScreenHeight.setData('Fit to Screen Height')
        actionFitScreenHeight.setToolTip('Fit the image within the height availabe on your screen')
        
        
        actionFullScreen = QAction(IconSet.ViewFullscreen(), 'F&ullscreen', self)
        actionFullScreen.setObjectName('actionFullScreen')
        actionFullScreen.setToolTip('Go to fullscreen mode; press F11 to exit')
        actionFullScreen.setData('Fullscreen Mode')
        actionFullScreen.setCheckable(True)
        

        actionSlideshow = QAction(IconSet.ViewSlideshow(), 'S&lideshow', self)
        actionSlideshow.setObjectName('actionSlideshow')
        actionSlideshow.setData('Slideshow Mode')
        actionSlideshow.setToolTip('Start a slideshow of the images in the current folder')
        
        
        actionPreviousImage = QAction(IconSet.ViewPrevious(), '&Previous Image', self)
        actionPreviousImage.setObjectName('actionPreviousImage')
        actionPreviousImage.setIconText('Previous')
        actionPreviousImage.setData('View Previous Image')
        actionPreviousImage.setToolTip('Go back to the previous image in the current folder')
        
        actionNextImage = QAction(IconSet.ViewNext(), '&Next Image', self)
        actionNextImage.setObjectName('actionNextImage')
        actionNextImage.setIconText('Next')
        actionNextImage.setData('View Next Image')
        actionNextImage.setToolTip('Go to the next image in the current folder')
        
        
        actionFirstImage = QAction(IconSet.ViewStart(), '&First Image', self)
        actionFirstImage.setObjectName('actionFirstImage')
        actionFirstImage.setIconText('First')
        actionFirstImage.setData('View First Image')
        actionFirstImage.setToolTip('Go to the first image in the current directory')
        
        actionLastImage = QAction(IconSet.ViewEnd(), '&Last Image', self)
        actionLastImage.setObjectName('actionLastImage')
        actionLastImage.setIconText('Last')
        actionLastImage.setToolTip('Go to the last image in the current folder')
        actionLastImage.setShortcut('PgUp')
        actionLastImage.setData('View Last Image')
        
        actionRefreshImage = QAction('&Reload', self)
        actionRefreshImage.setObjectName('actionRefreshImage')
        actionRefreshImage.setToolTip('Reload the currently displayed image')
        actionRefreshImage.setIcon(IconSet.ViewReload())
        actionRefreshImage.setShortcut('F5')
        actionRefreshImage.setData('Reload Image')

        #Window menu
        actionNewTab = QAction(IconSet.WindowNewTab(), '&New Tab', self)
        actionNewTab.setObjectName('actionNewTab')
        actionNewTab.setData('Open New Tab')
        actionNewTab.setShortcut('Ctrl+T')
        actionNewTab.setToolTip('Open a new tab for viewing images')
        
        actionRemoveTab = QAction(IconSet.WindowRemoveTab(), '&Close Tab', self)
        actionRemoveTab.setObjectName('actionRemoveTab')
        actionRemoveTab.setData('Close Tab')
        actionRemoveTab.setShortcut('Ctrl+F4')
        actionRemoveTab.setToolTip('Close the currently open tab')
        
#        actionInfoDock = QAction('&Image Info', self)
#        actionInfoDock.setObjectName('actionInfoDock')
#        actionInfoDock.setIcon(IconSet.ImageInfo())
#        actionInfoDock.setData('Toggle EXIF Data Dock')
#        actionInfoDock.setShortcut('I')
#        actionInfoDock.setToolTip('Open or close the image attribute display')
#        actionInfoDock.setCheckable(True)
        
#        actionIconDock = self.iconDock.toggleViewAction()
#        actionIconDock.setObjectName('actionIconDock')
#        actionIconDock.setText('&Thumbnail Viewer')
#        actionIconDock.setIcon(IconSet.WindowThumbnail())
#        actionIconDock.setIconText('Thumbnails')
#        actionIconDock.setToolTip('Open the thumbnail viewer')
#        actionIconDock.setData('Toggle Thumbnail Viewer')
#        actionIconDock.setShortcut('T')
#        actionIconDock.setCheckable(True)
#        
#        actionBrowserDock = self.browserDock.toggleViewAction()
#        actionBrowserDock.setObjectName('actionBrowserDock')
#        actionBrowserDock.setIcon(IconSet.WinPhotoFolder())
#        actionBrowserDock.setText('&Folder Browser')
#        actionBrowserDock.setIconText('Folders')
#        actionBrowserDock.setToolTip('Open or close the Folder Browser')
#        actionBrowserDock.setShortcut('D')
#        actionBrowserDock.setData('Toggle Folder Browser')
#        actionBrowserDock.setCheckable(True)
#        
#        actionDebugDock = self.debugDock.toggleViewAction()
#        actionDebugDock.setObjectName('actionDebugDock')
#        actionDebugDock.setIcon(IconSet.WindowDebugMode())
#        actionDebugDock.setText('&Debug Viewer')
#        actionDebugDock.setIconText('Debug')
#        actionDebugDock.setToolTip('Open the debug information window')
#        actionDebugDock.setData('Toggle Debug Dock')
#        actionDebugDock.setCheckable(True)


        # Help menu
        actionAbout = QAction(IconSet.Help(), '&About', self)
        actionAbout.setObjectName('actionAbout')
        actionAbout.setShortcut('F1')
        actionAbout.setData('About LIDS')
#        actionList.append[actionAbout]
        
        actionAboutQt = QAction(IconSet.QtLogo(), 'About &Qt', self)
        actionAboutQt.setObjectName('actionAboutQt')
        actionAboutQt.setShortcut('About Qt')
        
        #NOTE: This should contain ALL the registered actions. It's handy that way.
        self.__actionList = [ \
            actionOpen,
            actionClose,
            actionPrint,
            actionExit,
            actionAddBookmark,
            actionRemoveBookmark,
            actionEditMetadata, 
            actionOpenExternalViewer,
            actionOpenExplorer,
            actionPreferences, 
            actionZoomIn,
            actionZoomOut,
            actionActualSize, 
            actionFitScreen,
            actionFitScreenHeight, 
            actionFitScreenWidth,
            actionFullScreen, 
            actionSlideshow,
            actionFirstImage,
            actionPreviousImage, 
            actionNextImage,
            actionLastImage,
            actionRefreshImage,
            actionNewTab, 
            actionRemoveTab,
            actionAbout,
            actionAboutQt ]
            
        self.__actionDict = {\
            'Open' : actionOpen, 
            'Close' : actionClose, 
            'Print' : actionPrint, 
            'AddBookmark' : actionAddBookmark,
            'RemoveBookmark' :actionRemoveBookmark,
            'EditMetadata' : actionEditMetadata, 
            'ExternalViewer' : actionOpenExternalViewer,
            'OpenExplorer' : actionOpenExplorer,
            'Preferences' : actionPreferences, 
            'ZoomIn' : actionZoomIn,
            'ZoomOut' : actionZoomOut,
            'ActualSize' : actionActualSize, 
            'FitScreen' : actionFitScreen,
            'FitHeight' : actionFitScreenHeight, 
            'FitWidth' : actionFitScreenWidth,
            'FullScreen' : actionFullScreen, 
            'Slideshow' : actionSlideshow,
            'First' : actionFirstImage,
            'Previous' : actionPreviousImage, 
            'Next' : actionNextImage,
            'Last' : actionLastImage,
            'Refresh' : actionRefreshImage,
            'NewTab' : actionNewTab, 
            'RemoveTab' : actionRemoveTab,
            'About' : actionAbout,
            'AboutQt' : actionAboutQt}
            
    def actionList(self):
        return self.__actionList
        
    def actionDict(self):
        return self.__actionDict
