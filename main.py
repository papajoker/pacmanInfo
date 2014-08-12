#!/usr/bin/env python

from api.consts import Consts

"""
for test en
    #srcipt LANG=en
    import locale
    locale.setlocale(locale.LC_ALL, 'C')

shell test:
    #LANG=fr_FR.UTF-8
    python ./main.py $(kdialog --getopenfilename /usr/share/sounds/ '*.* |tous fichiers' 2>/dev/null)
"""

from PyQt5.QtWidgets import (QApplication)

from gui.application import TabDialog
from api.pacmantools import *
import sys
import os
import argparse

import gettext
gettext.install(Consts.appname)

class App():
  def __init__(self):
    self.consts_ = Consts()
    self.repository = None
    self.fileName = ''
    
  def run():
    pass
  
  
  

def parseFile(filename):
    if (os.path.isfile(fileName)!=True):
        raise FileExistsError(_('File not found')+': "'+fileName+'"' )
  
    repoName= Pacman.Qo(fileName)
    return Repot( fileName, Pacman.Qi(repoName) )

def fileDesktop():
    PATH='/home/{}/.kde4/share/kde4/services/{}.desktop'
    return PATH.format(subprocess.getoutput("logname"),__appname__)

def setup():
    BASEDIR = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(BASEDIR, os.path.basename(__file__ ) )
    # 'ajout kde4 service menu'
    TXT='''[Desktop Entry]
        Actions={appname};
        Type=Service
        ServiceTypes=KonqPopupMenu/Plugin,all/allfiles
        X-KDE-Submenu=Pacman Actions
        X-KDE-Submenu[{lang}]={title}
        MimeType=all/allfiles
        
        [Desktop Action {appname}]
        Name=package info
        Name[{lang}]={subtitle}
        Exec={exe} "%f"
        '''
    TXT=TXT.format(exe=path, appname=__appname__, lang=_('en'), title=_('Pacman Actions'), subtitle=_('package info'))
    desktopFile = open(fileDesktop() , "w")
    desktopFile.write(TXT)
    desktopFile.close()

def unSetup():
    os.remove(fileDesktop())
    
    

def main(fileName,argv):
  app = None
  if ( not QApplication.instance() ):
      app = QApplication(argv)

  if ( app ):
      repot = parseFile(fileName)
      tabdialog = TabDialog(repot)
      print ('--- '+Consts.appname+', version: '+Consts.getVersion())
      tabdialog.show()
      return app.exec_()
  
  return 9



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", 			 	help="File from pacman")
    parser.add_argument("-dl",  "--dl",   action="store_true",	help=_('Dolphin link'))
    parser.add_argument("-du",  "--du",   action="store_true",	help=_('Dolphin unlink'))
    parser.add_argument("-t",   "--test", action="store_true",	help="for a Test not use file arg")
    parser.add_argument("-en",  "--en",   action="store_true",	help=_('force locale: en'))
    
    """
    TODO
      parser.add_argument("-ta",   "--tabaur",     action="store_true",	help=_('Tab aur'))
      parser.add_argument("-tf",   "--tabfiles",   action="store_true",	help=_('Tab files'))
      parser.add_argument("-tp",   "--tabbtn",     action="store_true",	help=_('Tab plus'))
      
      parser.add_argument("-tab",  "--tababout",   action="store_true",	help=_('Tab about'))
      parser.add_argument("-tc",   "--tabconfig",  action="store_true",	help=_('Tab Setup')) ?
    """
    args = parser.parse_args()
    
    if (args.dl):
        setup()
        sys.exit()
        
    if (args.du):
        unSetup()
        sys.exit()
        
    if (args.en):
        import locale
        locale.setlocale(locale.LC_ALL, 'C')
    
    if (args.file):
        fileName = args.file
        
    if (args.test):
        fileName = "/usr/share/applications/firefox.desktop"
        #fileName = "/usr/share/apps/autocorrect/fr.xml"
    
    sys.exit(main(fileName,sys.argv))
