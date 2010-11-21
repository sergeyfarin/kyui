# -*- coding: utf-8 -*-

# Copyright (c) 2002 - 2010 Detlev Offenbach <detlev@die-offenbachs.de>
#

# The actions defined herein will be used as a test for KyRibbonBar
# -- JH

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from .Widgets.Action import KyAction


class E5ActionCreator():
    
    def initActions(target):
        iconCache = target.iconCache
        target.actions = []
        target.wizardsActions = []
        
        target.fileExitAct = KyAction(\
                parent=target, 
                iconText=target.tr('Quit'),
                icon=iconCache.icon("fileExit.png"),
                text=target.tr('&Quit'),
                shortcut=QKeySequence(target.tr("Ctrl+Q")),
                objectName='quit', 
                statusTip=target.tr('Quit the Eric5 IDE'))
        target.fileExitAct.setWhatsThis(target.tr(
            """<b>Quit the IDE</b>"""
            """<p>This quits the IDE. Any unsaved changes may be saved first."""
            """ Any Python program being debugged will be stopped and the"""
            """ preferences will be written to disc.</p>"""))
        target.actions.append(target.fileExitAct)
        
        target.editActions = []
        target.fileActions = []
        target.searchActions = []
        target.viewActions = []
        target.windowActions = []
        target.macroActions = []
        target.bookmarkActions = []
        target.spellingActions = []
        target.dbgActions = []
        target.utActions = []
        target.projectActions = []
        target.mpActions = []
        target.profileActions = []
        target.helpActions = []
        target.projActions = []
        target.prefActions = []
        target.toolActions = []
        
        
        target.actionSets = {
            'Bookmarks'  : target.bookmarkActions, 
            'Debug'     : target.dbgActions, 
            'Edit'      : target.editActions, 
            'File'      : target.fileActions,
            'Help'      : target.helpActions, 
            'Macro'     : target.macroActions, 
            'Multiproject' : target.mpActions,
            'Preferences'  : target.prefActions, 
            'Project'   : target.projActions, 
            'Search'    : target.searchActions, 
            'Spelling'  : target.spellingActions,
            'tools'     : target.toolActions, 
            'unittest'  : target.utActions , 
            'View'      : target.viewActions, 
            'Window'    : target.windowActions, 
        }
        
        E5ActionCreator.initBookmarkActions(target, iconCache)
        E5ActionCreator.initDebuggerActions(target, iconCache)
        E5ActionCreator.initEditActions(target, iconCache)
        E5ActionCreator.initFileActions(target, iconCache)
        E5ActionCreator.initMacroActions(target, iconCache)
        E5ActionCreator.initMultiprojectActions(target, iconCache)
        E5ActionCreator.initPluginActions(target, iconCache)
