#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 3

import os

class Consts():
  appname       = 'pacmanInfo'
  version_info  = (0, 1, 2)
  
  def __init__(self):
   
    # Paths
    self.PATHS = {}
    self.PATHS["root"]    = os.path.normpath(os.path.join(os.path.realpath(__file__), '..')) + os.path.sep
    self.PATHS["desktop"] = '/home/{}/.kde4/share/kde4/services/{}.desktop'
    self.PATHS["desktop"] = self.PATHS["desktop"].format(subprocess.getoutput("logname"), Consts.appname)
    

    self.PATHS["resources"] = {}
    self.PATHS["resources"]["directory"] = os.path.join(self.PATHS["root"], "resources" + os.path.sep)
    self.PATHS["resources"]["img"] = os.path.join(self.PATHS["resources"]["directory"], "img" + os.path.sep)
    self.PATHS["resources"]["css"] = os.path.join(self.PATHS["resources"]["directory"], "css" + os.path.sep)

    self.PATHS["tmp"] = {}
    self.PATHS["tmp"]["directory"] = os.path.join(self.PATHS["root"], "tmp" + os.path.sep)

    
  #@property
  def getVersion():
      return "{0}.{1}.{2}".format(Consts.version_info[0], Consts.version_info[1], Consts.version_info[2])
  #version = classmethod(getVersion)
