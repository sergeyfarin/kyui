# -*- coding: utf-8 -*-

# Copyright (c) 2002 - 2010 Detlev Offenbach <detlev@die-offenbachs.de>
#

# The actions defined herein will be used as a test for KyRibbonBar
# -- JH

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from .Widgets.Action import KyAction
from .IconSet import E5Icons


class E5ActionCreator(QObject):
    def __init__(self, target):
        iconCache = E5Icons('../E5Icons/')
        target.actions = []
        target.wizardsActions = []
        
        target.fileExitAct = KyAction(parent=target, 
                iconText=target.tr('Quit'),
                icon=iconCache.icon("exit.png"),
                text=target.tr('&Quit'),
                shortcut=QKeySequence(target.tr("Ctrl+Q")),
                objectName='quit', 
                statusTip=target.tr('Quit the Eric5 IDE'))
        target.exitAct.setWhatsThis(target.tr(
            """<b>Quit the IDE</b>"""
            """<p>This quits the IDE. Any unsaved changes may be saved first."""
            """ Any Python program being debugged will be stopped and the"""
            """ preferences will be written to disc.</p>"""))
        target.actions.append(target.fileExitAct)

        target.viewProfileActGrp = QActionGroup(target)
        target.viewProfileActGrp.setObjectName("viewprofiles")
        target.viewProfileActGrp.setExclusive(True)
        
        target.setEditProfileAct = KyAction(parent=target.viewProfileActGrp, 
                iconText=target.tr('Edit Profile'),
                icon=iconCache.icon("viewProfileEdit.png"),
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
        target.actions.append(target.setEditProfileAct)
        
        target.setDebugProfileAct = KyAction(\
                parent=target.viewProfileActGrp, 
                iconText=target.tr('Debug Profile'),
                icon=iconCache.icon("viewProfileDebug.png"),
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
        target.actions.append(target.setDebugProfileAct)
        
        target.pbAct = KyAction(\
                parent=target, 
                iconText=target.tr('Project Viewer'),
                text=target.tr('&Project-Viewer'), 
                objectName='project_viewer',
                checkable=True,
                statusTip=target.tr('Toggle the Project-Viewer window'))
        target.pbAct.setWhatsThis(target.tr(
            """<b>Toggle the Project-Viewer window</b>"""
            """<p>If the Project-Viewer window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.actions.append(target.pbAct)
        
        target.pbActivateAct = KyAction(\
                parent=target, 
                text=target.tr('Activate Project-Viewer'),
                shortcut=QKeySequence(target.tr("Alt+Shift+P")),
                objectName='project_viewer_activate', 
                checkable=True)
        target.actions.append(target.pbActivateAct)
        target.addAction(target.pbActivateAct)

        target.mpbAct = KyAction(\
                parent=target, 
                iconText=target.tr('Multiproject Viewer'), 
                text=target.tr('&Multiproject-Viewer'),
                objectName='multi_project_viewer', 
                checkable=True, 
                statusTip=target.tr('Toggle the Multiproject-Viewer window'))
        target.mpbAct.setWhatsThis(target.tr(
            """<b>Toggle the Multiproject-Viewer window</b>"""
            """<p>If the Multiproject-Viewer window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.actions.append(target.mpbAct)
        
        target.mpbActivateAct = KyAction( \
                parent=target, 
                text=target.tr('Activate Multiproject-Viewer'),
                shortcut=QKeySequence(target.tr("Alt+Shift+M")),
                objectName='multi_project_viewer_activate',
                checkable=True)
        target.actions.append(target.mpbActivateAct)
        target.addAction(target.mpbActivateAct)

        target.debugViewerAct = KyAction( \
                parent=target, 
                iconText=target.tr('Debug Viewer'),
                text=target.tr('&Debug-Viewer'),
                objectName='debug_viewer',
                checkable=True, 
                statusTip=target.tr('Toggle the Debug-Viewer window'))
        target.debugViewerAct.setWhatsThis(target.tr(
            """<b>Toggle the Debug-Viewer window</b>"""
            """<p>If the Debug-Viewer window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.actions.append(target.debugViewerAct)
        
        target.debugViewerActivateAct = KyAction(parent=target, 
                text=target.tr('Activate Debug-Viewer'),
                shortcut=QKeySequence(target.tr("Alt+Shift+D")),
                objectName='debug_viewer_activate',
                checkable=True)
        target.actions.append(target.debugViewerActivateAct)
        target.addAction(target.debugViewerActivateAct)

        target.shellAct = KyAction(parent=target, 
                iconText=target.tr('Shell'),
                text=target.tr('&Shell'),
                objectName='interpreter_shell',
                checkable=True, 
                statusTip=target.tr('Toggle the Shell window'))
        target.shellAct.setWhatsThis(target.tr(
            """<b>Toggle the Shell window</b>"""
            """<p>If the Shell window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.actions.append(target.shellAct)

        target.shellActivateAct = KyAction(parent=target, 
                text=target.tr('Activate Shell'),
                shortcut=QKeySequence(target.tr("Alt+Shift+S")),
                objectName='interpreter_shell_activate',
                checkable=True)
        target.actions.append(target.shellActivateAct)
        target.addAction(target.shellActivateAct)

        target.terminalAct = KyAction(parent=target, 
                iconText=target.tr('Terminal'),
                text=target.tr('Te&rminal'),
                objectName='terminal',
                checkable=True, 
                statusTip=target.tr('Toggle the Terminal window'))
        target.terminalAct.setWhatsThis(target.tr(
            """<b>Toggle the Terminal window</b>"""
            """<p>If the Terminal window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.actions.append(target.terminalAct)

        target.terminalActivateAct = KyAction(\
                parent=target, 
                text=target.tr('Activate Terminal'),
                shortcut=QKeySequence(target.tr("Alt+Shift+R")),
                objectName='terminal_activate',
                checkable=True)
        target.actions.append(target.terminalActivateAct)
        target.addAction(target.terminalActivateAct)

        target.browserAct = KyAction(\
                parent=target, 
                iconText=target.tr('File Browser'),
                text=target.tr('File &Browser'), 
                objectName='file_browser',
                checkable=True, 
                statusTip=target.tr('Toggle the File-Browser window'))
        target.browserAct.setWhatsThis(target.tr(
            """<b>Toggle the File-Browser window</b>"""
            """<p>If the File-Browser window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.actions.append(target.browserAct)

        target.browserActivateAct = KyAction(\
                parent=target,
                text=target.tr('Activate File-Browser'),
                shortcut=QKeySequence(target.tr("Alt+Shift+F")),
                objectName='file_browser_activate',
                checkable=True)
        target.actions.append(target.browserActivateAct)
        target.addAction(target.browserActivateAct)

        target.logViewerAct = KyAction(\
                parent=target, 
                iconText=target.tr('Log Viewer'),
                text=target.tr('&Log-Viewer'), 
                objectName='log_viewer',
                checkable=True, 
                statusTip=target.tr('Toggle the Log-Viewer window'))
        target.logViewerAct.setWhatsThis(target.tr(
            """<b>Toggle the Log-Viewer window</b>"""
            """<p>If the Log-Viewer window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.actions.append(target.logViewerAct)

        target.logViewerActivateAct = KyAction(\
                parent=target, 
                text=target.tr('Activate Log-Viewer'),
                shortcut=QKeySequence(target.tr("Alt+Shift+G")),
                objectName='log_viewer_activate',
                checkable=True)
        target.actions.append(target.logViewerActivateAct)
        target.addAction(target.logViewerActivateAct)

        target.taskViewerAct = KyAction(\
                parent=target, 
                iconText=target.tr('Task Viewer'),
                text=target.tr('T&ask-Viewer'),
                objectName='task_viewer',
                checkable=True, 
                statusTip=target.tr('Toggle the Task-Viewer window'))
        target.taskViewerAct.setWhatsThis(target.tr(
            """<b>Toggle the Task-Viewer window</b>"""
            """<p>If the Task-Viewer window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.actions.append(target.taskViewerAct)

        target.taskViewerActivateAct = KyAction(\
                parent=target, 
                text=target.tr('Activate Task-Viewer'),
                shortcut=QKeySequence(target.tr("Alt+Shift+T")),
                objectName='task_viewer_activate',
                checkable=True)
        target.actions.append(target.taskViewerActivateAct)
        target.addAction(target.taskViewerActivateAct)

        target.templateViewerAct = KyAction(\
                parent=target,
                text=target.tr('Template Viewer'),
                iconText=target.tr('Temp&late-Viewer'),
                objectName='template_viewer',
                checkable=True, 
                statusTip=target.tr('Toggle the Template-Viewer window'))
        target.templateViewerAct.setWhatsThis(target.tr(
            """<b>Toggle the Template-Viewer window</b>"""
            """<p>If the Template-Viewer window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        
        target.actions.append(target.templateViewerAct)

        target.templateViewerActivateAct = KyAction(\
                parent=target,
                text=target.tr('Activate Template-Viewer'),
                shortcut=QKeySequence(target.tr("Alt+Shift+A")),
                objectName='template_viewer_activate', 
                checkable=True)
        target.actions.append(target.templateViewerActivateAct)
        target.addAction(target.templateViewerActivateAct)

        target.vtAct = KyAction(\
                parent=target,
                iconText=target.tr('Vertical Toolbox'),
                text=target.tr('&Vertical Toolbox'),
                objectName='vertical_toolbox',
                checkable=True, 
                statusTip=target.tr('Toggle the Vertical Toolbox window'))
        target.vtAct.setWhatsThis(target.tr(
            """<b>Toggle the Vertical Toolbox window</b>"""
            """<p>If the Vertical Toolbox window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.actions.append(target.vtAct)
        
        target.htAct = KyAction(\
                parent=target,
                iconText=target.tr('Horizontal Toolbox'),
                text=target.tr('&Horizontal Toolbox'),
                objectName='horizontal_toolbox',
                checkable=True, 
                statusTip=target.tr('Toggle the Horizontal Toolbox window'))
        target.htAct.setWhatsThis(target.tr(
            """<b>Toggle the Horizontal Toolbox window</b>"""
            """<p>If the Horizontal Toolbox window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.actions.append(target.htAct)
        
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
        target.actions.append(target.lsbAct)
        
        target.bsbAct = KyAction(\
                parent=target,
                iconText=target.tr('Bottom Sidebar'),
                text=target.tr('&Bottom Sidebar'),
                objectName='bottom_sidebar',
                checkable=True, 
                statusTip=target.tr('Toggle the bottom sidebar window'))
        target.bsbAct.setWhatsThis(target.tr(
            """<b>Toggle the bottom sidebar window</b>"""
            """<p>If the bottom sidebar window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.actions.append(target.bsbAct)
        
        target.cooperationViewerAct = KyAction(\
                parent=target,
                iconText=target.tr('Cooperation'),
                text=target.tr('&Cooperation'),
                objectName='cooperation_viewer',
                checkable=True, 
                statusTip=target.tr('Toggle the Cooperation window'), 
                whatsThis=target.tr(
            """<b>Toggle the Cooperation window</b>"""
            """<p>If the Cooperation window is hidden then display it."""
            """ If it is displayed then close it.</p>"""))
        target.actions.append(target.cooperationViewerAct)
        
        target.cooperationViewerActivateAct = KyAction(\
                parent=target, 
                text=target.tr('Activate Cooperation-Viewer'),
                shortcut=QKeySequence(target.tr("Alt+Shift+O")),
                objectName='cooperation_viewer_activate',
                checkable=True)
        target.actions.append(target.cooperationViewerActivateAct)
        target.addAction(target.cooperationViewerActivateAct)

        target.whatsThisAct = KyAction(\
                parent=target,
                iconText=target.tr('What\'s This?'),
                icon=iconCache.icon("whatsThis.png"),
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
        target.actions.append(target.whatsThisAct)

        target.helpviewerAct = KyAction(\
                parent=target,
                iconText=target.tr('Helpviewer'),
                icon=iconCache.icon("help.png"),
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
        target.actions.append(target.helpviewerAct)
        
        target.__initQtDocActions()
        target.__initPythonDocAction()
        target.__initEricDocAction()
        target.__initPySideDocActions()
      
        target.versionAct = KyAction(\
                parent=target,
                text=target.tr('Versions'),
                iconText=target.tr('Show &Versions'),
                objectName='show_versions', 
                statusTip=target.tr('Display version information'), 
                whatsThis=target.tr(
            """<b>Show Versions</b>"""
            """<p>Display version information.</p>"""))
        target.actions.append(target.versionAct)

        target.checkUpdateAct = KyAction(\
                parent=target,
                iconText=target.tr('Updates'),
                text=target.tr('Check for &Updates...'),
                objectName='check_updates', 
                statusTip=target.tr('Check for Updates'))
        target.checkUpdateAct.setWhatsThis(target.tr(
            """<b>Check for Updates...</b>"""
            """<p>Checks the internet for updates of eric5.</p>"""))
        target.actions.append(target.checkUpdateAct)
    
        target.showVersionsAct = KyAction(parent=target,
                iconText=target.tr('Show downloadable versions'),
                text=target.tr('Show &downloadable versions...'), 
                objectName='show_downloadable_versions', 
                statusTip=target.tr('Show the versions available for download'))
        target.showVersionsAct.setWhatsThis(target.tr(
            """<b>Show downloadable versions...</b>"""
            """<p>Shows the eric5 versions available for download """
            """from the internet.</p>"""))
        target.actions.append(target.showVersionsAct)

        target.reportBugAct = KyAction(parent=target,
                iconText=target.tr('Report Bug'),
                text=target.tr('Report &Bug...'),
                objectName='report_bug',
                statusTip=target.tr('Report a bug'))
        target.reportBugAct.setWhatsThis(target.tr(
            """<b>Report Bug...</b>"""
            """<p>Opens a dialog to report a bug.</p>"""))
        target.actions.append(target.reportBugAct)
        
        target.requestFeatureAct = KyAction(parent=target,
                iconText=target.tr('Request Feature'),
                text=target.tr('Request &Feature...'),
                objectName='request_feature', 
                statusTip=target.tr('Send a feature request'))
        target.requestFeatureAct.setWhatsThis(target.tr(
            """<b>Request Feature...</b>"""
            """<p>Opens a dialog to send a feature request.</p>"""
                             ))
        target.actions.append(target.requestFeatureAct)

        target.utActGrp = QActionGroup(self)
        
        target.utDialogAct = KyAction(parent=target.utActGrp,
                iconText=target.tr('Unittest'), 
                icon=iconCache.icon("unittest.png"),
                text=target.tr('&Unittest...'),
                actionGroup=target.utActGrp,
                objectName='unittest', 
                statusTip=target.tr('Start unittest dialog'))
        target.utDialogAct.setWhatsThis(target.tr(
            """<b>Unittest</b>"""
            """<p>Perform unit tests. The dialog gives you the"""
            """ ability to select and run a unittest suite.</p>"""))
        target.actions.append(target.utDialogAct)

        target.utRestartAct = KyAction(parent=target.utActGrp,
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
        target.actions.append(target.utRestartAct)
        
        target.utScriptAct = KyAction(parent=target.utActGrp,
                iconText=target.tr('Unittest Script'),
                icon=iconCache.icon("unittestScript.png"),
                text=target.tr('Unittest &Script...'),
                actionGroup=target.utActGrp,
                objectName='unittest_script', 
                statusTip=target.tr('Run unittest with current script'), 
                enabled=False)
        target.utScriptAct.setWhatsThis(target.tr(
            """<b>Unittest Script</b>"""
            """<p>Run unittest with current script.</p>"""))
        target.actions.append(target.utScriptAct)
        
        target.utProjectAct = KyAction(parent=target.utActGrp, 
                iconText=target.tr('Unittest Project'),
                icon=iconCache.icon("unittestProject.png"),
                text=target.tr('Unittest &Project...'),
                actionGroup=target.utActGrp,
                objectName='unittest_project', 
                enabled=False, 
                statusTip=target.tr('Run unittest with current project'))
        target.utProjectAct.setWhatsThis(target.tr(
            """<b>Unittest Project</b>"""
            """<p>Run unittest with current project.</p>"""))
        target.utProjectAct.setEnabled(False)
        target.actions.append(target.utProjectAct)
        
        target.designer4Act = KyAction(parent=target, 
                toolTip=target.tr('Qt-Designer 4'),
                iconText='Designer 4', 
                icon=iconCache.icon("designer4.png"),
                text=target.tr('&Designer 4...'),
                objectName='qt_designer4', 
                statusTip=target.tr('Start Qt-Designer 4'))
        target.designer4Act.setWhatsThis(target.tr(
            """<b>Qt-Designer 4</b>"""
            """<p>Start Qt-Designer 4.</p>"""))
        target.actions.append(target.designer4Act)

        target.linguist4Act = KyAction(parent=target, 
                iconText=target.tr('Linguist 4'),
                icon=iconCache.icon("linguist4.png"),
                text=target.tr('&Linguist 4...'),
                objectName='qt_linguist4', 
                statusTip=target.tr('Start Qt-Linguist 4'))
        target.linguist4Act.setWhatsThis(target.tr(
            """<b>Qt-Linguist 4</b>"""
            """<p>Start Qt-Linguist 4.</p>"""))
        target.actions.append(target.linguist4Act)
    
        target.uipreviewerAct = KyAction(parent=target, 
                iconText=target.tr('UI Previewer'), 
                icon=iconCache.icon("uiPreviewer.png"),
                text=target.tr('&UI Previewer...'),
                objectName='ui_previewer', 
                statusTip=target.tr('Start the UI Previewer'))
        target.uipreviewerAct.setWhatsThis(target.tr(
            """<b>UI Previewer</b>"""
            """<p>Start the UI Previewer.</p>"""))
        target.actions.append(target.uipreviewerAct)
        
        target.trpreviewerAct = KyAction(parent=target,
                iconText=target.tr('Translations Previewer'), 
                icon=iconCache.icon("trPreviewer.png"),
                text=target.tr('&Translations Previewer...'),
                objectName='tr_previewer', 
                statusTip=target.tr('Start the Translations Previewer'))
        target.trpreviewerAct.setWhatsThis(target.tr(
            """<b>Translations Previewer</b>"""
            """<p>Start the Translations Previewer.</p>"""))
        target.actions.append(target.trpreviewerAct)
        
        target.diffAct = KyAction(parent=target,
                iconText=target.tr('Compare Files'),
                icon=iconCache.icon("diffFiles.png"),
                text=target.tr('&Compare Files...'),
                objectName='diff_files', 
                statusTip=target.tr('Compare two files'))
        target.diffAct.setWhatsThis(target.tr(
            """<b>Compare Files</b>"""
            """<p>Open a dialog to compare two files.</p>"""))
        target.actions.append(target.diffAct)

        target.compareAct = KyAction(parent=target,
                iconText=target.tr('Compare Files side by side'),
                icon=iconCache.icon("compareFiles.png"),
                text=target.tr('Compare Files &side by side...'), 
                objectName='compare_files', 
                statusTip=target.tr('Compare two files'))
        target.compareAct.setWhatsThis(target.tr(
            """<b>Compare Files side by side</b>"""
            """<p>Open a dialog to compare two files and show the result"""
            """ side by side.</p>"""))
        target.actions.append(target.compareAct)

        target.sqlBrowserAct = KyAction(parent=target,
                iconText=target.tr('SQL Browser'),
                icon=iconCache.icon("sqlBrowser.png"),
                text=target.tr('SQL &Browser...'), 
                objectName='sql_browser', 
                statusTip=target.tr('Browse a SQL database'))
        target.sqlBrowserAct.setWhatsThis(target.tr(
            """<b>SQL Browser</b>"""
            """<p>Browse a SQL database.</p>"""))
        target.actions.append(target.sqlBrowserAct)

        target.miniEditorAct = KyAction(parent=target,
                iconText=target.tr('Mini Editor'),
                icon=iconCache.icon("editor.png"),
                text=target.tr('Mini &Editor...'), 
                objectName='mini_editor', 
                statusTip=target.tr('Mini Editor'))
        target.miniEditorAct.setWhatsThis(target.tr(
            """<b>Mini Editor</b>"""
            """<p>Open a dialog with a simplified editor.</p>"""))
        target.actions.append(target.miniEditorAct)

        target.webBrowserAct = KyAction(parent=target,
                iconText=target.tr('Web Browser'),
                icon=iconCache.icon("ericWeb.png"),
                text=target.tr('&Web Browser...'), 
                objectName='web_browser', 
                statusTip=target.tr('Start the eric5 Web Browser'))
        target.webBrowserAct.setWhatsThis(target.tr(
            """<b>Web Browser</b>"""
            """<p>Browse the Internet with the eric5 Web Browser.</p>"""))
        target.actions.append(target.webBrowserAct)

        target.iconEditorAct = KyAction(parent=target,
                iconText=target.tr('Icon Editor'),
                icon=iconCache.icon("iconEditor.png"),
                text=target.tr('&Icon Editor...'), 
                objectName='icon_editor', 
                statusTip=target.tr('Start the eric5 Icon Editor'))
        target.iconEditorAct.setWhatsThis(target.tr(
            """<b>Icon Editor</b>"""
            """<p>Starts the eric5 Icon Editor for editing simple icons.</p>"""))
        target.actions.append(target.iconEditorAct)

        target.prefAct = KyAction(parent=target,
                iconText=target.tr('Preferences'),
                icon=iconCache.icon("configure.png"),
                text=target.tr('&Preferences...'),
                objectName='preferences', 
                statusTip=target.tr('Set the prefered configuration'))
        target.prefAct.setWhatsThis(target.tr(
            """<b>Preferences</b>"""
            """<p>Set the configuration items of the application"""
            """ with your prefered values.</p>"""))
        target.actions.append(target.prefAct)

        target.prefExportAct = KyAction(parent=target,
                iconText=target.tr('Export Preferences'),
                icon=iconCache.icon("configureExport.png"),
                text=target.tr('E&xport Preferences...'),
                objectName='export_preferences', 
                statusTip=target.tr('Export the current configuration'))
        target.prefExportAct.setWhatsThis(target.tr(
            """<b>Export Preferences</b>"""
            """<p>Export the current configuration to a file.</p>"""))
        target.actions.append(target.prefExportAct)

        target.prefImportAct = KyAction(parent=target,
                iconText=target.tr('Import Preferences'),
                icon=iconCache.icon("configureImport.png"),
                text=target.tr('I&mport Preferences...'),
                objectName='import_preferences', 
                statusTip=target.tr('Import a previously exported configuration'))
        target.prefImportAct.setWhatsThis(target.tr(
            """<b>Import Preferences</b>"""
            """<p>Import a previously exported configuration.</p>"""))
        target.actions.append(target.prefImportAct)

        target.reloadAPIsAct = KyAction(parent=target,
                iconText=target.tr('Reload APIs'),
                text=target.tr('Reload &APIs'),
                objectName='reload_apis', 
                statusTip=target.tr('Reload the API information'))
        target.reloadAPIsAct.setWhatsThis(target.tr(
            """<b>Reload APIs</b>"""
            """<p>Reload the API information.</p>"""))
        target.actions.append(target.reloadAPIsAct)

        target.showExternalToolsAct = KyAction(parent=target,
                iconText=target.tr('External tools'),
                icon=iconCache.icon("showPrograms.png"),
                text=target.tr('Show external &tools'),
                objectName='show_external_tools', 
                statusTip=target.tr('Reload the API information'))
        target.showExternalToolsAct.setWhatsThis(target.tr(
            """<b>Show external tools</b>"""
            """<p>Opens a dialog to show the path and versions of all"""
            """ extenal tools used by eric5.</p>"""))
        target.actions.append(target.showExternalToolsAct)

        target.configViewProfilesAct = KyAction(parent=target,
                iconText=target.tr('View Profiles'),
                icon=iconCache.icon("configureViewProfiles.png"),
                text=target.tr('&View Profiles...'),
                objectName='view_profiles', 
                statusTip=target.tr('Configure view profiles'))
        target.configViewProfilesAct.setWhatsThis(target.tr(
            """<b>View Profiles</b>"""
            """<p>Configure the view profiles. With this dialog you may"""
            """ set the visibility of the various windows for the predetermined"""
            """ view profiles.</p>"""))
        target.actions.append(target.configViewProfilesAct)

        target.configToolBarsAct = KyAction(parent=target,
                iconText=target.tr('Toolbars'),
                icon=iconCache.icon("toolbarsConfigure.png"),
                text=target.tr('Tool&bars...'),
                objectName='configure_toolbars', 
                statusTip=target.tr('Configure toolbars'))
        target.configToolBarsAct.setWhatsThis(target.tr(
            """<b>Toolbars</b>"""
            """<p>Configure the toolbars. With this dialog you may"""
            """ change the actions shown on the various toolbars and"""
            """ define your own toolbars.</p>"""))
        target.actions.append(target.configToolBarsAct)

        target.shortcutsAct = KyAction(parent=target,
                iconText=target.tr('Keyboard Shortcuts'),
                icon=iconCache.icon("configureShortcuts.png"),
                text=target.tr('Keyboard &Shortcuts...'),
                objectName='keyboard_shortcuts', 
                statusTip=target.tr('Set the keyboard shortcuts'))
        target.shortcutsAct.setWhatsThis(target.tr(
            """<b>Keyboard Shortcuts</b>"""
            """<p>Set the keyboard shortcuts of the application"""
            """ with your prefered values.</p>"""))
        target.actions.append(target.shortcutsAct)

        target.exportShortcutsAct = KyAction(parent=target,
                iconText=target.tr('Export Keyboard Shortcuts'),
                icon=iconCache.icon("exportShortcuts.png"),
                text=target.tr('&Export Keyboard Shortcuts...'),
                objectName='export_keyboard_shortcuts', 
                statusTip=target.tr('Export the keyboard shortcuts'))
        target.exportShortcutsAct.setWhatsThis(target.tr(
            """<b>Export Keyboard Shortcuts</b>"""
            """<p>Export the keyboard shortcuts of the application.</p>"""))
        target.actions.append(target.exportShortcutsAct)

        target.importShortcutsAct = KyAction(parent=target,
                iconText=target.tr('Import Keyboard Shortcuts'),
                icon=iconCache.icon("importShortcuts.png"),
                text=target.tr('&Import Keyboard Shortcuts...'),
                objectName='import_keyboard_shortcuts', 
                statusTip=target.tr('Import the keyboard shortcuts'))
        target.importShortcutsAct.setWhatsThis(target.tr(
            """<b>Import Keyboard Shortcuts</b>"""
            """<p>Import the keyboard shortcuts of the application.</p>"""))
        target.actions.append(target.importShortcutsAct)

        target.viewmanagerActivateAct = KyAction(parent=target,
                iconText=target.tr('Activate current editor'),
                text=target.tr('Activate current editor'),
                shortcut=QKeySequence(target.tr("Alt+Shift+E")),
                objectName='viewmanager_activate',
                checkable=True)
        target.actions.append(target.viewmanagerActivateAct)
        target.addAction(target.viewmanagerActivateAct)

        target.nextTabAct = KyAction(parent=target,
                text=target.tr('Show next'), 
                shortcut=QKeySequence(target.tr('Ctrl+Alt+Tab')),
                objectName='view_next_tab')
        target.actions.append(target.nextTabAct)
        target.addAction(target.nextTabAct)
        
        target.prevTabAct = KyAction(parent=target,
                text=target.tr('Show previous'), 
                shortcut=QKeySequence(target.tr('Shift+Ctrl+Alt+Tab')),
                objectName='view_previous_tab')
        target.actions.append(target.prevTabAct)
        target.addAction(target.prevTabAct)
        
        target.switchTabAct = KyAction(parent=target,
                text=target.tr('Switch between tabs'), 
                shortcut=QKeySequence(target.tr('Ctrl+1')),
                objectName='switch_tabs')
        target.actions.append(target.switchTabAct)
        target.addAction(target.switchTabAct)
        
        target.pluginInfoAct = KyAction(parent=target,
                iconText=target.tr('Plugins'),
                icon=iconCache.icon("plugin.png"),
                text=target.tr('&Plugins...'), 
                objectName='plugin_infos', 
                statusTip=target.tr('Show Plugin Infos'))
        target.pluginInfoAct.setWhatsThis(target.tr(
            """<b>Plugin Infos...</b>"""
            """<p>This opens a dialog, that show some information about"""
            """ loaded plugins.</p>"""))
        target.actions.append(target.pluginInfoAct)
        
        target.pluginInstallAct = KyAction(parent=target,
                iconText=target.tr('Install Plugins'),
                icon=iconCache.icon("pluginInstall.png"),
                text=target.tr('&Install Plugins...'),
                objectName='plugin_install', 
                statusTip=target.tr('Install Plugins'))
        target.pluginInstallAct.setWhatsThis(target.tr(
            """<b>Install Plugins...</b>"""
            """<p>This opens a dialog to install or update plugins.</p>"""))
        target.actions.append(target.pluginInstallAct)
        
        target.pluginDeinstallAct = KyAction(parent=target,
                iconText=target.tr('Uninstall Plugin'),
                icon=iconCache.icon("pluginUninstall.png"),
                text=target.tr('&Uninstall Plugin...'),
                objectName='plugin_deinstall', 
                statusTip=target.tr('Uninstall Plugin'))
        target.pluginDeinstallAct.setWhatsThis(target.tr(
            """<b>Uninstall Plugin...</b>"""
            """<p>This opens a dialog to uninstall a plugin.</p>"""))
        target.actions.append(target.pluginDeinstallAct)

        target.pluginRepoAct = KyAction(parent=target,
                iconText=target.tr('Plugin Repository'),
                icon=iconCache.icon("pluginRepository.png"),
                text=target.tr('Plugin &Repository...'),
                objectName='plugin_repository', 
                statusTip=target.tr('Show Plugins available for download'))
        target.pluginRepoAct.setWhatsThis(target.tr(
            """<b>Plugin Repository...</b>"""
            """<p>This opens a dialog, that shows a list of plugins """
            """available on the Internet.</p>"""))
        target.actions.append(target.pluginRepoAct)
        
        target.__initViewManagerActions()
        target.__initDebuggerActions()
        target.__initProjectActions()
        target.__initMultiProjectActions()
    

        target.qt4DocAct = KyAction(parent=target, 
                iconText=target.tr('Qt4'),
                toolTip=target.tr('Qt4 Documentation'), 
                text=target.tr('Qt&4 Documentation'),
                objectName='qt4_documentation', 
                statusTip=target.tr('Open Qt4 Documentation'))
        target.qt4DocAct.setWhatsThis(target.tr(
            """<b>Qt4 Documentation</b>"""
            """<p>Display the Qt4 Documentation. Dependant upon your settings, this"""
            """ will either show the help in Eric's internal help viewer, or execute"""
            """ a web browser or Qt Assistant. </p>"""))
        target.actions.append(target.qt4DocAct)
      
        target.pyqt4DocAct = KyAction(parent=target, 
                iconText=target.tr('PyQt4'),
                text=target.tr('P&yQt4 Documentation'), 
                toolTip=target.tr('PyQt4 Documentation'), 
                objectName='pyqt4_documentation', 
                statusTip=target.tr('Open PyQt4 Documentation'))
        target.pyqt4DocAct.setWhatsThis(target.tr(
            """<b>PyQt4 Documentation</b>"""
            """<p>Display the PyQt4 Documentation. Dependant upon your settings, this"""
            """ will either show the help in Eric's internal help viewer, or execute"""
            """ a web browser or Qt Assistant. </p>"""))
        target.actions.append(target.pyqt4DocAct)
        
        target.pythonDocAct = KyAction(parent=target, 
                iconText=target.tr('Python'), 
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
        target.actions.append(target.pythonDocAct)
        
        target.ericDocAct = KyAction(parent=target, 
                toolTip=target.tr("Eric API Documentation"),
                iconText='Eric API', 
                text=target.tr('&Eric API Documentation'),
                objectName='eric_documentation', 
                statusTip=target.tr("Open Eric API Documentation"))
        target.ericDocAct.setWhatsThis(target.tr(
            """<b>Eric API Documentation</b>"""
            """<p>Display the Eric API documentation."""
            """ The location for the documentation is the Documentation/Source"""
            """ subdirectory of the eric5 installation directory.</p>"""))
        target.actions.append(target.ericDocAct)
        
        target.iconCache = iconCache
        
        try:
            import PySide
            target.pysideDocAct = KyAction(parent=target,
                    iconText=target.tr('PySide Documentation'),
                    text=target.tr('Py&Side Documentation'),
                    objectName='pyside_documentation', 
                    statusTip=target.tr('Open PySide Documentation'))
            target.pysideDocAct.setWhatsThis(target.tr(
                """<b>PySide Documentation</b>"""
                """<p>Display the PySide Documentation. Dependant upon your settings, """
                """this will either show the help in Eric's internal help viewer, or """
                """execute a web browser or Qt Assistant. </p>"""
            ))
            target.actions.append(target.pysideDocAct)
            del PySide
        except ImportError:
            target.pysideDocAct = None
      
    def __initViewManagerActions(self):
        """
        Public method defining the user interface actions.
        """

        target.editActions = []
        target.fileActions = []
        target.searchActions = []
        target.viewActions = []
        target.windowActions = []
        target.macroActions = []
        target.bookmarkActions = []
        target.spellingActions = []
        
        target.__actions = {
            "bookmark"  : target.bookmarkActions, 
            "edit"      : target.editActions, 
            "file"      : target.fileActions, 
            "macro"     : target.macroActions, 
            "search"    : target.searchActions, 
            "spelling"  : target.spellingActions, 
            "view"      : target.viewActions, 
            "window"    : target.windowActions, 
        }
        
#        target.__initWindowActions()
        target.__initFileActions()
        target.__initEditActions()
        target.__initSearchActions()
        target.__initViewActions()
        target.__initMacroActions()
        target.__initBookmarkActions()
        target.__initSpellingActions()
        
    ##################################################################
    ## Initialize the file related actions, file menu and toolbar
    ##################################################################
    
    def __initFileActions(self):
        """
        Private method defining the user interface actions for file handling.
        """
        target.newAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'New'),
                icon=target.iconCache.icon("new.png"),
                text=target.tr('ViewManager', '&New'),
                shortcut=QKeySequence(target.tr('ViewManager', "Ctrl+N", "File|New")),
                objectName='vm_file_new', 
                statusTip=target.tr('ViewManager', 'Open an empty editor window'))
        target.newAct.setWhatsThis(target.tr('ViewManager', 
            """<b>New</b>"""
            """<p>An empty editor window will be created.</p>"""))
        target.fileActions.append(target.newAct)
        
        target.openAct = KyAction(parent=target,
                iconText=target.tr('ViewManager', 'Open'),
                icon=target.iconCache.icon("open.png"),
                text=target.tr('ViewManager', '&Open...'),
                shortcut=QKeySequence(target.tr('ViewManager', "Ctrl+O", "File|Open")), 
                objectName='vm_file_open', 
                statusTip=target.tr('ViewManager', 'Open a file'))
        target.openAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Open a file</b>"""
            """<p>You will be asked for the name of a file to be opened"""
            """ in an editor window.</p>"""))
        target.fileActions.append(target.openAct)
        
        target.closeActGrp = createActionGroup(self)
        
        target.closeAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Close'),
                icon=target.iconCache.icon("close.png"),
                text=target.tr('ViewManager', '&Close'),
                shortcut=QKeySequence(target.tr('ViewManager', "Ctrl+W", "File|Close")), 
                actionGroup=target.closeActGrp,
                objectName='vm_file_close', 
                statusTip=target.tr('ViewManager', 'Close the current window'))
        target.closeAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Close Window</b>"""
            """<p>Close the current window.</p>"""))
        target.fileActions.append(target.closeAct)
        
        target.closeAllAct = KyAction(\
                parent=target,
                iconText=target.tr('ViewManager', 'Close All'),
                text=target.tr('ViewManager', 'Clos&e All'),
                actionGroup=target.closeActGrp, 
                objectName='vm_file_close_all', 
                statusTip=target.tr('ViewManager', 'Close all editor windows'))
        target.closeAllAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Close All Windows</b>"""
            """<p>Close all editor windows.</p>"""))
        target.fileActions.append(target.closeAllAct)
        
        target.closeActGrp.setEnabled(False)
        
        target.saveActGrp = QActionGroup(self)
        
        target.saveAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Save'),
                icon=target.iconCache.icon("fileSave.png"),
                text=target.tr('ViewManager', '&Save'),
                shortcut=QKeySequence(target.tr('ViewManager',
                    "Ctrl+S", "File|Save")), 
                actionGroup=target.saveActGrp, 
                objectName='vm_file_save', 
                statusTip=target.tr('ViewManager', 'Save the current file'))
        target.saveAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Save File</b>"""
            """<p>Save the contents of current editor window.</p>"""))
        target.fileActions.append(target.saveAct)
        
        target.saveAsAct = KyAction(\
                parent=target,
                iconText=target.tr('ViewManager', 'Save As'),
                icon=target.iconCache.icon("fileSaveAs.png"),
                text=target.tr('ViewManager', 'Save &as...'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                    "Shift+Ctrl+S", "File|Save As")), 
                actionGroup=target.saveActGrp, 
                objectName='vm_file_save_as', 
                statusTip=target.tr('ViewManager',
                        'Save the current file to a new one'))
        target.saveAsAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Save File as</b>"""
            """<p>Save the contents of current editor window to a new file."""
            """ The file can be entered in a file selection dialog.</p>"""))
        target.fileActions.append(target.saveAsAct)
        
        target.saveAllAct = KyAction(\
                parent=target,
                iconText=target.tr('ViewManager', 'Save All'),
                icon=target.iconCache.icon("fileSaveAll.png"),
                text=target.tr('ViewManager', 'Save a&ll...'),
                actionGroup=target.saveActGrp, 
                objectName='vm_file_save_all', 
                statusTip=target.tr('ViewManager', 'Save all files'))
        target.saveAllAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Save All Files</b>"""
            """<p>Save the contents of all editor windows.</p>"""))
        target.fileActions.append(target.saveAllAct)
        
        target.saveActGrp.setEnabled(False)

        target.saveToProjectAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Save to Project'),
                icon=target.iconCache.icon("fileSaveProject.png"),
                text=target.tr('ViewManager', 'Save to Pro&ject'),
                objectName='vm_file_save_to_project', 
                statusTip=target.tr('ViewManager', 
                    'Save the current file to the current project'))
        target.saveToProjectAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Save to Project</b>"""
            """<p>Save the contents of the current editor window to the"""
            """ current project. After the file has been saved, it is"""
            """ automatically added to the current project.</p>"""))
        target.saveToProjectAct.setEnabled(False)
        target.fileActions.append(target.saveToProjectAct)
        
        target.printAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Print'),
                icon=target.iconCache.icon("print.png"),
                text=target.tr('ViewManager', '&Print'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+P", "File|Print")), 
                objectName='vm_file_print', 
                statusTip=target.tr('ViewManager', 'Print the current file'))
        target.printAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Print File</b>"""
            """<p>Print the contents of current editor window.</p>"""))
        target.printAct.setEnabled(False)
        target.fileActions.append(target.printAct)
        
        target.printPreviewAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Print Preview'),
                icon=target.iconCache.icon("printPreview.png"),
                text=target.tr('ViewManager', 'Print Preview'),
                objectName='vm_file_print_preview', 
                statusTip=target.tr('ViewManager', 
                    'Print preview of the current file'))
        target.printPreviewAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Print Preview</b>"""
            """<p>Print preview of the current editor window.</p>"""))
        target.printPreviewAct.setEnabled(False)
        target.fileActions.append(target.printPreviewAct)
        
        target.findFileNameAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Search File'),
                text=target.tr('ViewManager', 'Search &File...'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Alt+Ctrl+F", "File|Search File")), 
                objectName='vm_file_search_file', 
                statusTip=target.tr('ViewManager', 'Search for a file'))
        target.findFileNameAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Search File</b>"""
            """<p>Search for a file.</p>"""))
        target.fileActions.append(target.findFileNameAct)
        
    def __initEditActions(self):
        """
        Private method defining the user interface actions for the edit commands.
        """
        target.editActGrp = QActionGroup(self)
        
        target.undoAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Undo'),
                icon=target.iconCache.icon("editUndo.png"),
                text=target.tr('ViewManager', '&Undo'),
                shortcut=QKeySequence(target.tr('ViewManager',
                        "Ctrl+Z", "Edit|Undo")), 
                shortcuts2=QKeySequence(target.tr('ViewManager',
                        "Alt+Backspace", "Edit|Undo")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_undo', 
                statusTip=target.tr('ViewManager', 'Undo the last change'))
        target.undoAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Undo</b>"""
            """<p>Undo the last change done in the current editor.</p>"""))
        target.editActions.append(target.undoAct)
        
        target.redoAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Redo'),
                icon=target.iconCache.icon("editRedo.png"),
                text=target.tr('ViewManager', '&Redo'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+Shift+Z", "Edit|Redo")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_redo', 
                statusTip=target.tr('ViewManager', 'Redo the last change'))
        target.redoAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Redo</b>"""
            """<p>Redo the last change done in the current editor.</p>"""))
        target.editActions.append(target.redoAct)
        
        target.revertAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Revert to last saved state'),
                text=target.tr('ViewManager', 'Re&vert to last saved state'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+Y", "Edit|Revert")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_revert', 
                statusTip=target.tr('ViewManager', 'Revert to last saved state'))
        target.revertAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Revert to last saved state</b>"""
            """<p>Undo all changes up to the last saved state"""
            """ of the current editor.</p>"""))
        target.editActions.append(target.revertAct)
        
        target.copyActGrp = createActionGroup(target.editActGrp)
        
        target.cutAct = KyAction(\
                parent=target,                 
                iconText=target.tr('ViewManager', 'Cut'),
                icon=target.iconCache.icon("editCut.png"),
                text=target.tr('ViewManager', 'Cu&t'),
                shortcut=QKeySequence(target.tr('ViewManager',
                        "Ctrl+X", "Edit|Cut")),
                shortcut2=QKeySequence(target.tr('ViewManager', 
                        "Shift+Del", "Edit|Cut")),
                actionGroup=target.copyActGrp, 
                objectName='vm_edit_cut', 
                statusTip=target.tr('ViewManager', 'Cut the selection'))
        target.cutAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Cut</b>"""
            """<p>Cut the selected text of the current editor to the clipboard.</p>"""))
        target.editActions.append(target.cutAct)
        
        target.copyAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Copy'),
                icon=target.iconCache.icon("editCopy.png"),
                text=target.tr('ViewManager', '&Copy'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+C", "Edit|Copy")), 
                shortcut2=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+Ins", "Edit|Copy")), 
                actionGroup=target.copyActGrp, 
                objectName='vm_edit_copy', 
                statusTip=target.tr('ViewManager', 'Copy the selection'))
        target.copyAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Copy</b>"""
            """<p>Copy the selected text of the current editor to the clipboard.</p>"""))
        target.editActions.append(target.copyAct)
        
        target.pasteAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Paste'),
                icon=target.iconCache.icon("editPaste.png"),
                text=target.tr('ViewManager', '&Paste'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+V", "Edit|Paste")), 
                shortcut2=QKeySequence(target.tr('ViewManager', 
                        "Shift+Ins", "Edit|Paste")), 
                actionGroup=target.copyActGrp, 
                objectName='vm_edit_paste', 
                statusTip=target.tr('ViewManager', 'Paste the last cut/copied text'))
        target.pasteAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Paste</b>"""
            """<p>Paste the last cut/copied text from the clipboard to"""
            """ the current editor.</p>"""))
        target.editActions.append(target.pasteAct)
        
        target.deleteAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Clear'),
                icon=target.iconCache.icon("editDelete.png"),
                text=target.tr('ViewManager', 'Cl&ear'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Alt+Shift+C", "Edit|Clear")), 
                actionGroup=target.copyActGrp, 
                objectName='vm_edit_clear', 
                statusTip=target.tr('ViewManager', 'Clear all text'))
        target.deleteAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Clear</b>"""
            """<p>Delete all text of the current editor.</p>"""))
        target.editActions.append(target.deleteAct)
        
        target.indentAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Indent'),
                icon=target.iconCache.icon("editIndent.png"),
                text=target.tr('ViewManager', '&Indent'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+I", "Edit|Indent")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_indent', 
                statusTip=target.tr('ViewManager', 'Indent line'))
        target.indentAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Indent</b>"""
            """<p>Indents the current line or the lines of the"""
            """ selection by one level.</p>"""))
        target.editActions.append(target.indentAct)
        
        target.unindentAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Unindent'),
                icon=target.iconCache.icon("editUnindent.png"),
                text=target.tr('ViewManager', 'U&nindent'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+Shift+I", "Edit|Unindent")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_unindent', 
                statusTip=target.tr('ViewManager', 'Unindent line'))
        target.unindentAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Unindent</b>"""
            """<p>Unindents the current line or the lines of the"""
            """ selection by one level.</p>"""))
        target.editActions.append(target.unindentAct)
        
        target.smartIndentAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Smart indent'),
                icon=target.iconCache.icon("editSmartIndent.png"),
                text=target.tr('ViewManager', 'Smart indent'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+Alt+I", "Edit|Smart indent")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_smart_indent', 
                statusTip=target.tr('ViewManager', 'Smart indent Line or Selection'))
        target.smartIndentAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Smart indent</b>"""
            """<p>Indents the current line or the lines of the"""
            """ current selection smartly.</p>"""))
        target.editActions.append(target.smartIndentAct)
        
        target.commentAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Comment'),
                icon=target.iconCache.icon("editComment.png"),
                text=target.tr('ViewManager', 'C&omment'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+M", "Edit|Comment")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_comment', 
                statusTip=target.tr('ViewManager', 'Comment Line or Selection'))
        target.commentAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Comment</b>"""
            """<p>Comments the current line or the lines of the"""
            """ current selection.</p>"""))
        target.editActions.append(target.commentAct)
        
        target.uncommentAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Uncomment'),
                icon=target.iconCache.icon("editUncomment.png"),
                text=target.tr('ViewManager', 'Unco&mment'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Alt+Ctrl+M", "Edit|Uncomment")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_uncomment', 
                statusTip=target.tr('ViewManager', 'Uncomment Line or Selection'))
        target.uncommentAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Uncomment</b>"""
            """<p>Uncomments the current line or the lines of the"""
            """ current selection.</p>"""))
        target.editActions.append(target.uncommentAct)
        
        target.streamCommentAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Stream Comment'),
                text=target.tr('ViewManager', 'Stream Comment'),
                actionGroup=target.editActGrp, 
                objectName='vm_edit_stream_comment', 
                statusTip=target.tr('ViewManager', 
                        'Stream Comment Line or Selection'))
        target.streamCommentAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Stream Comment</b>"""
            """<p>Stream comments the current line or the current selection.</p>"""))
        target.editActions.append(target.streamCommentAct)
        
        target.boxCommentAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Box Comment'),
                text=target.tr('ViewManager', 'Box Comment'),
                actionGroup=target.editActGrp, 
                objectName='vm_edit_box_comment', 
                statusTip=target.tr('ViewManager', 'Box Comment Line or Selection'))
        target.boxCommentAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Box Comment</b>"""
            """<p>Box comments the current line or the lines of the"""
            """ current selection.</p>"""))
        target.editActions.append(target.boxCommentAct)
        
        target.selectBraceAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Select to brace'),
                text=target.tr('ViewManager', 'Select to &brace'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+E", "Edit|Select to brace")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_select_to_brace', 
                statusTip=target.tr('ViewManager', 
                        'Select text to the matching brace'))
        target.selectBraceAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Select to brace</b>"""
            """<p>Select text of the current editor to the matching brace.</p>"""))
        target.editActions.append(target.selectBraceAct)
        
        target.selectAllAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Select all'),
                text=target.tr('ViewManager', '&Select all'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+A", "Edit|Select all")), 
                actionGroup=target.editActGrp,
                objectName='vm_edit_select_all', 
                statusTip=target.tr('ViewManager', 'Select all text'))
        target.selectAllAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Select All</b>"""
            """<p>Select all text of the current editor.</p>"""))
        target.editActions.append(target.selectAllAct)
        
        target.deselectAllAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Deselect all'),
                text=target.tr('ViewManager', '&Deselect all'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Alt+Ctrl+A", "Edit|Deselect all")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_deselect_all', 
                statusTip=target.tr('ViewManager', 'Deselect all text'))
        target.deselectAllAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Deselect All</b>"""
            """<p>Deselect all text of the current editor.</p>"""))
        target.editActions.append(target.deselectAllAct)
        
        target.convertEOLAct = KyAction(\
                parent=target,
                iconText=target.tr('ViewManager', 'Convert EOL Characters'),
                text=target.tr('ViewManager', 'Convert EO&L Characters'),
                actionGroup=target.editActGrp, 
                objectName='vm_edit_convert_eol', 
                statusTip=target.tr('ViewManager', 'Convert Line End Characters'))
        target.convertEOLAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Convert Line End Characters</b>"""
            """<p>Convert the line end characters to the currently set type.</p>"""))
        target.editActions.append(target.convertEOLAct)
        
        target.shortenEmptyAct = KyAction(\
                parent=target,
                iconText=target.tr('ViewManager', 'Shorten empty lines'),
                text=target.tr('ViewManager', 'Shorten empty lines'),
                actionGroup=target.editActGrp, 
                objectName='vm_edit_shorten_empty_lines', 
                statusTip=target.tr('ViewManager', 'Shorten empty lines'))
        target.shortenEmptyAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Shorten empty lines</b>"""
            """<p>Shorten lines consisting solely of whitespace characters.</p>"""))
        target.editActions.append(target.shortenEmptyAct)
        
        target.autoCompleteAct = KyAction(\
                parent=target,
                iconText=target.tr('ViewManager', 'Autocomplete'),
                text=target.tr('ViewManager', '&Autocomplete'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+Space", "Edit|Autocomplete")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_autocomplete', 
                statusTip=target.tr('ViewManager', 'Autocomplete current word'))
        target.autoCompleteAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Autocomplete</b>"""
            """<p>Performs an autocompletion of the word containing the cursor.</p>"""))
        target.editActions.append(target.autoCompleteAct)
        
        target.autoCompleteFromDocAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Autocomplete from Document'),
                text=target.tr('ViewManager', 'Autocomplete from Document'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+Shift+Space", "Edit|Autocomplete from Document")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_autocomplete_from_document', 
                statusTip=target.tr('ViewManager', 
                        'Autocomplete current word from Document'))
        target.autoCompleteFromDocAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Autocomplete from Document</b>"""
            """<p>Performs an autocompletion from document of the word"""
            """ containing the cursor.</p>"""))
        target.editActions.append(target.autoCompleteFromDocAct)
        
        target.autoCompleteFromAPIsAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Autocomplete from APIs'),
                text=target.tr('ViewManager', 'Autocomplete from APIs'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+Alt+Space", 'Edit|Autocomplete from APIs')), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_autocomplete_from_api', 
                statusTip=target.tr('ViewManager', 
                        'Autocomplete current word from APIs'))
        target.autoCompleteFromAPIsAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Autocomplete from APIs</b>"""
            """<p>Performs an autocompletion from APIs of the word containing"""
            """ the cursor.</p>"""))
        target.editActions.append(target.autoCompleteFromAPIsAct)
        
        target.autoCompleteFromAllAct = KyAction(\
                parent=target,
                iconText=target.tr('ViewManager', 'Autocomplete from All'),
                text=target.tr('ViewManager','Autocomplete from All'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Alt+Shift+Space", "Edit|Autocomplete from All")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_autocomplete_from_all', 
                statusTip=target.tr('ViewManager', 
                        'Autocomplete current word from Document and APIs'))
        target.autoCompleteFromAllAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Autocomplete from Document and APIs</b>"""
            """<p>Performs an autocompletion from document and APIs"""
            """ of the word containing the cursor.</p>"""))
        target.editActions.append(target.autoCompleteFromAllAct)
        
        target.calltipsAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Calltip'),
                text=target.tr('ViewManager', '&Calltip'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Alt+Space", "Edit|Calltip")), 
                actionGroup=target.editActGrp, 
                objectName='vm_edit_calltip', 
                statusTip=target.tr('ViewManager', 'Show Calltips'))
        target.calltipsAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Calltip</b>"""
            """<p>Show calltips based on the characters immediately to the"""
            """ left of the cursor.</p>"""))
        target.editActions.append(target.calltipsAct)
        
        target.editActGrp.setEnabled(False)
        target.copyActGrp.setEnabled(False)
        
    def __initSearchActions(self):
        """
        Private method defining the user interface actions for the search commands.
        """
        target.searchActGrp = QActionGroup(self)
        
        target.searchAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Search'),
                icon=target.iconCache.icon("find.png"),
                text=target.tr('ViewManager', '&Search...'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+F", "Search|Search")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_search', 
                statusTip=target.tr('ViewManager', 'Search for a text'))
        target.searchAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Search</b>"""
            """<p>Search for some text in the current editor. A"""
            """ dialog is shown to enter the searchtext and options"""
            """ for the search.</p>"""))
        target.searchActions.append(target.searchAct)
        
        target.searchNextAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Search next'),
                icon=target.iconCache.icon("findNext.png"),
                text=target.tr('ViewManager', 'Search &next'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "F3", "Search|Search next")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_search_next', 
                statusTip=target.tr('ViewManager', 
                        'Search next occurrence of text'))
        target.searchNextAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Search next</b>"""
            """<p>Search the next occurrence of some text in the current editor."""
            """ The previously entered searchtext and options are reused.</p>"""))
        target.searchActions.append(target.searchNextAct)
        
        target.searchPrevAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Search previous'),
                icon=target.iconCache.icon("findPrev.png"),
                text=target.tr('ViewManager', 'Search &previous'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Shift+F3", "Search|Search previous")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_search_previous', 
                statusTip=target.tr('ViewManager', 
                        'Search previous occurrence of text'))
        target.searchPrevAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Search previous</b>"""
            """<p>Search the previous occurrence of some text in the current editor."""
            """ The previously entered searchtext and options are reused.</p>"""))
        target.searchActions.append(target.searchPrevAct)
        
        target.searchClearMarkersAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Clear search markers'),
                icon=target.iconCache.icon("findClear.png"),
                text=target.tr('ViewManager', 'Clear search markers'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+3", "Search|Clear search markers")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_clear_search_markers', 
                statusTip=target.tr('ViewManager', 
                        'Clear all displayed search markers'))
        target.searchClearMarkersAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Clear search markers</b>"""
            """<p>Clear all displayed search markers.</p>"""))
        target.searchActions.append(target.searchClearMarkersAct)
        
        target.replaceAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Replace'),
                text=target.tr('ViewManager', '&Replace...'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+R", "Search|Replace")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_search_replace', 
                statusTip=target.tr('ViewManager', 'Replace some text'))
        target.replaceAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Replace</b>"""
            """<p>Search for some text in the current editor and replace it. A"""
            """ dialog is shown to enter the searchtext, the replacement text"""
            """ and options for the search and replace.</p>"""))
        target.searchActions.append(target.replaceAct)
        
        target.quickSearchAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Quicksearch'),
                icon=target.iconCache.icon("quickFindNext.png"),
                text=target.tr('ViewManager', '&Quicksearch'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+Shift+K", "Search|Quicksearch")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_quicksearch', 
                statusTip=target.tr('ViewManager', 'Perform a quicksearch'))
        target.quickSearchAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Quicksearch</b>"""
            """<p>This activates the quicksearch function of the IDE by"""
            """ giving focus to the quicksearch entry field. If this field"""
            """ is already active and contains text, it searches for the"""
            """ next occurrence of this text.</p>"""))
        target.searchActions.append(target.quickSearchAct)
        
        target.quickSearchBackAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Quicksearch backwards'),
                icon=target.iconCache.icon("quickFindPrev.png"),
                text=target.tr('ViewManager', 'Quicksearch &backwards'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+Shift+J", "Search|Quicksearch backwards")),
                actionGroup=target.searchActGrp, 
                objectName='vm_quicksearch_backwards', 
                statusTip=target.tr('ViewManager', 
                        'Perform a quicksearch backwards'))
        target.quickSearchBackAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Quicksearch backwards</b>"""
            """<p>This searches the previous occurrence of the quicksearch text.</p>"""))
        target.searchActions.append(target.quickSearchBackAct)
        
        target.quickSearchExtendAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Quicksearch extend'),
                icon=target.iconCache.icon("quickFindExtend.png"),
                text=target.tr('ViewManager', 'Quicksearch e&xtend'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+Shift+H", "Search|Quicksearch extend")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_quicksearch_extend', 
                statusTip=target.tr('ViewManager',
                        'Extend the quicksearch to the end of the current word'))
        target.quickSearchExtendAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Quicksearch extend</b>"""
            """<p>This extends the quicksearch text to the end of the word"""
            """ currently found.</p>"""))
        target.searchActions.append(target.quickSearchExtendAct)
        
        target.gotoAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Goto Line'),
                icon=target.iconCache.icon("goto.png"),
                text=target.tr('ViewManager', '&Goto Line...'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+G", "Search|Goto Line")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_search_goto_line', 
                statusTip=target.tr('ViewManager', 'Goto Line'))
        target.gotoAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Goto Line</b>"""
            """<p>Go to a specific line of text in the current editor."""
            """ A dialog is shown to enter the linenumber.</p>"""))
        target.searchActions.append(target.gotoAct)
        
        target.gotoBraceAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Goto Brace'),
                icon=target.iconCache.icon("gotoBrace.png"),
                text=target.tr('ViewManager', 'Goto &Brace'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+L", "Search|Goto Brace")), 
                actionGroup=target.searchActGrp, 
                objectName='vm_search_goto_brace', 
                statusTip=target.tr('ViewManager', 'Goto Brace'))
        target.gotoBraceAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Goto Brace</b>"""
            """<p>Go to the matching brace in the current editor.</p>"""))
        target.searchActions.append(target.gotoBraceAct)
        
        target.searchActGrp.setEnabled(False)
        
        target.searchFilesAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Search in Files'),
                icon=target.iconCache.icon("projectFind.png"),
                text=target.tr('ViewManager', 'Search in &Files...'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Shift+Ctrl+F", "Search|Search Files")), 
                objectName='vm_search_in_files', 
                statusTip=target.tr('ViewManager', 
                        'Search for a text in files'))
        target.searchFilesAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Search in Files</b>"""
            """<p>Search for some text in the files of a directory tree"""
            """ or the project. A dialog is shown to enter the searchtext"""
            """ and options for the search and to display the result.</p>"""))
        target.searchActions.append(target.searchFilesAct)
        
        target.replaceFilesAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Replace in Files'),
                text=target.tr('ViewManager', 'Replace in F&iles...'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Shift+Ctrl+R", "Search|Replace in Files")), 
                objectName='vm_replace_in_files', 
                statusTip=target.tr('ViewManager', 
                    'Search for a text in files and replace it'))
        target.replaceFilesAct.setWhatsThis(target.tr('ViewManager', 
            """<b>Replace in Files</b>"""
            """<p>Search for some text in the files of a directory tree"""
            """ or the project and replace it. A dialog is shown to enter"""
            """ the searchtext, the replacement text and options for the"""
            """ search and to display the result.</p>"""))
        target.searchActions.append(target.replaceFilesAct)
        
    def __initViewActions(self):
        """
        Private method defining the user interface actions for the view commands.
        """
        target.viewActGrp = createActionGroup(self)
        target.viewFoldActGrp = createActionGroup(self)
        
        target.zoomInAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Zoom in'),
                icon=target.iconCache.icon("zoomIn.png"),
                text=target.tr('ViewManager', 'Zoom &in'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl++", "View|Zoom in")), 
                actionGroup=target.viewActGrp, 
                objectName='vm_view_zoom_in', 
                statusTip=target.tr('ViewManager', 'Zoom in on the text'))
        target.zoomInAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Zoom in</b>"""
                """<p>Zoom in on the text. This makes the text bigger.</p>"""))
        target.viewActions.append(target.zoomInAct)
        
        target.zoomOutAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Zoom out'),
                icon=target.iconCache.icon("zoomOut.png"),
                text=target.tr('ViewManager', 'Zoom &out'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+-", "View|Zoom out")), 
                actionGroup=target.viewActGrp, 
                objectName='vm_view_zoom_out', 
                statusTip=target.tr('ViewManager', 'Zoom out on the text'))
        target.zoomOutAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Zoom out</b>"""
                """<p>Zoom out on the text. This makes the text smaller.</p>"""))
        target.viewActions.append(target.zoomOutAct)
        
        target.zoomToAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Zoom'),
                icon=target.iconCache.icon("zoomTo.png"),
                text=target.tr('ViewManager', '&Zoom'),
                shortcut=QKeySequence(target.tr('ViewManager',
                        "Ctrl+#", "View|Zoom")), 
                actionGroup=target.viewActGrp,
                objectName='vm_view_zoom', 
                statusTip=target.tr('ViewManager', 'Zoom the text'))
        target.zoomToAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Zoom</b>"""
                """<p>Zoom the text. This opens a dialog where the"""
                """ desired size can be entered.</p>"""))
        target.viewActions.append(target.zoomToAct)
        
        target.toggleAllAct = KyAction(\
                parent=target,
                iconText=target.tr('ViewManager', 'Toggle all folds'),
                text=target.tr('ViewManager', 'Toggle &all folds'),
                actionGroup=target.viewFoldActGrp,
                objectName='vm_view_toggle_all_folds', 
                statusTip=target.tr('ViewManager', 'Toggle all folds'))
        target.toggleAllAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Toggle all folds</b>"""
                """<p>Toggle all folds of the current editor.</p>"""))
        target.viewActions.append(target.toggleAllAct)
        
        target.toggleAllChildrenAct = KyAction(\
                parent=target,
                iconText=target.tr('ViewManager', 'Toggle all folds recursively'),
                text=target.tr('ViewManager', 'Toggle all &folds recursively'),
                actionGroup=target.viewFoldActGrp, 
                objectName='vm_view_toggle_all_folds_children', 
                statusTip=target.tr('ViewManager', 
                    'Toggle all folds (including children)'))
        target.toggleAllChildrenAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Toggle all folds (including children)</b>"""
                """<p>Toggle all folds of the current editor including"""
                """ all children.</p>"""))
        target.viewActions.append(target.toggleAllChildrenAct)
        
        target.toggleCurrentAct = KyAction(\
                parent=target,
                iconText=target.tr('ViewManager', 'Toggle current fold'),
                text=target.tr('ViewManager', 'Toggle &current fold'),
                actionGroup=target.viewFoldActGrp,
                objectName='vm_view_toggle_current_fold', 
                statusTip=target.tr('ViewManager', 'Toggle current fold'))
        target.toggleCurrentAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Toggle current fold</b>"""
                """<p>Toggle the folds of the current line of the current editor.</p>"""))
        target.viewActions.append(target.toggleCurrentAct)
        
        target.unhighlightAct = KyAction(\
                parent=target,
                iconText=target.tr('ViewManager', 'Remove all highlights'),
                icon=target.iconCache.icon("unhighlight.png"),
                text=target.tr('ViewManager', 'Remove all highlights'),
                objectName='vm_view_unhighlight', 
                statusTip=target.tr('ViewManager', 'Remove all highlights'))
        target.unhighlightAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Remove all highlights</b>"""
                """<p>Remove the highlights of all editors.</p>"""))
        target.viewActions.append(target.unhighlightAct)
        
        target.splitViewAct = KyAction(\
                parent=target,
                iconText=target.tr('ViewManager', 'Split view'),
                icon=target.iconCache.icon("splitVertical.png"),
                text=target.tr('ViewManager', '&Split view'),
                objectName='vm_view_split_view', 
                statusTip=target.tr('ViewManager', 'Add a split to the view'))
        target.splitViewAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Split view</b>"""
                """<p>Add a split to the view.</p>"""))
        target.viewActions.append(target.splitViewAct)
        
        target.splitOrientationAct = KyAction(\
                parent=target,
                iconText=target.tr('ViewManager', 'Arrange horizontally'),
                text=target.tr('ViewManager', 'Arrange &horizontally'),
                objectName='vm_view_arrange_horizontally',
                checkable=True, 
                statusTip=target.tr('ViewManager', 
                        'Arrange the splitted views horizontally'))
        target.splitOrientationAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Arrange horizontally</b>"""
                """<p>Arrange the splitted views horizontally.</p>"""))
        target.splitOrientationAct.setChecked(False)
        target.viewActions.append(target.splitOrientationAct)
        
        target.splitRemoveAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Remove split'),
                icon=target.iconCache.icon("remsplitVertical.png"),
                text=target.tr('ViewManager', '&Remove split'),
                objectName='vm_view_remove_split', 
                statusTip=target.tr('ViewManager', 'Remove the current split'))
        target.splitRemoveAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Remove split</b>"""
                """<p>Remove the current split.</p>"""))
        target.viewActions.append(target.splitRemoveAct)
        
        target.nextSplitAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Next split'),
                text=target.tr('ViewManager', '&Next split'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+Alt+N", "View|Next split")), 
                objectName='vm_next_split', 
                statusTip=target.tr('ViewManager', 'Move to the next split'))
        target.nextSplitAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Next split</b>"""
                """<p>Move to the next split.</p>"""))
        target.viewActions.append(target.nextSplitAct)
        
        target.prevSplitAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Previous split'),
                text=target.tr('ViewManager', '&Previous split'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+Alt+P", "View|Previous split")), 
                objectName='vm_previous_split', 
                statusTip=target.tr('ViewManager', 'Move to the previous split'))
        target.prevSplitAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Previous split</b>"""
                """<p>Move to the previous split.</p>"""))
        target.viewActions.append(target.prevSplitAct)
        
        target.viewActGrp.setEnabled(False)
        target.viewFoldActGrp.setEnabled(False)
        target.unhighlightAct.setEnabled(False)
        target.splitViewAct.setEnabled(False)
        target.splitOrientationAct.setEnabled(False)
        target.splitRemoveAct.setEnabled(False)
        target.nextSplitAct.setEnabled(False)
        target.prevSplitAct.setEnabled(False)

    def __initMacroActions(self):
        """
        Private method defining the user interface actions for the macro commands.
        """
        target.macroActGrp = createActionGroup(self)

        target.macroStartRecAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Start Macro Recording'),
                text=target.tr('ViewManager', 'S&tart Macro Recording'),
                actionGroup=target.macroActGrp, 
                objectName='vm_macro_start_recording', 
                statusTip=target.tr('ViewManager', 'Start Macro Recording'))
        target.macroStartRecAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Start Macro Recording</b>"""
                """<p>Start recording editor commands into a new macro.</p>"""))
        target.macroActions.append(target.macroStartRecAct)
        
        target.macroStopRecAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Stop Macro Recording'),
                text=target.tr('ViewManager', 'Sto&p Macro Recording'),
                actionGroup=target.macroActGrp, 
                objectName='vm_macro_stop_recording', 
                statusTip=target.tr('ViewManager', 'Stop Macro Recording'))
        target.macroStopRecAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Stop Macro Recording</b>"""
                """<p>Stop recording editor commands into a new macro.</p>"""))
        target.macroActions.append(target.macroStopRecAct)
        
        target.macroRunAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Run Macro'),
                text=target.tr('ViewManager', '&Run Macro'),
                actionGroup=target.macroActGrp, 
                objectName='vm_macro_run', 
                statusTip=target.tr('ViewManager', 'Run Macro'))
        target.macroRunAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Run Macro</b>"""
                """<p>Run a previously recorded editor macro.</p>"""))
        target.macroActions.append(target.macroRunAct)
        
        target.macroDeleteAct = KyAction(
                parent=target, 
                iconText=target.tr('ViewManager', 'Delete Macro'),
                text=target.tr('ViewManager', '&Delete Macro'),
                actionGroup=target.macroActGrp, 
                objectName='vm_macro_delete', 
                statusTip=target.tr('ViewManager', 'Delete Macro'))
        target.macroDeleteAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Delete Macro</b>"""
                """<p>Delete a previously recorded editor macro.</p>"""))
        target.macroActions.append(target.macroDeleteAct)
        
        target.macroLoadAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Load Macro'),
                text=target.tr('ViewManager', '&Load Macro'),
                actionGroup=target.macroActGrp, 
                objectName='vm_macro_load', 
                statusTip=target.tr('ViewManager', 'Load Macro'))
        target.macroLoadAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Load Macro</b>"""
                """<p>Load an editor macro from a file.</p>"""))
        target.macroActions.append(target.macroLoadAct)
        
        target.macroSaveAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Save Macro'),
                text=target.tr('ViewManager', '&Save Macro'),
                actionGroup=target.macroActGrp, 
                objectName='vm_macro_save', 
                statusTip=target.tr('ViewManager', 'Save Macro'))
        target.macroSaveAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Save Macro</b>"""
                """<p>Save a previously recorded editor macro to a file.</p>"""))
        target.macroActions.append(target.macroSaveAct)
        
        target.macroActGrp.setEnabled(False)

    def __initBookmarkActions(self):
        """
        Private method defining the user interface actions for the bookmarks commands.
        """
        target.bookmarkActGrp = createActionGroup(self)

        target.bookmarkToggleAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Toggle Bookmark'),
                icon=target.iconCache.icon("bookmarkToggle.png"),
                text=target.tr('ViewManager', '&Toggle Bookmark'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                                "Alt+Ctrl+T", "Bookmark|Toggle")),
                actionGroup=target.bookmarkActGrp,
                objectName='vm_bookmark_toggle', 
                statusTip=target.tr('ViewManager', 'Toggle Bookmark'))
        target.bookmarkToggleAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Toggle Bookmark</b>"""
                """<p>Toggle a bookmark at the current line of the current editor.</p>"""))
        target.bookmarkActions.append(target.bookmarkToggleAct)
        
        target.bookmarkNextAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Next Bookmark'),
                icon=target.iconCache.icon("bookmarkNext.png"),
                text=target.tr('ViewManager', '&Next Bookmark'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+PgDown", "Bookmark|Next")),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_bookmark_next', 
                statusTip=target.tr('ViewManager', 'Next Bookmark'))
        target.bookmarkNextAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Next Bookmark</b>"""
                """<p>Go to next bookmark of the current editor.</p>"""))
        target.bookmarkActions.append(target.bookmarkNextAct)
        
        target.bookmarkPreviousAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Previous Bookmark'),
                icon=target.iconCache.icon("bookmarkPrevious.png"),
                text=target.tr('ViewManager', '&Previous Bookmark'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Ctrl+PgUp", "Bookmark|Previous")),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_bookmark_previous', 
                statusTip=target.tr('ViewManager', 'Previous Bookmark'))
        target.bookmarkPreviousAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Previous Bookmark</b>"""
                """<p>Go to previous bookmark of the current editor.</p>"""))
        target.bookmarkActions.append(target.bookmarkPreviousAct)
        
        target.bookmarkClearAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Clear Bookmarks'),
                text=target.tr('ViewManager', '&Clear Bookmarks'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Alt+Ctrl+C", "Bookmark|Clear")), 
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_bookmark_clear', 
                statusTip=target.tr('ViewManager', 
            'Clear Bookmarks'))
        target.bookmarkClearAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Clear Bookmarks</b>"""
                """<p>Clear bookmarks of all editors.</p>"""))
        target.bookmarkActions.append(target.bookmarkClearAct)
        
        target.syntaxErrorGotoAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Goto Syntax Error'),
                icon=target.iconCache.icon("syntaxErrorGoto.png"),
                text=target.tr('ViewManager', '&Goto Syntax Error'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_syntaxerror_goto', 
                statusTip=target.tr('ViewManager', 'Goto Syntax Error'))
        target.syntaxErrorGotoAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Goto Syntax Error</b>"""
                """<p>Go to next syntax error of the current editor.</p>"""))
        target.bookmarkActions.append(target.syntaxErrorGotoAct)
        
        target.syntaxErrorClearAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Clear Syntax Errors'),
                text=target.tr('ViewManager', 'Clear &Syntax Errors'),
                actionGroup=target.bookmarkActGrp,
                objectName='vm_syntaxerror_clear', 
                statusTip=target.tr('ViewManager', 'Clear Syntax Errors'))
        target.syntaxErrorClearAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Clear Syntax Errors</b>"""
                """<p>Clear syntax errors of all editors.</p>"""))
        target.bookmarkActions.append(target.syntaxErrorClearAct)
        
        target.warningsNextAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Next warning message'),
                icon=target.iconCache.icon("warningNext.png"),
                text=target.tr('ViewManager', '&Next warning message'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_warning_next', 
                statusTip=target.tr('ViewManager', 'Next warning message'))
        target.warningsNextAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Next warning message</b>"""
                """<p>Go to next line of the current editor"""
                """ having a py3flakes warning.</p>"""))
        target.bookmarkActions.append(target.warningsNextAct)
        
        target.warningsPreviousAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Previous warning message'),
                icon=target.iconCache.icon("warningPrev.png"),
                text=target.tr('ViewManager', '&Previous warning message'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_warning_previous', 
                statusTip=target.tr('ViewManager', 'Previous warning message'))
        target.warningsPreviousAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Previous warning message</b>"""
                """<p>Go to previous line of the current editor"""
                """ having a py3flakes warning.</p>"""))
        target.bookmarkActions.append(target.warningsPreviousAct)
        
        target.warningsClearAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Clear Warning Messages'),
                text=target.tr('ViewManager', 'Clear &Warning Messages'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_warnings_clear', 
                statusTip=target.tr('ViewManager', 'Clear Warning Messages'))
        target.warningsClearAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Clear Warning Messages</b>"""
                """<p>Clear py3flakes warning messages of all editors.</p>"""))
        target.bookmarkActions.append(target.warningsClearAct)
        
        target.notCoveredNextAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Next uncovered line'),
                icon=target.iconCache.icon("notCoveredNext.png"),
                text=target.tr('ViewManager', '&Next uncovered line'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_uncovered_next', 
                statusTip=target.tr('ViewManager', 'Next uncovered line'))
        target.notCoveredNextAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Next uncovered line</b>"""
                """<p>Go to next line of the current editor marked as not covered.</p>"""))
        target.bookmarkActions.append(target.notCoveredNextAct)
        
        target.notCoveredPreviousAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Previous uncovered line'),
                icon=target.iconCache.icon("notCoveredPrev.png"),
                text=target.tr('ViewManager', '&Previous uncovered line'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_uncovered_previous', 
                statusTip=target.tr('ViewManager', 'Previous uncovered line'))
        target.notCoveredPreviousAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Previous uncovered line</b>"""
                """<p>Go to previous line of the current editor marked"""
                """ as not covered.</p>"""))
        target.bookmarkActions.append(target.notCoveredPreviousAct)
        
        target.taskNextAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Next Task'),
                icon=target.iconCache.icon("taskNext.png"),
                text=target.tr('ViewManager', '&Next Task'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_task_next', 
                statusTip=target.tr('ViewManager', 'Next Task'))
        target.taskNextAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Next Task</b>"""
                """<p>Go to next line of the current editor having a task.</p>"""))
        target.bookmarkActions.append(target.taskNextAct)
        
        target.taskPreviousAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Previous Task'),
                icon=target.iconCache.icon("taskPrev.png"),
                text=target.tr('ViewManager', '&Previous Task'),
                actionGroup=target.bookmarkActGrp, 
                objectName='vm_task_previous', 
                statusTip=target.tr('ViewManager', 'Previous Task'))
        target.taskPreviousAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Previous Task</b>"""
                """<p>Go to previous line of the current editor having a task.</p>"""
                ))
        target.bookmarkActions.append(target.taskPreviousAct)
        
        target.bookmarkActGrp.setEnabled(False)

    def __initSpellingActions(self):
        """
        Private method to initialize the spell checking actions.
        """
        target.spellingActGrp = createActionGroup(self)
        
        target.spellCheckAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Spell check'),
                icon=target.iconCache.icon("spellchecking.png"),
                text=target.tr('ViewManager', '&Spell Check...'),
                shortcut=QKeySequence(target.tr('ViewManager', 
                        "Shift+F7", "Spelling|Spell Check")), 
                actionGroup=target.spellingActGrp, 
                objectName='vm_spelling_spellcheck', 
                statusTip=target.tr('ViewManager', 
                        'Perform spell check of current editor'))
        target.spellCheckAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Spell check</b>"""
                """<p>Perform a spell check of the current editor.</p>"""))
        target.spellingActions.append(target.spellCheckAct)
        
        target.autoSpellCheckAct = KyAction(\
                parent=target, 
                iconText=target.tr('ViewManager', 'Automatic spell checking'),
                icon=target.iconCache.icon("autospellchecking.png"),
                text=target.tr('ViewManager', '&Automatic spell checking'),
                actionGroup=target.spellingActGrp, 
                objectName='vm_spelling_autospellcheck', 
                statusTip=target.tr('ViewManager', 
                        '(De-)Activate automatic spell checking'))
        target.autoSpellCheckAct.setWhatsThis(target.tr('ViewManager', 
                """<b>Automatic spell checking</b>"""
                """<p>Activate or deactivate the automatic spell checking function of"""
                """ all editors.</p>"""))
        target.autoSpellCheckAct.setCheckable(True)
        target.spellingActions.append(target.autoSpellCheckAct)

    def __initDebuggerActions(self):
        """
        Method defining the user interface actions.
        """
        target.dbgActions = []
        
        target.dbgRunScriptAct = KyAction(\
                parent=target, 
                iconText=target.tr('Run Script'),
                icon=target.iconCache.icon("runScript.png"),
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
                icon=target.iconCache.icon("coverageScript.png"),
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
                icon=target.iconCache.icon("coverageProject.png"),
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
                icon=target.iconCache.icon("profileScript.png"),
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
                icon=target.iconCache.icon("profileProject.png"),
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
                icon=target.iconCache.icon("debugScript.png"),
                text=target.tr('&Debug Script...'),
                shortcut=QKeySequence(target.tr('Debugger', 'F5')), 
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
                icon=target.iconCache.icon("debugProject.png"),
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
                icon=target.iconCache.icon("restart.png"),
                text=target.tr('Restart Script'),
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
                icon=target.iconCache.icon("stopScript.png"),
                text=target.tr('Stop Script'),
                shortcut=QKeySequence(target.tr('Shift+F10')), 
                objectName='dbg_stop_script', 
                statusTip=target.tr("Stop the running script."), 
                whatsThis=target.tr(
                """<b>Stop Script</b>"""
                """<p>This stops the script running in the debugger backend.</p>"""))
        target.dbgActions.append(target.stopAct)

        target.dbgActGrp = QActionGroup(self)

        target.dbgContAct = KyAction(\
                parent=target, 
                iconText=target.tr('Continue'),
                icon=target.iconCache.icon("continue.png"),
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
                parent=target,
                iconText=target.tr('Continue to Cursor'),
                icon=target.iconCache.icon("continueToCursor.png"),
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
                parent=target, 
                iconText=target.tr('Single Step'),
                icon=target.iconCache.icon("step.png"),
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
                parent=target, 
                iconText=target.tr('Step Over'),
                icon=target.iconCache.icon("stepOver.png"),
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
                parent=target, 
                iconText=target.tr('Step Out'),
                icon=target.iconCache.icon("stepOut.png"),
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
                parent=target, 
                iconText=target.tr('Stop'),
                icon=target.iconCache.icon("stepQuit.png"),
                text=target.tr('&Stop'),
                shortcut=QKeySequence(target.tr('F10')), 
                actionGroup=target.dbgActGrp,
                objectName='dbg_stop', 
                statusTip=target.tr('Stop debugging'))
        target.dbgStopAct.setWhatsThis(target.tr(
            """<b>Stop</b>"""
            """<p>Stop the running debugging session.</p>"""))
        target.dbgActions.append(target.dbgStopAct)
        
        target.dbgContextActGrp = QActionGroup(self)

        target.dbgEvalAct = KyAction(\
                parent=target,
                iconText=target.tr('Evaluate'),
                text=target.tr('E&valuate...'),
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
                parent=target, 
                iconText=target.tr('Execute'),
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
                text=target.tr('&Exceptions Filter...'), 
                objectName='dbg_exceptions_filter', 
                statusTip=target.tr('Configure exceptions filter'), 
                whatsThis=target.tr(
            """<b>Exceptions Filter</b>"""
            """<p>Configure the exceptions filter. Only exception types that are"""
            """ listed are highlighted during a debugging session.</p>"""
            """<p>Please note, that all unhandled exceptions are highlighted"""
            """ indepent from the filter list.</p>"""))
        target.dbgActions.append(target.dbgExcpIgnoreAct)
        
        target.dbgExcpIgnoreAct = KyAction(\
                parent=target, 
                iconText=target.tr('Ignored Exceptions'),
                text=target.tr('&Ignored Exceptions...'),
                objectName='dbg_ignored_exceptions', 
                statusTip=target.tr('Configure ignored exceptions'), 
                whatsThis=target.tr(
            """<b>Ignored Exceptions</b>"""
            """<p>Configure the ignored exceptions. Only exception types that are"""
            """ not listed are highlighted during a debugging session.</p>"""
            """<p>Please note, that unhandled exceptions cannot be ignored.</p>"""))
        target.dbgActions.append(target.dbgExcpIgnoreAct)

        target.dbgBpActGrp = QActionGroup(self)

        target.dbgToggleBpAct = KyAction(\
                parent=target,
                iconText=target.tr('Toggle Breakpoint'),
                icon=target.iconCache.icon("breakpointToggle.png"),
                text=target.tr('Toggle Breakpoint'), 
                shortcut=QKeySequence(target.tr("Shift+F11","Debug|Toggle Breakpoint")),
                actionGroup=target.dbgBpActGrp,
                objectName='dbg_toggle_breakpoint', 
                statusTip=target.tr('Toggle Breakpoint'))
        target.dbgToggleBpAct.setWhatsThis(target.tr(
            """<b>Toggle Breakpoint</b>"""
            """<p>Toggles a breakpoint at the current line of the"""
            """ current editor.</p>"""))
        target.dbgActions.append(target.dbgToggleBpAct)
        
        target.dbgEditBpAct = KyAction(\
                parent=target, 
                iconText=target.tr('Edit Breakpoint'),
                icon=target.iconCache.icon("cBreakpointToggle.png"),
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
                parent=target, 
                iconText=target.tr('Next Breakpoint'),
                icon=target.iconCache.icon("breakpointNext.png"),
                text=target.tr('Next Breakpoint'),
                shortcut=QKeySequence(target.tr('Debugger',
                        "Ctrl+Shift+PgDown","Debug|Next Breakpoint")),
                actionGroup=target.dbgBpActGrp, 
                objectName='dbg_next_breakpoint', 
                statusTip=target.tr('Next Breakpoint'))
        target.dbgNextBpAct.setWhatsThis(target.tr(
            """<b>Next Breakpoint</b>"""
            """<p>Go to next breakpoint of the current editor.</p>"""))
        target.dbgActions.append(target.dbgNextBpAct)

        target.dbgPrevBpAct = KyAction(\
                parent=target,
                iconText=target.tr('Previous Breakpoint'),
                icon=target.iconCache.icon("breakpointPrevious.png"),
                text=target.tr('Previous Breakpoint'),
                shortcut=QKeySequence(target.tr('Debugger', 
                        "Ctrl+Shift+PgUp","Debug|Previous Breakpoint")), 
                actionGroup=target.dbgBpActGrp, 
                objectName='dbg_previous_breakpoint', 
                statusTip=target.tr('Previous Breakpoint'), 
                whatsThis=target.tr(
            """<b>Previous Breakpoint</b>"""
            """<p>Go to previous breakpoint of the current editor.</p>"""))
        target.dbgActions.append(target.dbgPrevBpAct)

        target.dbgClrBpAct = KyAction(\
                parent=target, 
                iconText=target.tr('Clear Breakpoints'),
                text=target.tr('Clear Breakpoints'),
                shortcut=QKeySequence(target.tr('Debugger', 
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

    def __initMultiprojectActions(self):
        
        target.mpActGrp = QActionGroup(self)
        
        target.mpNewAct = KyAction(\
                parent=target, 
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
                parent=target,
                iconText=target.tr('Open Multiproject'),
                icon=target.iconCache.icon("multiProjectOpen.png"),
                text=target.tr('&Open...'),
                actionGroup=target.mpActGrp,
                objectName='multi_project_open', 
                statusTip=target.tr('Open an existing multiproject'), 
                whatsThis=target.tr(
                    """<b>Open...</b>"""
                    """<p>This opens an existing multiproject.</p>"""))
        target.mpActions.append(eslf.mpOpenAct)

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
                icon=target.iconCache.icon("fileProject.png"),
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
                icon=target.iconCache.icon("multiProjectProps.png"),
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