#        E5ActionCreator.initProfileActions(target, iconCache)
        E5ActionCreator.initProjectActions(target, iconCache)
        E5ActionCreator.initPreferenceActions(target, iconCache)
        E5ActionCreator.initSearchActions(target, iconCache)
        E5ActionCreator.initSpellingActions(target, iconCache)
        E5ActionCreator.initToolActions(target, iconCache)
        E5ActionCreator.initUnittestActions(target, iconCache)
        E5ActionCreator.initViewActions(target, iconCache)
        E5ActionCreator.initWindowActions(target, iconCache)
        
        E5ActionCreator.initHelpActions(target, iconCache)
        E5ActionCreator.initDocActions(target, iconCache)
    
    def initWindowActions(target, iconCache):

        target.viewProfileActGrp = QActionGroup(target)
        target.viewProfileActGrp.setObjectName("viewprofiles")
        target.viewProfileActGrp.setExclusive(True)
        
        target.setEditProfileAct = KyAction(\
                iconText=target.tr('Edit Profile'),
#                icon=iconCache.icon("viewProfileEdit.png"),
                text=target.tr('Edit Profile'),
                actionGroup=target.viewProfileActGrp,
                objectName='edit_profile',
                checkable=True, 
                statusTip=target.tr('Activate the edit view profile'))
        target.setEditProfileAct.setWhatsThis(target.tr(
            """<b>Edit Profile</b>"""
            """<p>Activate the "Edit View Profile". Windows being shown,"""
            """ if this profile is active, may be configured with the"""
            """ "View Profile Configuration" dialog.</p>"""))
        target.windowActions.append(target.setEditProfileAct)
        
        target.setDebugProfileAct = KyAction(\
                iconText=target.tr('Debug Profile'),
#                icon=iconCache.icon("viewProfileDebug.png"),
                text=target.tr('Debug Profile'),
                actionGroup=target.viewProfileActGrp, 
                objectName='debug_profile',
                checkable=True, 
                statusTip=target.tr('Activate the debug view profile'))
        target.setDebugProfileAct.setWhatsThis(target.tr(
            """<b>Debug Profile</b>"""
            """<p>Activate the "Debug View Profile". Windows being shown,"""
            """ if this profile is active, may be configured with the"""
            """ "View Profile Configuration" dialog.</p>"""))
        target.windowActions.append(target.setDebugProfileAct)
        
        target.pbAct = KyAction(\
                parent=target, 
                iconText=target.tr('Project Viewer'),
                text=target.tr('&Project-Viewer'), 
                objectName='project_viewer',
                shortcut=QKeySequence(target.tr("Alt+Shift+P")),
                checkable=True,
                statusTip=target.tr('Toggle the Project-Viewer window'))
        target.pbAct.setWhatsThis(target.tr(
            """<b>Toggle the Project-Viewer window</b>"""
            """<p>If the Project-Viewer window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.windowActions.append(target.pbAct)
        
        target.mpbAct = KyAction(\
                parent=target, 
                iconText=target.tr('Multiproject Viewer'), 
                text=target.tr('&Multiproject-Viewer'),
                objectName='multi_project_viewer', 
                shortcut=QKeySequence(target.tr("Alt+Shift+M")),
                checkable=True, 
                statusTip=target.tr('Toggle the Multiproject-Viewer window'), 
                whatsThis=target.tr(
            """<b>Toggle the Multiproject-Viewer window</b>"""
            """<p>If the Multiproject-Viewer window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.windowActions.append(target.mpbAct)
        
        target.debugViewerAct = KyAction( \
                parent=target, 
                iconText=target.tr('Debug Viewer'),
                text=target.tr('&Debug-Viewer'),
                shortcut=QKeySequence(target.tr("Alt+Shift+D")),
                objectName='debug_viewer',
                checkable=True, 
                statusTip=target.tr('Toggle the Debug-Viewer window'))
        target.debugViewerAct.setWhatsThis(target.tr(
            """<b>Toggle the Debug-Viewer window</b>"""
            """<p>If the Debug-Viewer window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.actions.append(target.debugViewerAct)

        target.shellAct = KyAction(parent=target, 
                iconText=target.tr('Shell'),
                text=target.tr('&Shell'),
                objectName='interpreter_shell',
                shortcut=QKeySequence(target.tr("Alt+Shift+S")), 
                checkable=True, 
                statusTip=target.tr('Toggle the Shell window'), 
                whatsThis=target.tr(
            """<b>Toggle the Shell window</b>"""
            """<p>If the Shell window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.windowActions.append(target.shellAct)

        target.terminalAct = KyAction(\
                parent=target, 
                iconText=target.tr('Terminal'),
                text=target.tr('Te&rminal'),
                objectName='terminal',
                shortcut=QKeySequence(target.tr("Alt+Shift+R")),
                checkable=True, 
                statusTip=target.tr('Toggle the Terminal window'), 
                whatsThis=target.tr(
            """<b>Toggle the Terminal window</b>"""
            """<p>If the Terminal window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.windowActions.append(target.terminalAct)

        target.browserAct = KyAction(\
                parent=target, 
                iconText=target.tr('File Browser'),
                text=target.tr('File &Browser'), 
                objectName='file_browser',
                shortcut=QKeySequence(target.tr("Alt+Shift+F")),
                checkable=True, 
                statusTip=target.tr('Toggle the File-Browser window'), 
                whatsThis=target.tr(
            """<b>Toggle the File-Browser window</b>"""
            """<p>If the File-Browser window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.windowActions.append(target.browserAct)

        target.logViewerAct = KyAction(\
                parent=target, 
                iconText=target.tr('Log Viewer'),
                text=target.tr('&Log-Viewer'), 
                objectName='log_viewer',
                checkable=True, 
                shortcut=QKeySequence(target.tr("Alt+Shift+G")),
                statusTip=target.tr('Toggle the Log-Viewer window'), 
                whatsThis=target.tr(
            """<b>Toggle the Log-Viewer window</b>"""
            """<p>If the Log-Viewer window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.windowActions.append(target.logViewerAct)

        target.taskViewerAct = KyAction(\
                parent=target, 
                iconText=target.tr('Task Viewer'),
                text=target.tr('T&ask-Viewer'),
                objectName='task_viewer',
                shortcut=QKeySequence(target.tr("Alt+Shift+T")),
                checkable=True, 
                statusTip=target.tr('Toggle the Task-Viewer window'), 
                whatsThis=target.tr(
            """<b>Toggle the Task-Viewer window</b>"""
            """<p>If the Task-Viewer window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.windowActions.append(target.taskViewerAct)

        target.templateViewerAct = KyAction(\
                parent=target,
                text=target.tr('Template Viewer'),
                iconText=target.tr('Temp&late-Viewer'),
                objectName='template_viewer',
                checkable=True, 
                shortcut=QKeySequence(target.tr("Alt+Shift+A")),
                statusTip=target.tr('Toggle the Template-Viewer window'), 
                whatsThis=target.tr(
            """<b>Toggle the Template-Viewer window</b>"""
            """<p>If the Template-Viewer window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.windowActions.append(target.templateViewerAct)

        target.vtAct = KyAction(\
                parent=target,
                iconText=target.tr('Vertical Toolbox'),
                text=target.tr('&Vertical Toolbox'),
                objectName='vertical_toolbox',
                checkable=True, 
                statusTip=target.tr('Toggle the Vertical Toolbox window'), 
                whatsThis=target.tr(
            """<b>Toggle the Vertical Toolbox window</b>"""
            """<p>If the Vertical Toolbox window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.windowActions.append(target.vtAct)
        
        target.htAct = KyAction(\
                parent=target,
                iconText=target.tr('Horizontal Toolbox'),
                text=target.tr('&Horizontal Toolbox'),
                objectName='horizontal_toolbox',
                checkable=True, 
                statusTip=target.tr('Toggle the Horizontal Toolbox window'), 
                whatsThis=target.tr(
            """<b>Toggle the Horizontal Toolbox window</b>"""
            """<p>If the Horizontal Toolbox window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.windowActions.append(target.htAct)
        
        target.lsbAct = KyAction(\
                parent=target,
                iconText=target.tr('Left Sidebar'),
                text=target.tr('&Left Sidebar'),
                objectName='left_sidebar',
                checkable=True, 
                statusTip=target.tr('Toggle the left sidebar window'))
        target.lsbAct.setWhatsThis(target.tr(
            """<b>Toggle the left sidebar window</b>"""
            """<p>If the left sidebar window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.windowActions.append(target.lsbAct)
        
        target.bsbAct = KyAction(\
                parent=target,
                iconText=target.tr('Bottom Sidebar'),
                text=target.tr('&Bottom Sidebar'),
                objectName='bottom_sidebar',
                checkable=True, 
                statusTip=target.tr('Toggle the bottom sidebar window'), 
                whatsThis=target.tr(
            """<b>Toggle the bottom sidebar window</b>"""
            """<p>If the bottom sidebar window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.windowActions.append(target.bsbAct)
        
        target.cooperationViewerAct = KyAction(\
                parent=target,
                iconText=target.tr('Cooperation'),
                text=target.tr('&Cooperation'),
                objectName='cooperation_viewer',
                shortcut=QKeySequence(target.tr("Alt+Shift+O")),
                checkable=True, 
                statusTip=target.tr('Toggle the Cooperation window'), 
                whatsThis=target.tr(
            """<b>Toggle the Cooperation window</b>"""
            """<p>If the Cooperation window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.windowActions.append(target.cooperationViewerAct)

    def initHelpActions(target, iconCache):

        target.whatsThisAct = KyAction(\
                parent=target,
                iconText=target.tr('What\'s This?'),
#                icon=iconCache.icon("whatsThis.png"),
                text=target.tr('&What\'s This?'), 
                shortcut=QKeySequence(target.tr("Shift+F1")),
                objectName='whatsThis', 
                statusTip=target.tr('Context sensitive help'), 
                whatsThis=target.tr(
            """<b>Display context sensitive help</b>"""
            """<p>In What's This? mode, the mouse cursor shows an arrow with a question"""
            """ mark, and you can click on the interface elements to get a short"""
            """ description of what they do and how to use them. In dialogs, this"""
            """ feature can be accessed using the context help button in the"""
            """ titlebar.</p>"""))
        target.helpActions.append(target.whatsThisAct)

        target.helpViewerAct = KyAction(\
                parent=target,
                iconText=target.tr('Helpviewer'),
                icon=iconCache.icon("helpViewer.png"),
                text=target.tr('&Helpviewer...'), 
                shortcut=QKeySequence(target.tr("F1")),
                objectName='helpviewer', 
                statusTip=target.tr('Open the helpviewer window'), 
                whatsThis=target.tr(
            """<b>Helpviewer</b>"""
            """<p>Display the eric5 web browser. This window will show"""
            """ HTML help files and help from Qt help collections. It has the"""
            """ capability to navigate to links, set bookmarks, print the displayed"""
            """ help and some more features. You may use it to browse the internet"""
            """ as well</p><p>If called with a word selected, this word is search"""
            """ in the Qt help collection.</p>"""))
        target.helpActions.append(target.helpViewerAct)
      
        target.versionAct = KyAction(\
                parent=target,
                text=target.tr('Versions'),
                iconText=target.tr('Show &Versions'),
                objectName='show_versions', 
                statusTip=target.tr('Display version information'), 
                whatsThis=target.tr(
            """<b>Show Versions</b>"""
            """<p>Display version information.</p>"""))
        target.helpActions.append(target.versionAct)

        target.checkUpdateAct = KyAction(\
                parent=target,
                iconText=target.tr('Updates'),
                text=target.tr('Check for &Updates...'),
                objectName='check_updates', 
                statusTip=target.tr('Check for Updates'))
        target.checkUpdateAct.setWhatsThis(target.tr(
            """<b>Check for Updates...</b>"""
            """<p>Checks the internet for updates of eric5.</p>"""))
        target.helpActions.append(target.checkUpdateAct)
    
        target.showVersionsAct = KyAction(parent=target,
                iconText=target.tr('Show downloadable versions'),
                text=target.tr('Show &downloadable versions...'), 
                objectName='show_downloadable_versions', 
                statusTip=target.tr('Show the versions available for download'))
        target.showVersionsAct.setWhatsThis(target.tr(
            """<b>Show downloadable versions...</b>"""
            """<p>Shows the eric5 versions available for download """
            """from the internet.</p>"""))
        target.helpActions.append(target.showVersionsAct)

        target.reportBugAct = KyAction(parent=target,
                iconText=target.tr('Report Bug'),
                text=target.tr('Report &Bug...'),
                objectName='report_bug',
                statusTip=target.tr('Report a bug'))
        target.reportBugAct.setWhatsThis(target.tr(
            """<b>Report Bug...</b>"""
            """<p>Opens a dialog to report a bug.</p>"""))
        target.helpActions.append(target.reportBugAct)
        
        target.requestFeatureAct = KyAction(parent=target,
                iconText=target.tr('Request Feature'),
                text=target.tr('Request &Feature...'),
                objectName='request_feature', 
                statusTip=target.tr('Send a feature request'))
        target.requestFeatureAct.setWhatsThis(target.tr(
            """<b>Request Feature...</b>"""
            """<p>Opens a dialog to send a feature request.</p>"""
                             ))
        target.helpActions.append(target.requestFeatureAct)
        
    def initUnittestActions(target, iconCache):

        target.utActGrp = QActionGroup(target)
        
        target.utDialogAct = KyAction(\
                iconText=target.tr('Unittest'), 
                icon=iconCache.icon("unittestRun.png"),
                text=target.tr('&Unittest...'),
                actionGroup=target.utActGrp,
                objectName='unittest', 
                statusTip=target.tr('Start unittest dialog'))
        target.utDialogAct.setWhatsThis(target.tr(
            """<b>Unittest</b>"""
            """<p>Perform unit tests. The dialog gives you the"""
            """ ability to select and run a unittest suite.</p>"""))
        target.utActions.append(target.utDialogAct)

        target.utRestartAct = KyAction(\
                iconText=target.tr('Restart Unittest'),
                icon=iconCache.icon("unittestRestart.png"),
                text=target.tr('&Restart Unittest...'),
                actionGroup=target.utActGrp,
                objectName='unittest_restart', 
                enabled=False, 
                statusTip=target.tr('Restart last unittest'))
        target.utRestartAct.setWhatsThis(target.tr(
            """<b>Restart Unittest</b>"""
            """<p>Restart the unittest performed last.</p>"""))
        target.utActions.append(target.utRestartAct)
        
        target.utScriptAct = KyAction(\
                iconText=target.tr('Unittest Script'),
                icon=iconCache.icon("unittestScript.png"),
                text=target.tr('Unittest &Script...'),
                actionGroup=target.utActGrp,
                objectName='unittest_script', 
                statusTip=target.tr('Run unittest with current script'), 
                enabled=False, 
                whatsThis=target.tr(
            """<b>Unittest Script</b>"""
            """<p>Run unittest with current script.</p>"""))
        target.utActions.append(target.utScriptAct)
        
        target.utProjectAct = KyAction(\
                iconText=target.tr('Unittest Project'),
                icon=iconCache.icon("unittestProject.png"),
                text=target.tr('Unittest &Project...'),
                actionGroup=target.utActGrp,
                objectName='unittest_project', 
                enabled=False, 
                statusTip=target.tr('Run unittest with current project'), 
                whatsThis=target.tr(
            """<b>Unittest Project</b>"""
            """<p>Run unittest with current project.</p>"""))
        target.utActions.append(target.utProjectAct)
        
    def initToolActions(target, iconCache):
        
        target.designerAct = KyAction(\
                parent=target, 
                toolTip=target.tr('QtDesigner'),
                iconText='Designer', 
                icon=iconCache.icon("toolsDesigner.png"),
                text=target.tr('Qt&Designer...'),
                objectName='qt_designer', 
                statusTip=target.tr('Start QtDesigner'))
        target.designerAct.setWhatsThis(target.tr(
            """<b>Qt-Designer 4</b>"""
            """<p>Start Qt-Designer 4.</p>"""))
        target.toolActions.append(target.designerAct)

        target.linguistAct = KyAction(\
                parent=target, 
                iconText=target.tr('Linguist'),
                icon=iconCache.icon("toolsLinguist.png"),
                text=target.tr('Qt&Linguist ...'),
                objectName='qt_linguist4', 
                statusTip=target.tr('Start QtLinguist'), 
                whatsThis=target.tr(
            """<b>Qt-Linguist 4</b>"""
            """<p>Start Qt-Linguist 4.</p>"""))
        target.toolActions.append(target.linguistAct)
    
        target.uiPreviewerAct = KyAction(\
                parent=target, 
                iconText=target.tr('UI Previewer'), 
                icon=iconCache.icon("mimeDesigner.png"),
                text=target.tr('&UI Previewer...'),
                objectName='ui_previewer', 
                statusTip=target.tr('Start the UI Previewer'), 
                whatsThis=target.tr(
            """<b>UI Previewer</b>"""
            """<p>Start the UI Previewer.</p>"""))
        target.toolActions.append(target.uiPreviewerAct)
        
        target.trPreviewerAct = KyAction(\
                parent=target,
                iconText=target.tr('Translations Previewer'), 
                icon=iconCache.icon("mimeLinguist.png"),
                text=target.tr('&Translations Previewer...'),
                objectName='tr_previewer', 
                statusTip=target.tr('Start the Translations Previewer'), 
                whatsThis=target.tr(
            """<b>Translations Previewer</b>"""
            """<p>Start the Translations Previewer.</p>"""))
        target.toolActions.append(target.trPreviewerAct)
        
        target.diffAct = KyAction(\
                parent=target,
                iconText=target.tr('Compare Files'),
#                icon=iconCache.icon("diffFiles.png"),
                text=target.tr('&Compare Files...'),
                objectName='diff_files', 
                statusTip=target.tr('Compare two files'), 
                whatsThis=target.tr(
            """<b>Compare Files</b>"""
            """<p>Open a dialog to compare two files.</p>"""))
        target.toolActions.append(target.diffAct)

        target.compareAct = KyAction(\
                parent=target,
                iconText=target.tr('Compare Files side by side'),
                icon=iconCache.icon("compareFiles.png"),
                text=target.tr('Compare Files &side by side...'), 
                objectName='compare_files', 
                statusTip=target.tr('Compare two files'), 
                whatsThis=target.tr(
            """<b>Compare Files side by side</b>"""
            """<p>Open a dialog to compare two files and show the result"""
            """ side by side.</p>"""))
        target.toolActions.append(target.compareAct)

        target.sqlBrowserAct = KyAction(\
                parent=target,
                iconText=target.tr('SQL Browser'),
#                icon=iconCache.icon("sqlBrowser.png"),
                text=target.tr('SQL &Browser...'), 
                objectName='sql_browser', 
                statusTip=target.tr('Browse a SQL database'), 
                whatsThis=target.tr(
            """<b>SQL Browser</b>"""
            """<p>Browse a SQL database.</p>"""))
        target.toolActions.append(target.sqlBrowserAct)

        target.miniEditorAct = KyAction(\
                parent=target,
                iconText=target.tr('Mini Editor'),
#                icon=iconCache.icon("editor.png"),
                text=target.tr('Mini &Editor...'), 
                objectName='mini_editor', 
                statusTip=target.tr('Mini Editor'), 
                whatsThis=target.tr(
            """<b>Mini Editor</b>"""
            """<p>Open a dialog with a simplified editor.</p>"""))
        target.toolActions.append(target.miniEditorAct)

        target.webBrowserAct = KyAction(\
                parent=target,
                iconText=target.tr('Web Browser'),
                icon=iconCache.icon("ericWeb.png"),
                text=target.tr('&Web Browser...'), 
                objectName='web_browser', 
                statusTip=target.tr('Start the eric5 Web Browser'), 
                whatsThis=target.tr(
            """<b>Web Browser</b>"""
            """<p>Browse the Internet with the eric5 Web Browser.</p>"""))
        target.toolActions.append(target.webBrowserAct)

        target.iconEditorAct = KyAction(\
                parent=target,
                iconText=target.tr('Icon Editor'),
#                icon=iconCache.icon("iconEditor.png"),
                text=target.tr('&Icon Editor...'), 
                objectName='icon_editor', 
                statusTip=target.tr('Start the eric5 Icon Editor'), 
                whatsThis=target.tr(
            """<b>Icon Editor</b>"""
            """<p>Starts the eric5 Icon Editor for editing simple icons.</p>"""))
        target.toolActions.append(target.iconEditorAct)
        
    def initPreferenceActions(target, iconCache):

        target.prefAct = KyAction(\
                parent=target,
                iconText=target.tr('Preferences'),
#                icon=iconCache.icon("configure.png"),
                text=target.tr('&Preferences...'),
                objectName='preferences', 
                statusTip=target.tr('Set the prefered configuration'))
        target.prefAct.setWhatsThis(target.tr(
            """<b>Preferences</b>"""
            """<p>Set the configuration items of the application"""
            """ with your prefered values.</p>"""))
        target.prefActions.append(target.prefAct)

        target.prefExportAct = KyAction(\
                parent=target,
                iconText=target.tr('Export Preferences'),
#                icon=iconCache.icon("configureExport.png"),
                text=target.tr('E&xport Preferences...'),
                objectName='export_preferences', 
                statusTip=target.tr('Export the current configuration'))
        target.prefExportAct.setWhatsThis(target.tr(
            """<b>Export Preferences</b>"""
            """<p>Export the current configuration to a file.</p>"""))
        target.prefActions.append(target.prefExportAct)

        target.prefImportAct = KyAction(\
                parent=target,
                iconText=target.tr('Import Preferences'),
#                icon=iconCache.icon("configureImport.png"),
                text=target.tr('I&mport Preferences...'),
                objectName='import_preferences', 
                statusTip=target.tr('Import a previously exported configuration'), 
                whatsThis=target.tr(
            """<b>Import Preferences</b>"""
            """<p>Import a previously exported configuration.</p>"""))
        target.prefActions.append(target.prefImportAct)

        target.reloadAPIsAct = KyAction(\
                parent=target,
                iconText=target.tr('Reload APIs'),
                text=target.tr('Reload &APIs'),
                objectName='reload_apis', 
                statusTip=target.tr('Reload the API information'), 
                whatsThis=target.tr(
            """<b>Reload APIs</b>"""
            """<p>Reload the API information.</p>"""))
        target.prefActions.append(target.reloadAPIsAct)

        target.showExternalToolsAct = KyAction(\
                parent=target,
                iconText=target.tr('External tools'),
#                icon=iconCache.icon("showPrograms.png"),
                text=target.tr('Show external &tools'),
                objectName='show_external_tools', 
                statusTip=target.tr('Reload the API information'), 
                whatsThis=target.tr(
            """<b>Show external tools</b>"""
            """<p>Opens a dialog to show the path and versions of all"""
            """ extenal tools used by eric5.</p>"""))
        target.prefActions.append(target.showExternalToolsAct)

        target.configViewProfilesAct = KyAction(\
                parent=target,
                iconText=target.tr('View Profiles'),
#                icon=iconCache.icon("configureViewProfiles.png"),
                text=target.tr('&View Profiles...'),
                objectName='view_profiles', 
                statusTip=target.tr('Configure view profiles'), 
                whatsThis=target.tr(
            """<b>View Profiles</b>"""
            """<p>Configure the view profiles. With this dialog you may"""
            """ set the visibility of the various windows for the predetermined"""
            """ view profiles.</p>"""))
        target.prefActions.append(target.configViewProfilesAct)

        target.configToolBarsAct = KyAction(\
                parent=target,
                iconText=target.tr('Toolbars'),
#                icon=iconCache.icon("toolbarsConfigure.png"),
                text=target.tr('Tool&bars...'),
                objectName='configure_toolbars', 
                statusTip=target.tr('Configure toolbars'), 
                whatsThis=target.tr(
            """<b>Toolbars</b>"""
            """<p>Configure the toolbars. With this dialog you may"""
            """ change the actions shown on the various toolbars and"""
            """ define your own toolbars.</p>"""))
        target.prefActions.append(target.configToolBarsAct)

        target.shortcutsAct = KyAction(\
                parent=target,
                iconText=target.tr('Keyboard Shortcuts'),
#                icon=iconCache.icon("configureShortcuts.png"),
                text=target.tr('Keyboard &Shortcuts...'),
                objectName='keyboard_shortcuts', 
                statusTip=target.tr('Set the keyboard shortcuts'), 
                whatsThis=target.tr(
            """<b>Keyboard Shortcuts</b>"""
            """<p>Set the keyboard shortcuts of the application"""
            """ with your prefered values.</p>"""))
        target.prefActions.append(target.shortcutsAct)

        target.exportShortcutsAct = KyAction(\
                parent=target,
                iconText=target.tr('Export Keyboard Shortcuts'),
#                icon=iconCache.icon("exportShortcuts.png"),
                text=target.tr('&Export Keyboard Shortcuts...'),
                objectName='export_keyboard_shortcuts', 
                statusTip=target.tr('Export the keyboard shortcuts'), 
                whatsThis=target.tr(
            """<b>Export Keyboard Shortcuts</b>"""
            """<p>Export the keyboard shortcuts of the application.</p>"""))
        target.prefActions.append(target.exportShortcutsAct)

        target.importShortcutsAct = KyAction(\
                parent=target,
                iconText=target.tr('Import Keyboard Shortcuts'),
#                icon=iconCache.icon("importShortcuts.png"),
                text=target.tr('&Import Keyboard Shortcuts...'),
                objectName='import_keyboard_shortcuts', 
                statusTip=target.tr('Import the keyboard shortcuts'))
        target.importShortcutsAct.setWhatsThis(target.tr(
            """<b>Import Keyboard Shortcuts</b>"""
            """<p>Import the keyboard shortcuts of the application.</p>"""))
        target.prefActions.append(target.importShortcutsAct)
        
    def initPluginActions(target, iconCache):
        
        target.pluginInfoAct = KyAction(parent=target,
                iconText=target.tr('Plugins'),
#                icon=iconCache.icon("plugin.png"),
                text=target.tr('&Plugins...'), 
                objectName='plugin_infos', 
                statusTip=target.tr('Show Plugin Infos'))
        target.pluginInfoAct.setWhatsThis(target.tr(
            """<b>Plugin Infos...</b>"""
            """<p>This opens a dialog, that show some information about"""
            """ loaded plugins.</p>"""))
        target.prefActions.append(target.pluginInfoAct)
        
        target.pluginInstallAct = KyAction(parent=target,
                iconText=target.tr('Install Plugins'),
#                icon=iconCache.icon("pluginInstall.png"),
                text=target.tr('&Install Plugins...'),
                objectName='plugin_install', 
                statusTip=target.tr('Install Plugins'))
        target.pluginInstallAct.setWhatsThis(target.tr(
            """<b>Install Plugins...</b>"""
            """<p>This opens a dialog to install or update plugins.</p>"""))
        target.prefActions.append(target.pluginInstallAct)
        
        target.pluginDeinstallAct = KyAction(parent=target,
                iconText=target.tr('Uninstall Plugin'),
#                icon=iconCache.icon("pluginUninstall.png"),
                text=target.tr('&Uninstall Plugin...'),
                objectName='plugin_deinstall', 
                statusTip=target.tr('Uninstall Plugin'))
        target.pluginDeinstallAct.setWhatsThis(target.tr(
            """<b>Uninstall Plugin...</b>"""
            """<p>This opens a dialog to uninstall a plugin.</p>"""))
        target.prefActions.append(target.pluginDeinstallAct)

        target.pluginRepoAct = KyAction(parent=target,
                iconText=target.tr('Plugin Repository'),
#                icon=iconCache.icon("pluginRepository.png"),
                text=target.tr('Plugin &Repository...'),
                objectName='plugin_repository', 
                statusTip=target.tr('Show Plugins available for download'))
        target.pluginRepoAct.setWhatsThis(target.tr(
            """<b>Plugin Repository...</b>"""
            """<p>This opens a dialog, that shows a list of plugins """
            """available on the Internet.</p>"""))
        target.prefActions.append(target.pluginRepoAct)
        
    
    def initDocActions(target, iconCache):

        target.qt4DocAct = KyAction(parent=target, 
                iconText=target.tr('Qt4'),
                icon=iconCache.icon("docQt.png"),
                toolTip=target.tr('Qt4 Documentation'), 
                text=target.tr('Qt&4 Documentation'),
                objectName='qt4_documentation', 
                statusTip=target.tr('Open Qt4 Documentation'))
        target.qt4DocAct.setWhatsThis(target.tr(
            """<b>Qt4 Documentation</b>"""
            """<p>Display the Qt4 Documentation. Dependant upon your settings, this"""
            """ will either show the help in Eric's internal help viewer, or execute"""
            """ a web browser or Qt Assistant. </p>"""))
        target.helpActions.append(target.qt4DocAct)
      
        target.pyqt4DocAct = KyAction(parent=target, 
                iconText=target.tr('PyQt4'),
                icon=iconCache.icon("docPyQt.png"),
                text=target.tr('P&yQt4 Documentation'), 
                toolTip=target.tr('PyQt4 Documentation'), 
                objectName='pyqt4_documentation', 
                statusTip=target.tr('Open PyQt4 Documentation'))
        target.pyqt4DocAct.setWhatsThis(target.tr(
            """<b>PyQt4 Documentation</b>"""
            """<p>Display the PyQt4 Documentation. Dependant upon your settings, this"""
            """ will either show the help in Eric's internal help viewer, or execute"""
            """ a web browser or Qt Assistant. </p>"""))
        target.helpActions.append(target.pyqt4DocAct)
        
        target.pythonDocAct = KyAction(parent=target, 
                iconText=target.tr('Python'), 
                icon=iconCache.icon("docPython.png"),
                toolTip=target.tr('Python Documentation'),
                text=target.tr('&Python Documentation'), 
                objectName='python_documentation', 
                statusTip=target.tr('Open Python Documentation'))
        target.pythonDocAct.setWhatsThis(target.tr(
            """<b>Python Documentation</b>"""
            """<p>Display the python documentation."""
            """ If no documentation directory is configured,"""
            """ the location of the python documentation is assumed to be the doc"""
            """ directory underneath the location of the python executable on"""
            """ Windows and <i>/usr/share/doc/packages/python/html</i> on Unix."""
            """ Set PYTHONDOCDIR in your environment to override this. </p>"""))
        target.helpActions.append(target.pythonDocAct)
        
        target.ericDocAct = KyAction(parent=target, 
                toolTip=target.tr("Eric API Documentation"),
                iconText='Eric API', 
                icon=iconCache.icon("docEric.png"),
                text=target.tr('&Eric API Documentation'),
                objectName='eric_documentation', 
                statusTip=target.tr("Open Eric API Documentation"))
        target.ericDocAct.setWhatsThis(target.tr(
            """<b>Eric API Documentation</b>"""
            """<p>Display the Eric API documentation."""
            """ The location for the documentation is the Documentation/Source"""
            """ subdirectory of the eric5 installation directory.</p>"""))
        target.helpActions.append(target.ericDocAct)
        
        target.pysideDocAct = KyAction(parent=target,
                iconText=target.tr('PySide Documentation'),
                icon=iconCache.icon("docPySide.png"),
                text=target.tr('Py&Side Documentation'),
                objectName='pyside_documentation', 
                statusTip=target.tr('Open PySide Documentation'), 
                whatsThis=target.tr(
            """<b>PySide Documentation</b>"""
            """<p>Display the PySide Documentation. Dependant upon your settings, """
            """this will either show the help in Eric's internal help viewer, or """
            """execute a web browser or Qt Assistant. </p>"""
        ))
        target.helpActions.append(target.pysideDocAct)
    
    def initFileActions(target, iconCache):
        """
        Private method defining the user interface actions for file handling.
        """
        target.newAct = KyAction(\
                parent=target, 
                iconText=target.tr('New', 'ViewManager'),
                icon=target.iconCache.icon("fileNew.png"),
                text=target.tr('&New', 'ViewManager'),
                shortcut=QKeySequence(target.tr("Ctrl+N", "File|New")),
                objectName='vm_file_new', 
                statusTip=target.tr('Open an empty editor window', 'ViewManager'), 
                whatsThis=target.tr(
            """<b>New</b>"""
            """<p>An empty editor window will be created.</p>"""))
        target.fileActions.append(target.newAct)
        
        target.openAct = KyAction(parent=target,
                iconText=target.tr('Open'),
                icon=target.iconCache.icon("fileOpen.png"),
                text=target.tr('&Open...'),
                shortcut=QKeySequence(target.tr("Ctrl+O", "File|Open")), 
                objectName='vm_file_open', 
                statusTip=target.tr('Open a file'), 
                whatsThis=target.tr(
            """<b>Open a file</b>"""
            """<p>You will be asked for the name of a file to be opened"""
            """ in an editor window.</p>"""))
        target.fileActions.append(target.openAct)
        
        target.closeActGrp = QActionGroup(target)
        
        target.closeAct = KyAction(\
                actionGroup=target.closeActGrp, 
                iconText=target.tr('Close'),
                icon=target.iconCache.icon("fileClose.png"),
                text=target.tr('&Close'),
                shortcut=QKeySequence(target.tr("Ctrl+W", "File|Close")), 
                objectName='vm_file_close', 
                statusTip=target.tr('Close the current window'))
        target.closeAct.setWhatsThis(target.tr(
            """<b>Close Window</b>"""
            """<p>Close the current window.</p>"""))
        target.fileActions.append(target.closeAct)
        
        target.closeAllAct = KyAction(\
                iconText=target.tr('Close All'),
                text=target.tr('Clos&e All'),
                actionGroup=target.closeActGrp, 
                objectName='vm_file_close_all', 
                statusTip=target.tr('Close all editor windows'))
        target.closeAllAct.setWhatsThis(target.tr(
            """<b>Close All Windows</b>"""
            """<p>Close all editor windows.</p>"""))
        target.fileActions.append(target.closeAllAct)
        
        target.closeActGrp.setEnabled(False)
        
        target.saveActGrp = QActionGroup(target)
        
        target.saveAct = KyAction(\
                iconText=target.tr('Save'),
                icon=target.iconCache.icon("fileSave.png"),
                text=target.tr('&Save'),
                shortcut=QKeySequence(target.tr("Ctrl+S", "File|Save")), 
                actionGroup=target.saveActGrp, 
                objectName='vm_file_save', 
                statusTip=target.tr('Save the current file'))
        target.saveAct.setWhatsThis(target.tr(
            """<b>Save File</b>"""
            """<p>Save the contents of current editor window.</p>"""))
        target.fileActions.append(target.saveAct)
        
        target.saveAsAct = KyAction(\
                iconText=target.tr('Save As'),
                icon=target.iconCache.icon("fileSaveAs.png"),
                text=target.tr('Save &as...'),
                shortcut=QKeySequence(target.tr("Shift+Ctrl+S", "File|Save As")), 
                actionGroup=target.saveActGrp, 
                objectName='vm_file_save_as', 
                statusTip=target.tr(
                        'Save the current file to a new one'))
        target.saveAsAct.setWhatsThis(target.tr(
            """<b>Save File as</b>"""
            """<p>Save the contents of current editor window to a new file."""
            """ The file can be entered in a file selection dialog.</p>"""))
        target.fileActions.append(target.saveAsAct)
        
        target.saveAllAct = KyAction(\
                iconText=target.tr('Save All'),
                icon=target.iconCache.icon("fileSaveAll.png"),
                text=target.tr('Save a&ll...'),
                actionGroup=target.saveActGrp, 
                objectName='vm_file_save_all', 
                statusTip=target.tr('Save all files'))
        target.saveAllAct.setWhatsThis(target.tr(
            """<b>Save All Files</b>"""
            """<p>Save the contents of all editor windows.</p>"""))
        target.fileActions.append(target.saveAllAct)
        
        target.saveActGrp.setEnabled(False)

        target.saveToProjectAct = KyAction(\
                parent=target, 
                iconText=target.tr('Save to Project'),
#                icon=target.iconCache.icon("fileSaveToProject.png"),
                text=target.tr('Save to Pro&ject'),
                objectName='vm_file_save_to_project', 
                statusTip=target.tr(
                    'Save the current file to the current project'), 
                enabled=False, 
                whatsThis=target.tr(
            """<b>Save to Project</b>"""
            """<p>Save the contents of the current editor window to the"""
            """ current project. After the file has been saved, it is"""
            """ automatically added to the current project.</p>"""))
        target.fileActions.append(target.saveToProjectAct)
        
        target.printAct = KyAction(\
                parent=target, 
                iconText=target.tr('Print'),
                icon=target.iconCache.icon("filePrint.png"),
                text=target.tr('&Print'),
                shortcut=QKeySequence(target.tr("Ctrl+P", "File|Print")), 
                objectName='vm_file_print', 
                statusTip=target.tr('Print the current file'), 
                whatsThis=target.tr(
            """<b>Print File</b>"""
            """<p>Print the contents of current editor window.</p>"""))
        
        target.fileActions.append(target.printAct)
        
        target.printPreviewAct = KyAction(\
                parent=target, 
                iconText=target.tr('Print Preview'),
#                icon=target.iconCache.icon("printPreview.png"),
                text=target.tr('Print Preview'),
                objectName='vm_file_print_preview', 
                statusTip=target.tr('Print preview of the current file'), 
                whatsThis=target.tr(
            """<b>Print Preview</b>"""
            """<p>Print preview of the current editor window.</p>"""))
        
        target.fileActions.append(target.printPreviewAct)
        
        target.findFileNameAct = KyAction(\
                parent=target, 
                iconText=target.tr('Search File'),
                icon=target.iconCache.icon("fileFind.png"),
                text=target.tr('Search &File...'),
                shortcut=QKeySequence(target.tr("Alt+Ctrl+F", "File|Search File")), 
                objectName='vm_file_search_file', 
                statusTip=target.tr('Search for a file'), 
                whatsThis=target.tr(
            """<b>Search File</b>"""
            """<p>Search for a file.</p>"""))
        target.fileActions.append(target.findFileNameAct)
        
#        target.printAct.setEnabled(False)
#        target.printPreviewAct.setEnabled(False)
        
    def initEditActions(target, iconCache):
        """
        Private method defining the user interface actions for the edit commands.
        """
        target.editActGrp = QActionGroup(target)
        target.changesActGrp = QActionGroup(target)
        target.clipActGrp = QActionGroup(target)
        target.indentActGrp = QActionGroup(target)
        
        target.autoCompleteMenu = QMenu()
        target.commentMenu = QMenu()
        
        target.undoAct = KyAction(\
                iconText=target.tr('Undo'),
                icon=target.iconCache.icon("editUndo.png"),
                text=target.tr('&Undo'),
                shortcut=QKeySequence(target.tr("Ctrl+Z", "Edit|Undo")), 
                shortcut2=QKeySequence(target.tr("Alt+Backspace", "Edit|Undo")), 
                actionGroup=target.changesActGrp, 
                objectName='vm_edit_undo', 
                statusTip=target.tr('Undo the last change'))
        target.undoAct.setWhatsThis(target.tr(
            """<b>Undo</b>"""
            """<p>Undo the last change done in the current editor.</p>"""))
        target.editActions.append(target.undoAct)
        
        target.redoAct = KyAction( \
                iconText=target.tr('Redo'),
                icon=target.iconCache.icon("editRedo.png"),
                text=target.tr('&Redo'),
                shortcut=QKeySequence(target.tr("Ctrl+Shift+Z", "Edit|Redo")), 
                actionGroup=target.changesActGrp, 
                objectName='vm_edit_redo', 
                statusTip=target.tr('Redo the last change'))
        target.redoAct.setWhatsThis(target.tr(
            """<b>Redo</b>"""
            """<p>Redo the last change done in the current editor.</p>"""))
        target.editActions.append(target.redoAct)
        
        target.revertAct = KyAction(\
                iconText=target.tr('Revert'),
                icon=target.iconCache.icon("editRevert.png"),
                text=target.tr('Re&vert to last saved state'),
                shortcut=QKeySequence(target.tr("Ctrl+Y", "Edit|Revert")), 
                actionGroup=target.changesActGrp, 
                objectName='vm_edit_revert', 
                statusTip=target.tr('Revert to last saved state'))
        target.revertAct.setWhatsThis(target.tr(
            """<b>Revert to last saved state</b>"""
            """<p>Undo all changes up to the last saved state"""
            """ of the current editor.</p>"""))
        target.editActions.append(target.revertAct)
        
        
        target.cutAct = KyAction(\
                iconText=target.tr('Cut'),
                icon=target.iconCache.icon("editCut.png"),
                text=target.tr('Cu&t'),
                shortcut=QKeySequence(target.tr("Ctrl+X", "Edit|Cut")),
                shortcut2=QKeySequence(target.tr("Shift+Del", "Edit|Cut")),
                actionGroup=target.clipActGrp, 
                objectName='vm_edit_cut', 
                statusTip=target.tr('Cut the selection'))
        target.cutAct.setWhatsThis(target.tr(
            """<b>Cut</b>"""
            """<p>Cut the selected text of the current editor to the clipboard.</p>"""))
        target.editActions.append(target.cutAct)
        
        target.copyAct = KyAction(\
                iconText=target.tr('Copy'),
                icon=target.iconCache.icon("editCopy.png"),
                text=target.tr('&Copy'),
                shortcut=QKeySequence(target.tr("Ctrl+C", "Edit|Copy")), 
                shortcut2=QKeySequence(target.tr("Ctrl+Ins", "Edit|Copy")), 
                actionGroup=target.clipActGrp, 
                objectName='vm_edit_copy', 
                statusTip=target.tr('Copy the selection'))
        target.copyAct.setWhatsThis(target.tr(
            """<b>Copy</b>"""
            """<p>Copy the selected text of the current editor to the clipboard.</p>"""))
        target.editActions.append(target.copyAct)
        
        target.pasteAct = KyAction(\
                iconText=target.tr('Paste'),
                icon=target.iconCache.icon("editPaste.png"),
                text=target.tr('&Paste'),
                shortcut=QKeySequence(target.tr("Ctrl+V", "Edit|Paste")), 
                shortcut2=QKeySequence(target.tr("Shift+Ins", "Edit|Paste")), 
                actionGroup=target.clipActGrp, 
                objectName='vm_edit_paste', 
                statusTip=target.tr('Paste the last cut/copied text'))
        target.pasteAct.setWhatsThis(target.tr(
            """<b>Paste</b>"""
            """<p>Paste the last cut/copied text from the clipboard to"""
            """ the current editor.</p>"""))
        target.editActions.append(target.pasteAct)
        
        target.deleteAct = KyAction(\
                iconText=target.tr('Clear'),
                icon=target.iconCache.icon("editDelete.png"),
                text=target.tr('Cl&ear'),
                shortcut=QKeySequence(target.tr("Alt+Shift+C", "Edit|Clear")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_clear', 
                statusTip=target.tr('Clear all text'))
        target.deleteAct.setWhatsThis(target.tr(
            """<b>Clear</b>"""
            """<p>Delete all text of the current editor.</p>"""))
        target.editActions.append(target.deleteAct)
        
        target.indentAct = KyAction(\
                iconText=target.tr('Indent'),
#                icon=target.iconCache.icon("editIndent.png"),
                text=target.tr('&Indent'),
                shortcut=QKeySequence(target.tr("Ctrl+I", "Edit|Indent")), 
                actionGroup=target.indentActGrp, 
                objectName='vm_edit_indent', 
                statusTip=target.tr('Indent line'))
        target.indentAct.setWhatsThis(target.tr(
            """<b>Indent</b>"""
            """<p>Indents the current line or the lines of the"""
            """ selection by one level.</p>"""))
        target.editActions.append(target.indentAct)
        
        target.unindentAct = KyAction(\
                iconText=target.tr('Unindent'),
#                icon=target.iconCache.icon("editUnindent.png"),
                text=target.tr('U&nindent'),
                shortcut=QKeySequence(target.tr("Ctrl+Shift+I", "Edit|Unindent")), 
                actionGroup=target.indentActGrp, 
                objectName='vm_edit_unindent', 
                statusTip=target.tr('Unindent line'))
        target.unindentAct.setWhatsThis(target.tr(
            """<b>Unindent</b>"""
            """<p>Unindents the current line or the lines of the"""
            """ selection by one level.</p>"""))
        target.editActions.append(target.unindentAct)
        
        target.smartIndentAct = KyAction(\
                iconText=target.tr('Smart indent'),
#                icon=target.iconCache.icon("editSmartIndent.png"),
                text=target.tr('Smart indent'),
                shortcut=QKeySequence(target.tr("Ctrl+Alt+I", "Edit|Smart indent")), 
                actionGroup=target.indentActGrp, 
                objectName='vm_edit_smart_indent', 
                statusTip=target.tr('Smart indent Line or Selection'))
        target.smartIndentAct.setWhatsThis(target.tr(
            """<b>Smart indent</b>"""
            """<p>Indents the current line or the lines of the"""
            """ current selection smartly.</p>"""))
        target.editActions.append(target.smartIndentAct)
        
        target.commentAct = KyAction(\
                iconText=target.tr('Comment'),
                icon=target.iconCache.icon("editComment.png"),
                text=target.tr('C&omment'),
                shortcut=QKeySequence(target.tr("Ctrl+M", "Edit|Comment")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_comment', 
                statusTip=target.tr('Comment Line or Selection'))
        target.commentAct.setWhatsThis(target.tr(
            """<b>Comment</b>"""
            """<p>Comments the current line or the lines of the"""
            """ current selection.</p>"""))
        target.editActions.append(target.commentAct)
        
        target.uncommentAct = KyAction(\
                iconText=target.tr('Uncomment'),
                icon=target.iconCache.icon("editUncomment.png"),
                text=target.tr('Unco&mment'),
                shortcut=QKeySequence(target.tr("Alt+Ctrl+M", "Edit|Uncomment")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_uncomment', 
                statusTip=target.tr('Uncomment Line or Selection'))
        target.uncommentAct.setWhatsThis(target.tr(
            """<b>Uncomment</b>"""
            """<p>Uncomments the current line or the lines of the"""
            """ current selection.</p>"""))
        target.editActions.append(target.uncommentAct)
        
        target.streamCommentAct = KyAction(\
                iconText=target.tr('Stream Comment'),
                icon=target.iconCache.icon("editStreamComment.png"), 
                text=target.tr('Stream Comment'),
                actionGroup=target.editActGrp, 
                objectName='vm_edit_stream_comment', 
                statusTip=target.tr(
                        'Stream Comment Line or Selection'))
        target.streamCommentAct.setWhatsThis(target.tr(
            """<b>Stream Comment</b>"""
            """<p>Stream comments the current line or the current selection.</p>"""))
        target.editActions.append(target.streamCommentAct)
        
        target.boxCommentAct = KyAction(\
                iconText=target.tr('Box Comment'),
                text=target.tr('Box Comment'),
                actionGroup=target.editActGrp, 
                objectName='vm_edit_box_comment', 
                statusTip=target.tr('Box Comment Line or Selection'))
        target.boxCommentAct.setWhatsThis(target.tr(
            """<b>Box Comment</b>"""
            """<p>Box comments the current line or the lines of the"""
            """ current selection.</p>"""))
        target.editActions.append(target.boxCommentAct)
        
        target.selectBraceAct = KyAction(\
                iconText=target.tr('Select to brace'),
                text=target.tr('Select to &brace'),
                shortcut=QKeySequence(target.tr("Ctrl+E", "Edit|Select to brace")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_select_to_brace', 
                statusTip=target.tr(
                        'Select text to the matching brace'))
        target.selectBraceAct.setWhatsThis(target.tr(
            """<b>Select to brace</b>"""
            """<p>Select text of the current editor to the matching brace.</p>"""))
        target.editActions.append(target.selectBraceAct)
        
        target.selectAllAct = KyAction(\
                iconText=target.tr('Select all'),
                text=target.tr('&Select all'),
                shortcut=QKeySequence(target.tr("Ctrl+A", "Edit|Select all")), 
                actionGroup=target.editActGrp,
                objectName='vm_edit_select_all', 
                statusTip=target.tr('Select all text'))
        target.selectAllAct.setWhatsThis(target.tr(
            """<b>Select All</b>"""
            """<p>Select all text of the current editor.</p>"""))
        target.editActions.append(target.selectAllAct)
        
        target.deselectAllAct = KyAction(\
                iconText=target.tr('Deselect all'),
                text=target.tr('&Deselect all'),
                shortcut=QKeySequence(target.tr("Alt+Ctrl+A", "Edit|Deselect all")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_deselect_all', 
                statusTip=target.tr('Deselect all text'))
        target.deselectAllAct.setWhatsThis(target.tr(
            """<b>Deselect All</b>"""
            """<p>Deselect all text of the current editor.</p>"""))
        target.editActions.append(target.deselectAllAct)
        
        target.convertEOLAct = KyAction(\
                iconText=target.tr('Convert EOL Characters'),
                text=target.tr('Convert EO&L Characters'),
                actionGroup=target.editActGrp, 
                objectName='vm_edit_convert_eol', 
                statusTip=target.tr('Convert Line End Characters'))
        target.convertEOLAct.setWhatsThis(target.tr(
            """<b>Convert Line End Characters</b>"""
            """<p>Convert the line end characters to the currently set type.</p>"""))
        target.editActions.append(target.convertEOLAct)
        
        target.shortenEmptyAct = KyAction(\
                iconText=target.tr('Shorten empty lines'),
                text=target.tr('Shorten empty lines'),
                actionGroup=target.editActGrp, 
                objectName='vm_edit_shorten_empty_lines', 
                statusTip=target.tr('Shorten empty lines'))
        target.shortenEmptyAct.setWhatsThis(target.tr(
            """<b>Shorten empty lines</b>"""
            """<p>Shorten lines consisting solely of whitespace characters.</p>"""))
        target.editActions.append(target.shortenEmptyAct)
        
        target.autoCompleteAct = KyAction(\
                iconText=target.tr('Autocomplete'),
                icon=target.iconCache.icon("editAutocomplete.png"),
                text=target.tr('&Autocomplete'),
                shortcut=QKeySequence(target.tr("Ctrl+Space", "Edit|Autocomplete")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_autocomplete', 
                statusTip=target.tr('Autocomplete current word'), 
                whatsThis=target.tr(
            """<b>Autocomplete</b>"""
            """<p>Performs an autocompletion of the word containing the cursor.</p>"""))
        target.editActions.append(target.autoCompleteAct)
        
        target.autoCompleteFromDocAct = KyAction(\
                iconText=target.tr('Autocomplete from Document'),
                text=target.tr('Autocomplete from Document'),
                shortcut=QKeySequence(target.tr(
                        "Ctrl+Shift+Space", "Edit|Autocomplete from Document")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_autocomplete_from_document', 
                statusTip=target.tr(
                        'Autocomplete current word from Document'), 
                whatsThis=target.tr(
            """<b>Autocomplete from Document</b>"""
            """<p>Performs an autocompletion from document of the word"""
            """ containing the cursor.</p>"""))
        target.editActions.append(target.autoCompleteFromDocAct)
        
        target.autoCompleteFromAPIsAct = KyAction(\
                iconText=target.tr('Autocomplete from APIs'),
                text=target.tr('Autocomplete from APIs'),
                shortcut=QKeySequence(target.tr(
                        "Ctrl+Alt+Space", 'Edit|Autocomplete from APIs')), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_autocomplete_from_api', 
                statusTip=target.tr(
                        'Autocomplete current word from APIs'), 
                whatsThis=target.tr(
            """<b>Autocomplete from APIs</b>"""
            """<p>Performs an autocompletion from APIs of the word containing"""
            """ the cursor.</p>"""))
        target.editActions.append(target.autoCompleteFromAPIsAct)
        
        target.autoCompleteFromAllAct = KyAction(\
                iconText=target.tr('Autocomplete from All'),
                text=target.tr('Autocomplete from All'),
                shortcut=QKeySequence(target.tr(
                        "Alt+Shift+Space", "Edit|Autocomplete from All")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_autocomplete_from_all', 
                statusTip=target.tr(
                        'Autocomplete current word from Document and APIs'), 
                whatsThis=target.tr(
            """<b>Autocomplete from Document and APIs</b>"""
            """<p>Performs an autocompletion from document and APIs"""
            """ of the word containing the cursor.</p>"""))
        target.editActions.append(target.autoCompleteFromAllAct)
        
        target.calltipsAct = KyAction(\
                iconText=target.tr('Calltip'),
                text=target.tr('&Calltip'),
                shortcut=QKeySequence(target.tr("Alt+Space", "Edit|Calltip")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_calltip', 
                statusTip=target.tr('Show Calltips'), 
                whatsThis=target.tr(
            """<b>Calltip</b>"""
            """<p>Show calltips based on the characters immediately to the"""
            """ left of the cursor.</p>"""))
        target.editActions.append(target.calltipsAct)
        
#        target.editActGrp.setEnabled(False)
#        target.copyActGrp.setEnabled(False)
        
    def initSearchActions(target, iconCache):
        """
        Private method defining the user interface actions for the search commands.
        """
        target.searchActGrp = QActionGroup(target)
        
        target.searchAct = KyAction(\
                iconText=target.tr('Search'),
                icon=target.iconCache.icon("find.png"),
                text=target.tr('&Search...'),
                shortcut=QKeySequence(target.tr("Ctrl+F", "Search|Search")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_search', 
                statusTip=target.tr('Search for a text'), 
                whatsThis=target.tr(
            """<b>Search</b>"""
            """<p>Search for some text in the current editor. A"""
            """ dialog is shown to enter the searchtext and options"""
            """ for the search.</p>"""))
        target.searchActions.append(target.searchAct)
        
        target.searchNextAct = KyAction(\
                iconText=target.tr('Search next'),
                icon=target.iconCache.icon("findNext.png"),
                text=target.tr('Search &next'),
                shortcut=QKeySequence(target.tr("F3", "Search|Search next")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_search_next', 
                statusTip=target.tr(
                        'Search next occurrence of text'), 
                whatsThis=target.tr(
            """<b>Search next</b>"""
            """<p>Search the next occurrence of some text in the current editor."""
            """ The previously entered searchtext and options are reused.</p>"""))
        target.searchActions.append(target.searchNextAct)
        
        target.searchPrevAct = KyAction(\
                iconText=target.tr('Search previous'),
                icon=target.iconCache.icon("findPrevious.png"),
                text=target.tr('Search &previous'),
                shortcut=QKeySequence(target.tr(
                        "Shift+F3", "Search|Search previous")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_search_previous', 
                statusTip=target.tr(
                        'Search previous occurrence of text'), 
                whatsThis=target.tr(
            """<b>Search previous</b>"""
            """<p>Search the previous occurrence of some text in the current editor."""
            """ The previously entered searchtext and options are reused.</p>"""))
        target.searchActions.append(target.searchPrevAct)
        
        target.searchClearMarkersAct = KyAction(\
                iconText=target.tr('Clear search markers'),
                icon=target.iconCache.icon("findClear.png"),
                text=target.tr('Clear search markers'),
                shortcut=QKeySequence(target.tr(
                        "Ctrl+3", "Search|Clear search markers")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_clear_search_markers', 
                statusTip=target.tr(
                        'Clear all displayed search markers'))
        target.searchClearMarkersAct.setWhatsThis(target.tr(
            """<b>Clear search markers</b>"""
            """<p>Clear all displayed search markers.</p>"""))
        target.searchActions.append(target.searchClearMarkersAct)
        
        target.replaceAct = KyAction(\
                iconText=target.tr('Replace'),
                text=target.tr('&Replace...'),
                shortcut=QKeySequence(target.tr("Ctrl+R", "Search|Replace")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_search_replace', 
                statusTip=target.tr('Replace some text'))
        target.replaceAct.setWhatsThis(target.tr(
            """<b>Replace</b>"""
            """<p>Search for some text in the current editor and replace it. A"""
            """ dialog is shown to enter the searchtext, the replacement text"""
            """ and options for the search and replace.</p>"""))
        target.searchActions.append(target.replaceAct)
        
        target.quickSearchAct = KyAction(\
                iconText=target.tr('Quicksearch'),
#                icon=target.iconCache.icon("quickFindNext.png"),
                text=target.tr('&Quicksearch'),
                shortcut=QKeySequence(target.tr(
                        "Ctrl+Shift+K", "Search|Quicksearch")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_quicksearch', 
                statusTip=target.tr('Perform a quicksearch'))
        target.quickSearchAct.setWhatsThis(target.tr(
            """<b>Quicksearch</b>"""
            """<p>This activates the quicksearch function of the IDE by"""
            """ giving focus to the quicksearch entry field. If this field"""
            """ is already active and contains text, it searches for the"""
            """ next occurrence of this text.</p>"""))
        target.searchActions.append(target.quickSearchAct)
        
        target.quickSearchBackAct = KyAction(\
                iconText=target.tr('Quicksearch backwards'),
#                icon=target.iconCache.icon("quickFindPrev.png"),
                text=target.tr('Quicksearch &backwards'),
                shortcut=QKeySequence(target.tr(
                        "Ctrl+Shift+J", "Search|Quicksearch backwards")),
                actionGroup=target.searchActGrp, 
                objectName='vm_quicksearch_backwards', 
                statusTip=target.tr(
                        'Perform a quicksearch backwards'))
        target.quickSearchBackAct.setWhatsThis(target.tr(
            """<b>Quicksearch backwards</b>"""
            """<p>This searches the previous occurrence of the quicksearch text.</p>"""))
        target.searchActions.append(target.quickSearchBackAct)
        
        target.quickSearchExtendAct = KyAction(\
                iconText=target.tr('Quicksearch extend'),
#                icon=target.iconCache.icon("quickFindExtend.png"),
                text=target.tr('Quicksearch e&xtend'),
                shortcut=QKeySequence(target.tr(
                        "Ctrl+Shift+H", "Search|Quicksearch extend")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_quicksearch_extend', 
                statusTip=target.tr(
                        'Extend the quicksearch to the end of the current word'))
        target.quickSearchExtendAct.setWhatsThis(target.tr(
            """<b>Quicksearch extend</b>"""
            """<p>This extends the quicksearch text to the end of the word"""
            """ currently found.</p>"""))
        target.searchActions.append(target.quickSearchExtendAct)
        
        target.gotoLineAct = KyAction(\
                iconText=target.tr('Goto Line'),
                icon=target.iconCache.icon("gotoLine.png"),
                text=target.tr('&Goto Line...'),
                shortcut=QKeySequence(target.tr("Ctrl+G", "Search|Goto Line")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_search_goto_line', 
                statusTip=target.tr('Goto Line'))
        target.gotoLineAct.setWhatsThis(target.tr(
            """<b>Goto Line</b>"""
            """<p>Go to a specific line of text in the current editor."""
            """ A dialog is shown to enter the linenumber.</p>"""))
        target.searchActions.append(target.gotoLineAct)
        
        target.gotoBraceAct = KyAction(\
                iconText=target.tr('Goto Brace'),
                icon=target.iconCache.icon("gotoBrace.png"),
                text=target.tr('Goto &Brace'),
                shortcut=QKeySequence(target.tr("Ctrl+L", "Search|Goto Brace")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_search_goto_brace', 
                statusTip=target.tr('Goto Brace'))
        target.gotoBraceAct.setWhatsThis(target.tr(
            """<b>Goto Brace</b>"""
            """<p>Go to the matching brace in the current editor.</p>"""))
        target.searchActions.append(target.gotoBraceAct)
        
        target.searchActGrp.setEnabled(False)
        
        target.searchFilesAct = KyAction(\
                parent=target, 
                iconText=target.tr('Search in Files'),
                icon=target.iconCache.icon("projectFind.png"),
                text=target.tr('Search in &Files...'),
                shortcut=QKeySequence(target.tr(
                        "Shift+Ctrl+F", "Search|Search Files")), 
                objectName='vm_search_in_files', 
                statusTip=target.tr(
                        'Search for a text in files'))
        target.searchFilesAct.setWhatsThis(target.tr(
            """<b>Search in Files</b>"""
            """<p>Search for some text in the files of a directory tree"""
            """ or the project. A dialog is shown to enter the searchtext"""
            """ and options for the search and to display the result.</p>"""))
        target.searchActions.append(target.searchFilesAct)
        
        target.replaceFilesAct = KyAction(\
                parent=target, 
                iconText=target.tr('Replace in Files'),
                text=target.tr('Replace in F&iles...'),
                shortcut=QKeySequence(target.tr(
                        "Shift+Ctrl+R", "Search|Replace in Files")), 
                objectName='vm_replace_in_files', 
                statusTip=target.tr(
                    'Search for a text in files and replace it'))
        target.replaceFilesAct.setWhatsThis(target.tr(
            """<b>Replace in Files</b>"""
            """<p>Search for some text in the files of a directory tree"""
            """ or the project and replace it. A dialog is shown to enter"""
            """ the searchtext, the replacement text and options for the"""
            """ search and to display the result.</p>"""))
        target.searchActions.append(target.replaceFilesAct)
        
    def initViewActions(target, iconCache):
        """
        Private method defining the user interface actions for the view commands.
        """
        target.viewActGrp = QActionGroup(target)
        target.viewFoldActGrp = QActionGroup(target)
        
        target.zoomInAct = KyAction(\
                iconText=target.tr('Zoom in'),
                icon=target.iconCache.icon("zoomIn.png"),
                text=target.tr('Zoom &in'),
                shortcut=QKeySequence(target.tr("Ctrl++", "View|Zoom in")), 
                actionGroup=target.viewActGrp, 
                objectName='vm_view_zoom_in', 
                statusTip=target.tr('Zoom in on the text'))
        target.zoomInAct.setWhatsThis(target.tr(
                """<b>Zoom in</b>"""
                """<p>Zoom in on the text. This makes the text bigger.</p>"""))
        target.viewActions.append(target.zoomInAct)
        
        target.zoomOutAct = KyAction(\
                iconText=target.tr('Zoom out'),
                icon=target.iconCache.icon("zoomOut.png"),
                text=target.tr('Zoom &out'),
                shortcut=QKeySequence(target.tr("Ctrl+-", "View|Zoom out")), 
                actionGroup=target.viewActGrp, 
                objectName='vm_view_zoom_out', 
                statusTip=target.tr('Zoom out on the text'))
        target.zoomOutAct.setWhatsThis(target.tr(
                """<b>Zoom out</b>"""
                """<p>Zoom out on the text. This makes the text smaller.</p>"""))
        target.viewActions.append(target.zoomOutAct)
        
        target.zoomToAct = KyAction(\
                iconText=target.tr('Zoom'),
                icon=target.iconCache.icon("zoomTo.png"),
                text=target.tr('&Zoom'),
                shortcut=QKeySequence(target.tr("Ctrl+#", "View|Zoom")), 
                actionGroup=target.viewActGrp,
                objectName='vm_view_zoom', 
                statusTip=target.tr('Zoom the text'))
        target.zoomToAct.setWhatsThis(target.tr(
                """<b>Zoom</b>"""
                """<p>Zoom the text. This opens a dialog where the"""
                """ desired size can be entered.</p>"""))
        target.viewActions.append(target.zoomToAct)
        
        target.toggleAllAct = KyAction(\
                iconText=target.tr('Toggle all folds'),
                text=target.tr('Toggle &all folds'),
                actionGroup=target.viewFoldActGrp,
                objectName='vm_view_toggle_all_folds', 
                statusTip=target.tr('Toggle all folds'))
        target.toggleAllAct.setWhatsThis(target.tr(
                """<b>Toggle all folds</b>"""
                """<p>Toggle all folds of the current editor.</p>"""))
        target.viewActions.append(target.toggleAllAct)
        
        target.toggleAllChildrenAct = KyAction(\
                iconText=target.tr('Toggle all folds recursively'),
                text=target.tr('Toggle all &folds recursively'),
                actionGroup=target.viewFoldActGrp, 
                objectName='vm_view_toggle_all_folds_children', 
                statusTip=target.tr(
                    'Toggle all folds (including children)'))
        target.toggleAllChildrenAct.setWhatsThis(target.tr(
                """<b>Toggle all folds (including children)</b>"""
                """<p>Toggle all folds of the current editor including"""
                """ all children.</p>"""))
        target.viewActions.append(target.toggleAllChildrenAct)
        
        target.toggleCurrentAct = KyAction(\
                iconText=target.tr('Toggle current fold'),
                text=target.tr('Toggle &current fold'),
                actionGroup=target.viewFoldActGrp,
                objectName='vm_view_toggle_current_fold', 
                statusTip=target.tr('Toggle current fold'))
        target.toggleCurrentAct.setWhatsThis(target.tr(
                """<b>Toggle current fold</b>"""
                """<p>Toggle the folds of the current line of the current editor.</p>"""))
        target.viewActions.append(target.toggleCurrentAct)
        
        target.unhighlightAct = KyAction(\
                parent=target,
                iconText=target.tr('Remove all highlights'),
#                icon=target.iconCache.icon("unhighlight.png"),
                text=target.tr('Remove all highlights'),
                objectName='vm_view_unhighlight', 
                statusTip=target.tr('Remove all highlights'))
        target.unhighlightAct.setWhatsThis(target.tr(
                """<b>Remove all highlights</b>"""
                """<p>Remove the highlights of all editors.</p>"""))
        target.viewActions.append(target.unhighlightAct)
        
        target.splitViewAct = KyAction(\
                parent=target,
                iconText=target.tr('Split view'),
                icon=target.iconCache.icon("splitNew.png"),
                text=target.tr('&Split view'),
                objectName='vm_view_split_view', 
                statusTip=target.tr('Add a split to the view'))
        target.splitViewAct.setWhatsThis(target.tr(
                """<b>Split view</b>"""
                """<p>Add a split to the view.</p>"""))
        target.viewActions.append(target.splitViewAct)
        
        target.splitOrientationAct = KyAction(\
                parent=target,
                iconText=target.tr('Arrange Left-Right'),
                icon=target.iconCache.icon("arrangeLeftRight.png"),
                text=target.tr('Arrange Splits Left-Right'),
                objectName='vm_view_arrange_horizontally',
                checkable=True, 
                statusTip=target.tr(
                        'Arrange the splitted views horizontally'))
        target.splitOrientationAct.setWhatsThis(target.tr(
                """<b>Arrange horizontally</b>"""
                """<p>Arrange the splitted views horizontally.</p>"""))
        target.splitOrientationAct.setChecked(False)
        target.viewActions.append(target.splitOrientationAct)
        
        target.splitRemoveAct = KyAction(\
                parent=target, 
                iconText=target.tr('Remove split'),
                icon=target.iconCache.icon("splitRemove.png"),
                text=target.tr('&Remove split'),
                objectName='vm_view_remove_split', 
                statusTip=target.tr('Remove the current split'))
        target.splitRemoveAct.setWhatsThis(target.tr(
                """<b>Remove split</b>"""
                """<p>Remove the current split.</p>"""))
        target.viewActions.append(target.splitRemoveAct)
        
        target.nextSplitAct = KyAction(\
                parent=target, 
                iconText=target.tr('Next split'),
                icon=target.iconCache.icon("splitNext.png"),
                text=target.tr('&Next split'),
                shortcut=QKeySequence(target.tr("Ctrl+Alt+N", "View|Next split")), 
                objectName='vm_next_split', 
                statusTip=target.tr('Move to the next split'))
        target.nextSplitAct.setWhatsThis(target.tr(
                """<b>Next split</b>"""
                """<p>Move to the next split.</p>"""))
        target.viewActions.append(target.nextSplitAct)
        
        target.prevSplitAct = KyAction(\
                parent=target, 
                iconText=target.tr('Previous split'),
                icon=target.iconCache.icon("splitPrev.png"),
                text=target.tr('&Previous split'),
                shortcut=QKeySequence(target.tr(
                        "Ctrl+Alt+P", "View|Previous split")), 
                objectName='vm_previous_split', 
                statusTip=target.tr('Move to the previous split'))
        target.prevSplitAct.setWhatsThis(target.tr(
                """<b>Previous split</b>"""
                """<p>Move to the previous split.</p>"""))
        target.viewActions.append(target.prevSplitAct)
        
#        target.viewActGrp.setEnabled(False)
#        target.viewFoldActGrp.setEnabled(False)
#        target.unhighlightAct.setEnabled(False)
#        target.splitViewAct.setEnabled(False)
#        target.splitOrientationAct.setEnabled(False)
#        target.splitRemoveAct.setEnabled(False)
#        target.nextSplitAct.setEnabled(False)
#        target.prevSplitAct.setEnabled(False)

    def initMacroActions(target, iconCache):
        """
        Private method defining the user interface actions for the macro commands.
        """
        target.macroActGrp = QActionGroup(target)

        target.macroStartRecAct = KyAction(\
                iconText=target.tr('Start Macro Recording'),
                icon=target.iconCache.icon("macroStartRecording.png"),
                text=target.tr('S&tart Macro Recording'),
                actionGroup=target.macroActGrp, 
                objectName='vm_macro_start_recording', 
                statusTip=target.tr('Start Macro Recording'))
        target.macroStartRecAct.setWhatsThis(target.tr(
                """<b>Start Macro Recording</b>"""
                """<p>Start recording editor commands into a new macro.</p>"""))
        target.macroActions.append(target.macroStartRecAct)
        
        target.macroStopRecAct = KyAction(\
                iconText=target.tr('Stop Macro Recording'),
                icon=target.iconCache.icon("macroStopRecording.png"),
                text=target.tr('Sto&p Macro Recording'),
                actionGroup=target.macroActGrp, 
                objectName='vm_macro_stop_recording', 
                statusTip=target.tr('Stop Macro Recording'))
        target.macroStopRecAct.setWhatsThis(target.tr(
                """<b>Stop Macro Recording</b>"""
                """<p>Stop recording editor commands into a new macro.</p>"""))
        target.macroActions.append(target.macroStopRecAct)
        
        target.macroRunAct = KyAction(\
                iconText=target.tr('Run Macro'),
                icon=target.iconCache.icon("macroRun.png"),
                text=target.tr('&Run Macro'),
                actionGroup=target.macroActGrp, 
                objectName='vm_macro_run', 
                statusTip=target.tr('Run Macro'))
        target.macroRunAct.setWhatsThis(target.tr(
                """<b>Run Macro</b>"""
                """<p>Run a previously recorded editor macro.</p>"""))
        target.macroActions.append(target.macroRunAct)
        
        target.macroDeleteAct = KyAction(
                iconText=target.tr('Delete Macro'),
                icon=target.iconCache.icon("macroDelete.png"),
                text=target.tr('&Delete Macro'),
                actionGroup=target.macroActGrp, 
                objectName='vm_macro_delete', 
                statusTip=target.tr('Delete Macro'))
        target.macroDeleteAct.setWhatsThis(target.tr(
                """<b>Delete Macro</b>"""
                """<p>Delete a previously recorded editor macro.</p>"""))
        target.macroActions.append(target.macroDeleteAct)
        
        target.macroLoadAct = KyAction(\
                iconText=target.tr('Load Macro'),
                icon=target.iconCache.icon("macroLoad.png"),
                text=target.tr('&Load Macro'),
                actionGroup=target.macroActGrp, 
                objectName='vm_macro_load', 
                statusTip=target.tr('Load Macro'))
        target.macroLoadAct.setWhatsThis(target.tr(
                """<b>Load Macro</b>"""
                """<p>Load an editor macro from a file.</p>"""))
        target.macroActions.append(target.macroLoadAct)
        
        target.macroSaveAct = KyAction(\
                iconText=target.tr('Save Macro'),
                icon=target.iconCache.icon("macroSave.png"),
                text=target.tr('&Save Macro'),
                actionGroup=target.macroActGrp, 
                objectName='vm_macro_save', 
                statusTip=target.tr('Save Macro'))
        target.macroSaveAct.setWhatsThis(target.tr(
                """<b>Save Macro</b>"""
                """<p>Save a previously recorded editor macro to a file.</p>"""))
        target.macroActions.append(target.macroSaveAct)
        
        target.macroActGrp.setEnabled(False)

    def initBookmarkActions(target, iconCache):
        """
        Private method defining the user interface actions for the bookmarks commands.
        """
        target.bookmarkActGrp = QActionGroup(target)
        
        target.bookmarkToggleAct = KyAction(\
                iconText=target.tr('Toggle Bookmark'),
                icon=target.iconCache.icon("bookmarkToggle.png"),
                text=target.tr('&Toggle Bookmark'),
                shortcut=QKeySequence(target.tr("Alt+Ctrl+T", "Bookmark|Toggle")),
                actionGroup=target.bookmarkActGrp,
                objectName='vm_bookmark_toggle', 
                statusTip=target.tr('Toggle Bookmark'))
        target.bookmarkToggleAct.setWhatsThis(target.tr(
                """<b>Toggle Bookmark</b>"""
                """<p>Toggle a bookmark at the current line of the current editor.</p>"""))
        target.bookmarkActions.append(target.bookmarkToggleAct)
        
        target.bookmarkNextAct = KyAction(\
                iconText=target.tr('Next Bookmark'),
                icon=target.iconCache.icon("bookmarkNext.png"),
                text=target.tr('&Next Bookmark'),
                shortcut=QKeySequence(target.tr("Ctrl+PgDown", "Bookmark|Next")),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_bookmark_next', 
                statusTip=target.tr('Next Bookmark'))
        target.bookmarkNextAct.setWhatsThis(target.tr(
                """<b>Next Bookmark</b>"""
                """<p>Go to next bookmark of the current editor.</p>"""))
        target.bookmarkActions.append(target.bookmarkNextAct)
        
        target.bookmarkPreviousAct = KyAction(\
                iconText=target.tr('Previous Bookmark'),
                icon=target.iconCache.icon("bookmarkPrevious.png"),
                text=target.tr('&Previous Bookmark'),
                shortcut=QKeySequence(target.tr("Ctrl+PgUp", "Bookmark|Previous")),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_bookmark_previous', 
                statusTip=target.tr('Previous Bookmark'))
        target.bookmarkPreviousAct.setWhatsThis(target.tr(
                """<b>Previous Bookmark</b>"""
                """<p>Go to previous bookmark of the current editor.</p>"""))
        target.bookmarkActions.append(target.bookmarkPreviousAct)
        
        target.bookmarkClearAct = KyAction(\
                iconText=target.tr('Clear Bookmarks'),
                icon=target.iconCache.icon("bookmarkClear.png"),
                text=target.tr('&Clear Bookmarks'),
                shortcut=QKeySequence(target.tr("Alt+Ctrl+C", "Bookmark|Clear")), 
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_bookmark_clear', 
                statusTip=target.tr(
            'Clear Bookmarks'))
        target.bookmarkClearAct.setWhatsThis(target.tr(
                """<b>Clear Bookmarks</b>"""
                """<p>Clear bookmarks of all editors.</p>"""))
        target.bookmarkActions.append(target.bookmarkClearAct)
        
        target.syntaxErrorGotoAct = KyAction(\
                iconText=target.tr('Goto Syntax Error'),
                icon=target.iconCache.icon("gotoSyntaxError.png"),
                text=target.tr('&Goto Syntax Error'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_syntaxerror_goto', 
                statusTip=target.tr('Goto Syntax Error'))
        target.syntaxErrorGotoAct.setWhatsThis(target.tr(
                """<b>Goto Syntax Error</b>"""
                """<p>Go to next syntax error of the current editor.</p>"""))
        target.bookmarkActions.append(target.syntaxErrorGotoAct)
        
        target.syntaxErrorClearAct = KyAction(\
                iconText=target.tr('Clear Syntax Errors'),
                icon=target.iconCache.icon("syntaxErrorClear.png"),
                text=target.tr('Clear &Syntax Errors'),
                actionGroup=target.bookmarkActGrp,
                objectName='vm_syntaxerror_clear', 
                statusTip=target.tr('Clear Syntax Errors'))
        target.syntaxErrorClearAct.setWhatsThis(target.tr(
                """<b>Clear Syntax Errors</b>"""
                """<p>Clear syntax errors of all editors.</p>"""))
        target.bookmarkActions.append(target.syntaxErrorClearAct)
        
        target.warningsNextAct = KyAction(\
                iconText=target.tr('Next warning message'),
                icon=target.iconCache.icon("warningNext.png"),
                text=target.tr('&Next warning message'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_warning_next', 
                statusTip=target.tr('Next warning message'))
        target.warningsNextAct.setWhatsThis(target.tr(
                """<b>Next warning message</b>"""
                """<p>Go to next line of the current editor"""
                """ having a py3flakes warning.</p>"""))
        target.bookmarkActions.append(target.warningsNextAct)
        
        target.warningsPreviousAct = KyAction(\
                iconText=target.tr('Previous warning message'),
                icon=target.iconCache.icon("warningPrev.png"),
                text=target.tr('&Previous warning message'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_warning_previous', 
                statusTip=target.tr('Previous warning message'))
        target.warningsPreviousAct.setWhatsThis(target.tr(
                """<b>Previous warning message</b>"""
                """<p>Go to previous line of the current editor"""
                """ having a py3flakes warning.</p>"""))
        target.bookmarkActions.append(target.warningsPreviousAct)
        
        target.warningsClearAct = KyAction(\
                iconText=target.tr('Clear Warning Messages'),
                icon=target.iconCache.icon("warningClear.png"),
                text=target.tr('Clear &Warning Messages'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_warnings_clear', 
                statusTip=target.tr('Clear Warning Messages'))
        target.warningsClearAct.setWhatsThis(target.tr(
                """<b>Clear Warning Messages</b>"""
                """<p>Clear py3flakes warning messages of all editors.</p>"""))
        target.bookmarkActions.append(target.warningsClearAct)
        
        target.notCoveredNextAct = KyAction(\
                iconText=target.tr('Next uncovered line'),
                icon=target.iconCache.icon("flagNext.png"),
                text=target.tr('&Next uncovered line'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_uncovered_next', 
                statusTip=target.tr('Next uncovered line'))
        target.notCoveredNextAct.setWhatsThis(target.tr(
                """<b>Next uncovered line</b>"""
                """<p>Go to next line of the current editor marked as not covered.</p>"""))
        target.bookmarkActions.append(target.notCoveredNextAct)
        
        target.notCoveredPreviousAct = KyAction(\
                iconText=target.tr('Previous uncovered line'),
                icon=target.iconCache.icon("flagPrevious.png"),
                text=target.tr('&Previous uncovered line'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_uncovered_previous', 
                statusTip=target.tr('Previous uncovered line'))
        target.notCoveredPreviousAct.setWhatsThis(target.tr(
                """<b>Previous uncovered line</b>"""
                """<p>Go to previous line of the current editor marked"""
                """ as not covered.</p>"""))
        target.bookmarkActions.append(target.notCoveredPreviousAct)
        
        target.taskNextAct = KyAction(\
                iconText=target.tr('Next Task'),
                icon=target.iconCache.icon("taskNext.png"),
                text=target.tr('&Next Task'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_task_next', 
                statusTip=target.tr('Next Task'))
        target.taskNextAct.setWhatsThis(target.tr(
                """<b>Next Task</b>"""
                """<p>Go to next line of the current editor having a task.</p>"""))
        target.bookmarkActions.append(target.taskNextAct)
        
        target.taskPreviousAct = KyAction(\
                iconText=target.tr('Previous Task'),
                icon=target.iconCache.icon("taskPrevious.png"),
                text=target.tr('&Previous Task'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_task_previous', 
                statusTip=target.tr('Previous Task'))
        target.taskPreviousAct.setWhatsThis(target.tr(
                """<b>Previous Task</b>"""
                """<p>Go to previous line of the current editor having a task.</p>"""
                ))
        target.bookmarkActions.append(target.taskPreviousAct)
        
        target.bookmarkActGrp.setEnabled(False)

    def initSpellingActions(target, iconCache):
        """
        Private method to initialize the spell checking actions.
        """
        target.spellingActGrp = QActionGroup(target)
        
        target.spellCheckAct = KyAction(\
                iconText=target.tr('Spell check'),
#                icon=target.iconCache.icon("spellchecking.png"),
                text=target.tr('&Spell Check...'),
                shortcut=QKeySequence(target.tr("Shift+F7", "Spelling|Spell Check")), 
                actionGroup=target.spellingActGrp, 
                objectName='vm_spelling_spellcheck', 
                statusTip=target.tr(
                        'Perform spell check of current editor'))
        target.spellCheckAct.setWhatsThis(target.tr(
                """<b>Spell check</b>"""
                """<p>Perform a spell check of the current editor.</p>"""))
        target.spellingActions.append(target.spellCheckAct)
        
        target.autoSpellCheckAct = KyAction(\
                iconText=target.tr('Automatic spell checking'),
#                icon=target.iconCache.icon("autospellchecking.png"),
                text=target.tr('&Automatic spell checking'),
                actionGroup=target.spellingActGrp, 
                objectName='vm_spelling_autospellcheck', 
                statusTip=target.tr(
                        '(De-)Activate automatic spell checking'))
        target.autoSpellCheckAct.setWhatsThis(target.tr(
                """<b>Automatic spell checking</b>"""
                """<p>Activate or deactivate the automatic spell checking function of"""
                """ all editors.</p>"""))
        target.autoSpellCheckAct.setCheckable(True)
        target.spellingActions.append(target.autoSpellCheckAct)

    def initDebuggerActions(target, iconCache):
        """
        Method defining the user interface actions.
        """
        target.dbgActions = []
        
        target.dbgRunScriptAct = KyAction(\
                parent=target, 
                iconText=target.tr('Run Script'),
                icon=target.iconCache.icon("scriptRun.png"),
                text=target.tr('&Run Script...'),
                shortcut=QKeySequence(target.tr('F2')),
                objectName='dbg_run_script',
                statusTip=target.tr('Run the current Script'))
        target.dbgRunScriptAct.setWhatsThis(target.tr(
            """<b>Run Script</b>"""
            """<p>Set the command line arguments and run the script outside the"""
            """ debugger. If the file has unsaved changes it may be saved first.</p>"""))
        target.dbgActions.append(target.dbgRunScriptAct)

        target.dbgRunProjectAct = KyAction(\
                parent=target, 
                iconText=target.tr('Run Project'),
                icon=target.iconCache.icon("runProject.png"),
                text=target.tr('Run &Project...'),
                shortcut=QKeySequence(target.tr('Shift+F2')), 
                objectName='dbg_run_project', 
                statusTip=target.tr('Run the current Project'))
        target.dbgRunProjectAct.setWhatsThis(target.tr(
            """<b>Run Project</b>"""
            """<p>Set the command line arguments and run the current project"""
            """ outside the debugger."""
            """ If files of the current project have unsaved changes they may"""
            """ be saved first.</p>"""))
        target.dbgActions.append(target.dbgRunProjectAct)

        target.dbgCoverageScriptAct = KyAction(
                parent=target, 
                iconText=target.tr('Coverage run of Script'),
                icon=target.iconCache.icon("runCoverageScript.png"),
                text=target.tr('Coverage run of Script...'), 
                objectName='dbg_coverage_script', 
                statusTip=target.tr('Perform a coverage run of the current Script'))
        target.dbgCoverageScriptAct.setWhatsThis(target.tr(
            """<b>Coverage run of Script</b>"""
            """<p>Set the command line arguments and run the script under the control"""
            """ of a coverage analysis tool. If the file has unsaved changes it may be"""
            """ saved first.</p>"""))
        target.dbgActions.append(target.dbgCoverageScriptAct)

        target.dbgCoverageProjectAct = KyAction(\
                parent=target, 
                iconText=target.tr('Coverage run of Project'),
                icon=target.iconCache.icon("runCoverageProject.png"),
                text=target.tr('Coverage run of Project...'),
                objectName='dbg_coverage_project', 
                statusTip=target.tr('Perform a coverage run of the current Project'))
        target.dbgCoverageProjectAct.setWhatsThis(target.tr(
            """<b>Coverage run of Project</b>"""
            """<p>Set the command line arguments and run the current project"""
            """ under the control of a coverage analysis tool."""
            """ If files of the current project have unsaved changes they may"""
            """ be saved first.</p>"""))
        target.dbgActions.append(target.dbgCoverageProjectAct)

        target.dbgProfileScriptAct = KyAction(\
                parent=target, 
                iconText=target.tr('Profile Script'),
                icon=target.iconCache.icon("runProfileScript.png"),
                text=target.tr('Profile Script...'),
                objectName='dbg_profile_script', 
                statusTip=target.tr('Profile the current Script'))
        target.dbgProfileScriptAct.setWhatsThis(target.tr(
            """<b>Profile Script</b>"""
            """<p>Set the command line arguments and profile the script."""
            """ If the file has unsaved changes it may be saved first.</p>"""))
        target.dbgActions.append(target.dbgProfileScriptAct)

        target.dbgProfileProjectAct = KyAction(\
                parent=target, 
                iconText=target.tr('Profile Project'),
                icon=target.iconCache.icon("runProfileProject.png"),
                text=target.tr('Profile Project...'),
                objectName='dbg_profile_project', 
                statusTip=target.tr('Profile the current Project'))
        target.dbgProfileProjectAct.setWhatsThis(target.tr(
            """<b>Profile Project</b>"""
            """<p>Set the command line arguments and profile the current project."""
            """ If files of the current project have unsaved changes they may"""
            """ be saved first.</p>"""))
        target.dbgActions.append(target.dbgProfileProjectAct)

        target.dbgDebugScriptAct = KyAction(\
                parent=target, 
                iconText=target.tr('Debug Script'),
                icon=target.iconCache.icon("runDebugScript.png"),
                text=target.tr('&Debug Script...'),
                shortcut=QKeySequence(target.tr('F5')), 
                objectName='dbg_debug_script', 
                statusTip=target.tr('Debug the current Script'), 
                whatsThis=target.tr(
            """<b>Debug Script</b>"""
            """<p>Set the command line arguments and set the current line to be the"""
            """ first executable Python statement of the current editor window."""
            """ If the file has unsaved changes it may be saved first.</p>"""))
        target.dbgActions.append(target.dbgDebugScriptAct)

        target.dbgDebugProjectAct = KyAction(\
                parent=target, 
                iconText=target.tr('Debug Project'),
                icon=target.iconCache.icon("runDebugProject.png"),
                text=target.tr('Debug &Project...'),
                shortcut=QKeySequence(target.tr('Shift+F5')), 
                objectName='dbg_debug_project', 
                statusTip=target.tr('Debug the current Project'), 
                whatsThis=target.tr(
                    """<b>Debug Project</b>"""
                    """<p>Set the command line arguments and set the current line to be the"""
                    """ first executable Python statement of the main script of the current"""
                    """ project. If files of the current project have unsaved changes they may"""
                    """ be saved first.</p>"""))
        target.dbgActions.append(target.dbgDebugProjectAct)

        target.restartAct = KyAction(\
                parent=target, 
                iconText=target.tr('Restart Script'),
                icon=target.iconCache.icon("runRestart.png"),
                text=target.tr('scriptRestart'),
                shortcut=QKeySequence(target.tr('F4')), 
                objectName='dbg_restart_script', 
                statusTip=target.tr('Restart the last debugged script'), 
                whatsThis=target.tr(
                    """<b>Restart Script</b>"""
                    """<p>Set the command line arguments and set the current line to be the"""
                    """ first executable Python statement of the script that was debugged last."""
                    """ If there are unsaved changes, they may be saved first.</p>"""))
        target.dbgActions.append(target.restartAct)

        target.stopAct = KyAction(\
                parent=target, 
                iconText=target.tr('Stop Script'),
                icon=target.iconCache.icon("runStop.png"),
                text=target.tr('Stop Script'),
                shortcut=QKeySequence(target.tr('Shift+F10')), 
                objectName='dbg_stop_script', 
                statusTip=target.tr("Stop the running script."), 
                whatsThis=target.tr(
                """<b>Stop Script</b>"""
                """<p>This stops the script running in the debugger backend.</p>"""))
        target.dbgActions.append(target.stopAct)

        target.dbgActGrp = QActionGroup(target)

        target.dbgContAct = KyAction(\
                iconText=target.tr('Continue'),
#                icon=target.iconCache.icon("debugContinue.png"),
                text=target.tr('&Continue'),
                shortcut=QKeySequence(target.tr('F6')), 
                actionGroup=target.dbgActGrp,
                objectName='dbg_continue', 
                statusTip=target.tr(
                        'Continue running the program from the current line'), 
                whatsThis=target.tr(
                    """<b>Continue</b>"""
                    """<p>Continue running the program from the current line."""
                    """ The program will stop when it terminates or when a """
                    """breakpoint is reached.</p>"""))
        target.dbgActions.append(target.dbgContAct)

        target.dbgContCrsrAct = KyAction(\
                iconText=target.tr('Continue to Cursor'),
#                icon=target.iconCache.icon("debugContinueToCursor.png"),
                text=target.tr('Continue &To Cursor'),
                shortcut=QKeySequence(target.tr('Shift+F6')), 
                actionGroup=target.dbgActGrp,
                objectName='dbg_continue_to_cursor', 
                statusTip=target.tr(\
                    "Continue execution up to the current cursor position"))
        target.dbgContCrsrAct.setWhatsThis(target.tr(
            """<b>Continue To Cursor</b>"""
            """<p>Continue running the program from the current line to the"""
            """ current cursor position.</p>"""))
        target.dbgActions.append(target.dbgContCrsrAct)

        target.dbgSingleStepAct = KyAction(\
                iconText=target.tr('Single Step'),
#                icon=target.iconCache.icon("debugStep.png"),
                text=target.tr('Sin&gle Step'),
                shortcut=QKeySequence(target.tr('F7')), 
                actionGroup=target.dbgActGrp,
                objectName='dbg_single_step', 
                statusTip=target.tr('Execute a single Python statement'))
        target.dbgSingleStepAct.setWhatsThis(target.tr(
            """<b>Single Step</b>"""
            """<p>Execute a single Python statement. If the statement"""
            """ is an <tt>import</tt> statement, a class constructor, or a"""
            """ method or function call then control is returned to the debugger at"""
            """ the next statement.</p>"""))
        target.dbgActions.append(target.dbgSingleStepAct)

        target.dbgStepOverAct = KyAction(\
                iconText=target.tr('Step Over'),
#                icon=target.iconCache.icon("debugStepOver.png"),
                text=target.tr('Step &Over'),
                shortcut=QKeySequence(target.tr('F8')), 
                actionGroup=target.dbgActGrp,
                objectName='dbg_step_over', 
                statusTip=target.tr(
                    "Execute a single Python statement staying in the current frame"))
        target.dbgStepOverAct.setWhatsThis(target.tr(
            """<b>Step Over</b>"""
            """<p>Execute a single Python statement staying in the same frame. If"""
            """ the statement is an <tt>import</tt> statement, a class constructor,"""
            """ or a method or function call then control is returned to the debugger"""
            """ after the statement has completed.</p>"""))
        target.dbgActions.append(target.dbgStepOverAct)

        target.dbgStepOutAct = KyAction(\
                iconText=target.tr('Step Out'),
#                icon=target.iconCache.icon("debugStepOut.png"),
                text=target.tr('Step Ou&t'),
                shortcut=QKeySequence(target.tr('F9')), 
                actionGroup=target.dbgActGrp,
                objectName='dbg_step_out', 
                statusTip=target.tr("Execute Python statements until leaving"))
        target.dbgStepOutAct.setWhatsThis(target.tr(
            """<b>Step Out</b>"""
            """<p>Execute Python statements until leaving the current frame. If"""
            """ the statements are inside an <tt>import</tt> statement, a class"""
            """ constructor, or a method or function call then control is returned"""
            """ to the debugger after the current frame has been left.</p>"""))
        target.dbgActions.append(target.dbgStepOutAct)

        target.dbgStopAct = KyAction(\
                iconText=target.tr('Stop'),
#                icon=target.iconCache.icon("debugStop.png"),
                text=target.tr('&Stop'),
                shortcut=QKeySequence(target.tr('F10')), 
                actionGroup=target.dbgActGrp,
                objectName='dbg_stop', 
                statusTip=target.tr('Stop debugging'))
        target.dbgStopAct.setWhatsThis(target.tr(
            """<b>Stop</b>"""
            """<p>Stop the running debugging session.</p>"""))
        target.dbgActions.append(target.dbgStopAct)
        
        target.dbgContextActGrp = QActionGroup(target)

        target.dbgEvalAct = KyAction(\
                iconText=target.tr('Evaluate'),
                text=target.tr('E&valuate...'),
                icon=target.iconCache.icon("debugContextExecute.png"),
                actionGroup=target.dbgContextActGrp,
                objectName='dbg_evaluate', 
                statusTip=target.tr('Evaluate in current context'))
        target.dbgEvalAct.setWhatsThis(target.tr(
            """<b>Evaluate</b>"""
            """<p>Evaluate an expression in the current context of the"""
            """ debugged program. The result is displayed in the"""
            """ shell window.</p>"""))
        target.dbgActions.append(target.dbgEvalAct)
        
        target.dbgExecAct = KyAction(\
                iconText=target.tr('Execute'),
                icon=target.iconCache.icon("debugContextExecute2.png"),
                text=target.tr('E&xecute...'),
                actionGroup=target.dbgContextActGrp,
                objectName='dbg_execute', 
                statusTip=target.tr(\
                    'Execute a one line statement in the current context'))
        target.dbgExecAct.setWhatsThis(target.tr(
            """<b>Execute</b>"""
            """<p>Execute a one line statement in the current context"""
            """ of the debugged program.</p>"""))
        target.dbgActions.append(target.dbgExecAct)
        
        target.dbgFilterAct = KyAction(\
                parent=target, 
                iconText=target.tr('Variables Type Filter'),
                icon=target.iconCache.icon("filterVariables.png"),
                text=target.tr('Varia&bles Type Filter...'), 
                objectName='dbg_variables_filter', 
                statusTip=target.tr('Configure variables type filter'))
        target.dbgFilterAct.setWhatsThis(target.tr(
            """<b>Variables Type Filter</b>"""
            """<p>Configure the variables type filter. Only variable types that are not"""
            """ selected are displayed in the global or local variables window"""
            """ during a debugging session.</p>"""))
        target.dbgActions.append(target.dbgFilterAct)

        target.dbgExcpFilterAct = KyAction(\
                parent=target, 
                iconText=target.tr('Exceptions Filter'),
                icon=target.iconCache.icon("filterExceptions.png"),
                text=target.tr('&Exceptions Filter...'), 
                objectName='dbg_exceptions_filter', 
                statusTip=target.tr('Configure exceptions filter'), 
                whatsThis=target.tr(
            """<b>Exceptions Filter</b>"""
            """<p>Configure the exceptions filter. Only exception types that are"""
            """ listed are highlighted during a debugging session.</p>"""
            """<p>Please note, that all unhandled exceptions are highlighted"""
            """ indepent from the filter list.</p>"""))
        target.dbgActions.append(target.dbgExcpFilterAct)
        
        target.dbgExcpIgnoreAct = KyAction(\
                parent=target, 
                iconText=target.tr('Ignored Exceptions'),
                icon=target.iconCache.icon("ignoreExceptions.png"),
                text=target.tr('&Ignored Exceptions...'),
                objectName='dbg_ignored_exceptions', 
                statusTip=target.tr('Configure ignored exceptions'), 
                whatsThis=target.tr(
            """<b>Ignored Exceptions</b>"""
            """<p>Configure the ignored exceptions. Only exception types that are"""
            """ not listed are highlighted during a debugging session.</p>"""
            """<p>Please note, that unhandled exceptions cannot be ignored.</p>"""))
        target.dbgActions.append(target.dbgExcpIgnoreAct)

        target.dbgBpActGrp = QActionGroup(target)

        target.dbgToggleBpAct = KyAction(\
                iconText=target.tr('Toggle Breakpoint'),
                icon=target.iconCache.icon("breakpointToggle.png"),
                text=target.tr('Toggle Breakpoint'), 
                shortcut=QKeySequence(target.tr(
                        "Shift+F11", "Debug|Toggle Breakpoint")),
                actionGroup=target.dbgBpActGrp,
                objectName='dbg_toggle_breakpoint', 
                statusTip=target.tr('Toggle Breakpoint'))
        target.dbgToggleBpAct.setWhatsThis(target.tr(
            """<b>Toggle Breakpoint</b>"""
            """<p>Toggles a breakpoint at the current line of the"""
            """ current editor.</p>"""))
        target.dbgActions.append(target.dbgToggleBpAct)
        
        target.dbgEditBpAct = KyAction(\
                iconText=target.tr('Edit Breakpoint'),
                icon=target.iconCache.icon("breakpointEdit.png"),
                text=target.tr('Edit Breakpoint...'),
                shortcut=QKeySequence(target.tr(
                        "Shift+F12", "Debug|Edit Breakpoint")),
                actionGroup=target.dbgBpActGrp,
                objectName='dbg_edit_breakpoint', 
                statusTip=target.tr('Edit Breakpoint'))
        target.dbgEditBpAct.setWhatsThis(target.tr(
            """<b>Edit Breakpoint</b>"""
            """<p>Opens a dialog to edit the breakpoints properties."""
            """ It works at the current line of the current editor.</p>"""))
        target.dbgActions.append(target.dbgEditBpAct)

        target.dbgNextBpAct = KyAction(\
                iconText=target.tr('Next Breakpoint'),
                icon=target.iconCache.icon("breakpointNext.png"),
                text=target.tr('Next Breakpoint'),
                shortcut=QKeySequence(target.tr(
                        "Ctrl+Shift+PgDown","Debug|Next Breakpoint")),
                actionGroup=target.dbgBpActGrp, 
                objectName='dbg_next_breakpoint', 
                statusTip=target.tr('Next Breakpoint'))
        target.dbgNextBpAct.setWhatsThis(target.tr(
            """<b>Next Breakpoint</b>"""
            """<p>Go to next breakpoint of the current editor.</p>"""))
        target.dbgActions.append(target.dbgNextBpAct)

        target.dbgPrevBpAct = KyAction(\
                iconText=target.tr('Previous Breakpoint'),
                icon=target.iconCache.icon("breakpointPrevious.png"),
                text=target.tr('Previous Breakpoint'),
                shortcut=QKeySequence(target.tr( 
                        "Ctrl+Shift+PgUp","Debug|Previous Breakpoint")), 
                actionGroup=target.dbgBpActGrp, 
                objectName='dbg_previous_breakpoint', 
                statusTip=target.tr('Previous Breakpoint'), 
                whatsThis=target.tr(
            """<b>Previous Breakpoint</b>"""
            """<p>Go to previous breakpoint of the current editor.</p>"""))
        target.dbgActions.append(target.dbgPrevBpAct)

        target.dbgClrBpAct = KyAction(\
                iconText=target.tr('Clear Breakpoints'),
                icon=target.iconCache.icon("breakpointClear.png"),
                text=target.tr('Clear Breakpoints'),
                shortcut=QKeySequence(target.tr(
                        "Ctrl+Shift+C","Debug|Clear Breakpoints")),
                actionGroup=target.dbgBpActGrp, 
                objectName='dbg_clear_breakpoint', 
                statusTip=target.tr('Clear Breakpoints'))
        target.dbgClrBpAct.setWhatsThis(target.tr(
            """<b>Clear Breakpoints</b>"""
            """<p>Clear breakpoints of all editors.</p>"""))
        target.dbgActions.append(target.dbgClrBpAct)

#        target.dbgActGrp.setEnabled(False)
#        target.dbgContextActGrp.setEnabled(False)
#        target.dbgBpActGrp.setEnabled(False)
#        target.dbgRunScriptAct.setEnabled(False)
#        target.dbgRunProjectAct.setEnabled(False)
#        target.dbgProfileScriptAct.setEnabled(False)
#        target.dbgProfileProjectAct.setEnabled(False)
#        target.dbgCoverageScriptAct.setEnabled(False)
#        target.dbgCoverageProjectAct.setEnabled(False)
#        target.dbgDebugScriptAct.setEnabled(False)
#        target.dbgDebugProjectAct.setEnabled(False)
#        target.dbgRestartAct.setEnabled(False)
#        target.dbgStopAct.setEnabled(False)

    def initMultiprojectActions(target, iconCache):
        
        target.mpActGrp = QActionGroup(target)
        
        target.mpNewAct = KyAction(\
                iconText=target.tr('New Multiproject'),
                icon=target.iconCache.icon("multiProjectNew.png"),
                text=target.tr('&New...'),
                actionGroup=target.mpActGrp,
                objectName='multi_project_new', 
                statusTip=target.tr('Create a new multiproject'), 
                whatsThis=target.tr(
                    """<b>New...</b>"""
                    """<p>This opens a dialog for entering the info for"""
                    """ creating a new multiproject.</p>"""))
        target.mpActions.append(target.mpNewAct)

        target.mpOpenAct = KyAction(\
                iconText=target.tr('Open Multiproject'),
                icon=target.iconCache.icon("multiProjectOpen.png"),
                text=target.tr('&Open...'),
                actionGroup=target.mpActGrp,
                objectName='multi_project_open', 
                statusTip=target.tr('Open an existing multiproject'), 
                whatsThis=target.tr(
                    """<b>Open...</b>"""
                    """<p>This opens an existing multiproject.</p>"""))
        target.mpActions.append(target.mpOpenAct)

        target.mpCloseAct = KyAction(\
                parent=target, 
                iconText=target.tr('Close Multiproject'),
                icon=target.iconCache.icon("multiProjectClose.png"),
                text=target.tr('&Close'), 
                objectName='multi_project_close', 
                statusTip=target.tr('Close the current multiproject'), 
                whatsThis=target.tr(
                    """<b>Close</b>"""
                    """<p>This closes the current multiproject.</p>"""))
        target.mpActions.append(target.mpCloseAct)

        target.mpSaveAct = KyAction(\
                parent=target, 
                iconText=target.tr('Save Multiproject'),
                icon=target.iconCache.icon("multiProjectSave.png"),
                text=target.tr('&Save'),
                objectName='multi_project_save', 
                statusTip=target.tr('Save the current multiproject'),
                whatsThis=target.tr(
                    """<b>Save</b>"""
                    """<p>This saves the current multiproject.</p>"""))
        target.mpActions.append(target.mpSaveAct)

        target.mpSaveAsAct = KyAction(\
                parent=target, 
                iconText=target.tr('Save Multiproject As'),
                icon=target.iconCache.icon("multiProjectSaveAs.png"),
                text=target.tr('Save &As...'), 
                objectName='multi_project_save_as', 
                statusTip=target.tr('Save the current multiproject to a new file'), 
                whatsThis=target.tr(
                    """<b>Save as</b>"""
                    """<p>This saves the current multiproject to a new file.</p>"""))
        target.mpActions.append(target.mpSaveAsAct)

        target.mpAddAct = KyAction(\
                parent=target, 
                iconText=target.tr('Add project to multiproject'),
                icon=target.iconCache.icon("multiProjectAdd.png"),
                text=target.tr('Add &project...'),
                objectName='multi_project_add_project', 
                statusTip=target.tr('Add a project to the current multiproject'), 
                whatsThis=target.tr(
            """<b>Add project...</b>"""
            """<p>This opens a dialog for adding a project"""
            """ to the current multiproject.</p>"""))
        target.mpActions.append(target.mpAddAct)

        target.mpPropsAct = KyAction(\
                parent=target, 
                iconText=target.tr('Multiproject Properties'),
                icon=target.iconCache.icon("multiProjectProperties.png"),
                text=target.tr('&Properties...'), 
                objectName='multi_project_properties', 
                statusTip=target.tr('Show the multiproject properties'), 
                whatsThis=target.tr(
                    """<b>Properties...</b>"""
                    """<p>This shows a dialog to edit the multiproject properties.</p>"""))
        target.mpActions.append(target.mpPropsAct)

#        target.mpCloseAct.setEnabled(False)
#        target.mpSaveAct.setEnabled(False)
#        target.mpSaveAsAct.setEnabled(False)
#        target.mpAddAct.setEnabled(False)
#        target.mpPropsAct.setEnabled(False)

    def initProjectActions(target, iconCache):
        trUtf8 = target.trUtf8
        
        target.projActions = []
        
        target.projFileActGrp = QActionGroup(target)
        
        target.projNewAct = KyAction(\
                iconText=trUtf8('New project'),
                icon=iconCache.icon("projectNew.png"),
                text=trUtf8('&New...'),
                actionGroup=target.projFileActGrp,
                objectName='project_new', 
                statusTip=trUtf8('Generate a new project'), 
                whatsThis=trUtf8(
            """<b>New...</b>"""
            """<p>This opens a dialog for entering the info for a"""
            """ new project.</p>"""))
        target.projActions.append(target.projNewAct)

        target.projOpenAct = KyAction(\
                iconText=trUtf8('Open project'),
                icon=iconCache.icon("projectOpen.png"),
                text=trUtf8('&Open...'),
                actionGroup=target.projFileActGrp,
                objectName='project_open', 
                statusTip=trUtf8('Open an existing project'), 
                whatsThis=trUtf8(
            """<b>Open...</b>"""
            """<p>This opens an existing project.</p>"""))
        target.projActions.append(target.projOpenAct)

        target.projCloseAct = KyAction(\
                iconText=trUtf8('Close project'),
                icon=iconCache.icon("projectClose.png"),
                text=trUtf8('&Close'), 
                actionGroup=target.projFileActGrp,
                objectName='project_close', 
                statusTip=trUtf8('Close the current project'), 
                whatsThis=trUtf8(
            """<b>Close</b>"""
            """<p>This closes the current project.</p>"""))
        target.projActions.append(target.projOpenAct)

        target.projSaveAct = KyAction(\
                iconText=trUtf8('Save project'),
                icon=iconCache.icon("projectSave.png"),
                text=trUtf8('&Save'), 
                actionGroup=target.projFileActGrp, 
                objectName='project_save', 
                statusTip=trUtf8('Save the current project'), 
                whatsThis=trUtf8(
            """<b>Save</b>"""
            """<p>This saves the current project.</p>"""))
        target.projActions.append(target.projSaveAct)

        target.projSaveAsAct = KyAction(\
                iconText=trUtf8('Save project as'),
                icon=iconCache.icon("projectSaveAs.png"),
                text=trUtf8('Save &as...'),
                actionGroup=target.projFileActGrp,
                objectName='project_save_as', 
                statusTip=trUtf8('Save the current project to a new file'), 
                whatsThis=trUtf8(
            """<b>Save as</b>"""
            """<p>This saves the current project to a new file.</p>"""))
        target.projActions.append(target.projSaveAsAct)

        target.projMgmtActGrp = QActionGroup(target)
        
        target.projAddFilesAct = KyAction(\
                iconText=trUtf8('Add files to project'),
                icon=iconCache.icon("fileMisc.png"),
                text=trUtf8('Add &files...'),
                actionGroup=target.projMgmtActGrp,
                objectName='project_add_file', 
                statusTip=trUtf8('Add files to the current project'), 
                whatsThis=trUtf8(
            """<b>Add files...</b>"""
            """<p>This opens a dialog for adding files to the current project."""
            """ The place to add is determined by the file extension.</p>"""))
        target.projActions.append(target.projAddFilesAct)

        target.projAddDirAct = KyAction(\
                iconText=trUtf8('Add directory to project'),
                icon=iconCache.icon("dirOpen.png"),
                text=trUtf8('Add directory...'),
                actionGroup=target.projMgmtActGrp,
                objectName='project_add_dir', 
                statusTip=trUtf8('Add a directory to the current project'), 
                whatsThis=trUtf8(
            """<b>Add directory...</b>"""
            """<p>This opens a dialog for adding a directory to """
            """the current project.</p>"""))
        target.projActions.append(target.projAddDirAct)

        target.addLangAct = KyAction(\
                iconText=trUtf8('Add translation to project'),
                icon=iconCache.icon("linguist4.png"),
                text=trUtf8('Add &translation...'),
                actionGroup=target.projMgmtActGrp,
                objectName='project_add_translation', 
                statusTip=trUtf8('Add a translation to the current project'), 
                whatsThis=trUtf8(
            """<b>Add translation...</b>"""
            """<p>This opens a dialog for add a translation"""
            """ to the current project.</p>"""))
        target.projActions.append(target.addLangAct)

        target.projFindNewAct = KyAction(\
                iconText=trUtf8('Search for new files'),
                text=trUtf8('Searc&h new files...'),
                actionGroup=target.projMgmtActGrp,
                objectName='project_find_new_files', 
                statusTip=trUtf8('Search for new files in the project directory.'), 
                whatsThis=trUtf8(
            """<b>Search new files...</b>"""
            """<p>This searches for new files (sources, *.ui, *.idl) in """
            """ the project directory and registered subdirectories.</p>"""))
        target.projActions.append(target.projFindNewAct)

        target.projPropsAct = KyAction(\
                iconText=trUtf8('Project properties'),
                icon=iconCache.icon("projectProps.png"),
                text=trUtf8('&Properties...'),
                parent=target, 
                objectName='project_properties', 
                statusTip=trUtf8('Show the project properties'), 
                whatsThis=trUtf8(
            """<b>Properties...</b>"""
            """<p>This shows a dialog to edit the project properties.</p>"""))
        target.projActions.append(target.projPropsAct)

        target.projUserPropsAct = KyAction(\
                iconText=trUtf8('User project properties'),
                icon=iconCache.icon("projectUserProps.png"),
                text=trUtf8('&User Properties...'), 
                parent=target, 
                objectName='project_user_properties', 
                statusTip=trUtf8('Show the user specific project properties'), 
                whatsThis=trUtf8(
            """<b>User Properties...</b>"""
            """<p>This shows a dialog to edit the user specific project properties.</p>"""))
        target.projActions.append(target.projUserPropsAct)

        target.projFileTypesAct = KyAction(\
                iconText=trUtf8('Filetype Associations'),
                text=trUtf8('Filetype Associations...'),
                parent=target, 
                objectName='project_filetype_associations', 
                statusTip=trUtf8('Show the project filetype associations'), 
                whatsThis=trUtf8(
            """<b>Filetype Associations...</b>"""
            """<p>This shows a dialog to edit the filetype associations of the project."""
            """ These associations determine the type (source, form, interface"""
            """ or others) with a filename pattern. They are used when adding a file"""
            """ to the project and when performing a search for new files.</p>"""))
        target.projActions.append(target.projFileTypesAct)

        target.projLexersAct = KyAction(\
                iconText=trUtf8('Lexer Associations'),
                text=trUtf8('Lexer Associations...'),
                parent=target, 
                objectName='project_lexer_associations', 
                statusTip=trUtf8('Show the project lexer associations (overriding defaults)'), 
                whatsThis=trUtf8(
            """<b>Lexer Associations...</b>"""
            """<p>This shows a dialog to edit the lexer associations of the project."""
            """ These associations override the global lexer associations. Lexers"""
            """ are used to highlight the editor text.</p>"""))
        target.projActions.append(target.projLexersAct)

        target.projDbgActGrp = QActionGroup(target)
        
        target.projDbgPropsAct = KyAction(\
                iconText=trUtf8('Debugger Properties'),
                text=trUtf8('Debugger &Properties...'),
                actionGroup=target.projDbgActGrp, 
                objectName='project_debugger_properties', 
                statusTip=trUtf8('Show the debugger properties'), 
                whatsThis=trUtf8(
            """<b>Debugger Properties...</b>"""
            """<p>This shows a dialog to edit project specific debugger settings.</p>"""))
        target.projActions.append(target.projDbgPropsAct)
        
        target.projDbgLoadAct = KyAction(\
                iconText=trUtf8('Load'),
                text=trUtf8('&Load'),
                actionGroup=target.projDbgActGrp, 
                objectName='project_debugger_load', 
                statusTip=trUtf8('Load the debugger properties'), 
                whatsThis=trUtf8(
            """<b>Load Debugger Properties</b>"""
            """<p>This loads the project specific debugger settings.</p>"""))
        target.projActions.append(target.projDbgLoadAct)
        
        target.projDbgSaveAct= KyAction(\
                iconText=trUtf8('Save'),
                text=trUtf8('&Save', 'Project Debugger'),
                actionGroup=target.projDbgActGrp, 
                objectName='project_debugger_save', 
                statusTip=trUtf8('Save the debugger properties'), 
                whatsThis=trUtf8(
            """<b>Save Debugger Properties</b>"""
            """<p>This saves the project specific debugger settings.</p>"""))
        target.projActions.append(target.projDbgSaveAct)
        
        target.projDbgDelAct = KyAction(\
                iconText=trUtf8('Delete'),
                text=trUtf8('&Delete'),
                actionGroup=target.projDbgActGrp, 
                objectName='project_debugger_delete', 
                statusTip=trUtf8('Delete the debugger properties'), 
                whatsThis=trUtf8(
            """<b>Delete Debugger Properties</b>"""
            """<p>This deletes the file containing the project specific"""
            """ debugger settings.</p>"""))
        target.projActions.append(target.projDbgDelAct)
        
        target.projDbgResetAct = KyAction(\
                iconText=trUtf8('Reset'),
                text=trUtf8('&Reset'),
                actionGroup=target.projDbgActGrp, 
                objectName='project_debugger_resets', 
                statusTip=trUtf8('Reset the debugger properties'), 
                whatsThis=trUtf8(
            """<b>Reset Debugger Properties</b>"""
            """<p>This resets the project specific debugger settings.</p>"""))
        target.projActions.append(target.projDbgResetAct)
        
        target.sessionActGrp = QActionGroup(target)

        target.sessionLoadAct = KyAction(\
                iconText=trUtf8('Load session'),
                text=trUtf8('Load session'),
                actionGroup=target.sessionActGrp, 
                objectName='project_load_session', 
                statusTip=trUtf8('Load the projects session file.'), 
                whatsThis=trUtf8(
            """<b>Load session</b>"""
            """<p>This loads the projects session file. The session consists"""
            """ of the following data.<br>"""
            """- all open source files<br>"""
            """- all breakpoint<br>"""
            """- the commandline arguments<br>"""
            """- the working directory<br>"""
            """- the exception reporting flag</p>"""))
        target.projActions.append(target.sessionLoadAct)

        target.sessionSaveAct = KyAction(\
                iconText=trUtf8('Save session'),
                text=trUtf8('Save session'),
                actionGroup=target.sessionActGrp, 
                objectName='project_save_session', 
                statusTip=trUtf8('Save the projects session file.'), 
                whatsThis=trUtf8(
            """<b>Save session</b>"""
            """<p>This saves the projects session file. The session consists"""
            """ of the following data.<br>"""
            """- all open source files<br>"""
            """- all breakpoint<br>"""
            """- the commandline arguments<br>"""
            """- the working directory<br>"""
            """- the exception reporting flag</p>"""))
        target.projActions.append(target.sessionSaveAct)
        
        target.sessionDelAct = KyAction(\
                iconText=trUtf8('Delete session'),
                text=trUtf8('Delete session'),
                actionGroup=target.sessionActGrp, 
                objectName='project_delete_session', 
                statusTip=trUtf8('Delete the projects session file.'), 
                whatsThis=trUtf8(
            """<b>Delete session</b>"""
            """<p>This deletes the projects session file</p>"""))
        target.projActions.append(target.sessionDelAct)
        
        target.projCodeActGrp = QActionGroup(target)

        target.codeMetricsAct = KyAction(\
                iconText=trUtf8('Code Metrics'),
                text=trUtf8('&Code Metrics...'),
                actionGroup=target.projCodeActGrp,
                objectName='project_code_metrics', 
                statusTip=trUtf8(\
                    'Show some code metrics for the project.'), 
                whatsThis=trUtf8(
            """<b>Code Metrics...</b>"""
            """<p>This shows some code metrics for all Python files in the project.</p>"""))
        target.projActions.append(target.codeMetricsAct)

        target.codeCoverageAct = KyAction(\
                iconText=trUtf8('Python Code Coverage'),
                text=trUtf8('Code Co&verage...'),
                actionGroup=target.projCodeActGrp,
                objectName='project_code_coverage', 
                statusTip=trUtf8(\
                    'Show code coverage information for the project.'), 
                whatsThis=trUtf8(
            """<b>Code Coverage...</b>"""
            """<p>This shows the code coverage information for all Python files"""
            """ in the project.</p>"""))
        target.projActions.append(target.codeCoverageAct)

        target.codeProfileAct = KyAction(\
                iconText=trUtf8('Profile Data'),
                text=trUtf8('&Profile Data...'),
                actionGroup=target.projCodeActGrp,
                objectName='project_profile_data', 
                statusTip=trUtf8('Show profiling data for the project.'), 
                whatsThis=trUtf8(
            """<b>Profile Data...</b>"""
            """<p>This shows the profiling data for the project.</p>"""))
        target.projActions.append(target.codeProfileAct)

        target.codeDiagramAct = KyAction(\
                iconText=trUtf8('Application Diagram'),
                text=trUtf8('&Application Diagram...'),
                actionGroup=target.projCodeActGrp,
                objectName='project_code_diagram', 
                statusTip=trUtf8('Show a diagram of the project.'), 
                whatsThis=trUtf8(
            """<b>Application Diagram...</b>"""
            """<p>This shows a diagram of the project.</p>"""))
        target.projActions.append(target.codeDiagramAct)

        target.pkgActGrp = QActionGroup(target)

        target.pkgListAct = KyAction(\
                iconText=trUtf8('Create Package List'),
                icon=iconCache.icon("pluginArchiveList.png"),
                text=trUtf8('Create &Package List'),
                actionGroup=target.pkgActGrp,
                objectName='project_package_list', 
                statusTip=trUtf8(\
                    'Create an initial PKGLIST file for an eric5 plugin.'), 
                whatsThis=trUtf8(
            """<b>Create Package List</b>"""
            """<p>This creates an initial list of files to include in an eric5 """
            """plugin archive. The list is created from the project file.</p>"""))
        target.projActions.append(target.pkgListAct)

        target.pkgArchiveAct = KyAction(\
                iconText=trUtf8('Create Plugin Archive'),
                icon=iconCache.icon("pluginArchive.png"),
                text=trUtf8('Create Plugin &Archive'),
                actionGroup=target.pkgActGrp,
                objectName='project_package_archive', 
                statusTip=trUtf8(\
                    'Create an eric5 plugin archive file.'), 
                whatsThis=trUtf8(
            """<b>Create Plugin Archive</b>"""
            """<p>This creates an eric5 plugin archive file using the list of files """
            """given in the PKGLIST file. The archive name is built from the main """
            """script name.</p>"""))
        target.projActions.append(target.pkgArchiveAct)

        target.pkgArchiveSnapAct = KyAction(\
                iconText=trUtf8('Create Plugin Archive Snapshot'),
                icon=iconCache.icon("pluginArchiveSnapshot.png"),
                text=trUtf8('Create Plugin Archive &Snapshot'),
                actionGroup=target.pkgActGrp,
                objectName='project_package_snapshot_archive', 
                statusTip=trUtf8(
                    'Create an eric5 plugin archive file (snapshot release).'), 
                whatsThis=trUtf8(
            """<b>Create Plugin Archive (Snapshot)</b>"""
            """<p>This creates an eric5 plugin archive file using the list of files """
            """given in the PKGLIST file. The archive name is built from the main """
            """script name. The version entry of the main script is modified to """
            """reflect a snapshot release.</p>"""))
        target.projActions.append(target.pkgArchiveSnapAct)

#        target.projCloseAct.setEnabled(False)
#        target.projSaveAct.setEnabled(False)
#        target.projSaveAsAct.setEnabled(False)
#        target.projMgmtActGrp.setEnabled(False)
#        target.projPropsAct.setEnabled(False)
#        target.projUserPropsAct.setEnabled(False)
#        target.projFileTypesAct.setEnabled(False)
#        target.projLexersAct.setEnabled(False)
#        target.sessionActGrp.setEnabled(False)
#        target.projDbgActGrp.setEnabled(False)
#        target.pkgActGrp.setEnabled(False)
