#!/usr/bin/env python

"""
    GUI
"""

from api.consts import Consts


from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import (QApplication, QCheckBox, QDialog,
        QDialogButtonBox, QFrame, QGroupBox, QLabel, QLineEdit, QListWidget,
        QCommandLinkButton, QMessageBox,  
        QTabWidget, QVBoxLayout, QWidget)

from api.pacmantools import *
import os

import gettext
gettext.install(Consts.appname)

LABEL_STYLE=QFrame.Panel | QFrame.Sunken


class TabDialog(QDialog):
    """
        Fenetre principale
    """
    def __init__(self, repo, parent=None):
        super().__init__(parent)

        fileInfo = QFileInfo(repo.fileName)

        tabWidget = QTabWidget()
        
        tabWidget.addTab(repoTab(repo),         _("Repo"))
        tabWidget.addTab(ApplicationsTab(repo), _("Files"))
        tabWidget.addTab(GeneralTab(fileInfo),  _("File"))
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        
        '''
        key=RepoAttributes.URL.value
        if (key in repo.items):
            self.url=repo.items[key]
            self.urlbtn = QCommandLinkButton( self.url)
            self.urlbtn.clicked.connect(self.OnUrlMessage)
            #mainLayout.addWidget(self.urlbtn)
        '''
        
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle(repo.name)
        
    def OnUrlMessage(self):
        from PyQt5.QtGui import QDesktopServices
        from PyQt5.QtCore import QUrl
        reply = QMessageBox.information(self,
                "www", _('Open web')+'\n'+self.url)
        if reply == QMessageBox.Ok:
            QDesktopServices.openUrl(QUrl(self.url))


class GeneralTab(QWidget):
    def __init__(self, fileInfo, parent=None):
        super().__init__(parent)

        fileNameLabel = QLabel(_("File Name")+':')
        fileNameEdit  = QLineEdit(fileInfo.fileName())

        pathLabel      = QLabel(_("Path")+':')
        pathValueLabel = QLabel(fileInfo.absoluteFilePath())
        pathValueLabel.setFrameStyle(LABEL_STYLE)

        sizeLabel = QLabel(_("Size")+':')
        size = fileInfo.size() // 1024
        sizeValueLabel = QLabel("%d Ko" % size)
        sizeValueLabel.setFrameStyle(LABEL_STYLE)

        lastModLabel = QLabel(_("Last Modified")+':')
        lastModValueLabel = QLabel(fileInfo.lastModified().toString())
        lastModValueLabel.setFrameStyle(LABEL_STYLE)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(fileNameLabel)
        mainLayout.addWidget(fileNameEdit)
        mainLayout.addWidget(pathLabel)
        mainLayout.addWidget(pathValueLabel)
        mainLayout.addWidget(sizeLabel)
        mainLayout.addWidget(sizeValueLabel)
        mainLayout.addWidget(lastModLabel)
        mainLayout.addWidget(lastModValueLabel)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)
        
class repoTab(QWidget):
    """
        details du depot
    """
    def __init__(self, repo, parent=None):
        super().__init__(parent)

        mainLayout = QVBoxLayout()
        
        for key in RepoAttributes:
            try:
                value= repo.items[key.value]
                if (key==RepoAttributes.URL):
                    raise
            except:
                continue
            if len(value)>2:
                keyLabel = QLabel(key.value)
                if (key==RepoAttributes.name):
                    url=''
                    if (RepoAttributes.URL.value in repo.items):
                        url= 'href="'+repo.items[RepoAttributes.URL.value]+'"'
                    value= '<a {0}><b>{1}</b></a>'.format(url,value)
                
                value=self.setLabelValue(value, key)
                valueLabel = QLabel( value )
                if (key==RepoAttributes.name):
                    valueLabel.setOpenExternalLinks(True)
                valueLabel.setFrameStyle(LABEL_STYLE)
                mainLayout.addWidget(keyLabel)
                mainLayout.addWidget(valueLabel)
        
        deps=''
        for value in repo.deps: 
            deps +=value+'\n'
        if (len(deps)>2):
            keyLabel = QLabel(RepoAttributes.optionalDeps.value)
            valueLabel = QLabel( deps )
            valueLabel.setFrameStyle(LABEL_STYLE)
            mainLayout.addWidget(keyLabel)
            mainLayout.addWidget(valueLabel)
        
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)
        
    @staticmethod
    def setLabelValue(value, key=RepoAttributes.name):
        """
            format string if too many dep.
        """
        if  (key!=RepoAttributes.requiredBy) and \
            (key!=RepoAttributes.dependsOn):
            return value
        words= value.split()
        if len(words)<9:
            return value;
        ret=''
        i=0
        for word in words:
            ret +=word+' '
            i+=1
            if (i>7):
                i=0
                ret+= '\n'
        return ret



class ApplicationsTab(QWidget):
    """
        Liste des fichiers du depot
    """
    def __init__(self, repo, parent=None):
        super().__init__()
      
        topLabel = QLabel(_("files in repo")+':')
        applicationsListBox = QListWidget()
        applications = []
        
        applications = Pacman.Ql(repo.name)

        applicationsListBox.insertItems(0, applications)

        layout = QVBoxLayout()
        layout.addWidget(topLabel)
        layout.addWidget(applicationsListBox)
        self.setLayout(layout)

