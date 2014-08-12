#!/usr/bin/env python

"""
    pacman tools
    pacman datas structs
"""

from api.consts import Consts

import os
import subprocess

import gettext
gettext.install(Consts.appname)

from enum import Enum

class RepoAttributes(Enum):
    name          = _('Name')
    version       = _('Version')
    description   = _('Description')
    architecture  = _('Architecture')
    URL           = _('URL')
    licences      = _('Licences')
    groups        = _('Groups')
    provides      = _('Provides')
    dependsOn     = _('Depends On')
    optionalDeps  = _('Optional Deps.')
    requiredBy    = _('Required By')
    conflictsWith = _('Conflicts With')
    replaces      = _('Replaces')
    installedSize = _('Installed Size')
    #packager      = _('Packager')
    installDate   = _('Install Date')
    InstallReason = _('Install Reason')
    #scrit install, validate by
    

class Pacman:
    """
        run pacman
    """
    pacmanBin= '/usr/bin/pacman'
    
    def getQo(cls,fileName):
        "fichier appartient ou non a un paquet"
        out= cls.run('Qo',fileName)
        ret = out.split(' ')
        if (ret[0]==fileName):
            return ret[len(ret)-2]
        else:
            raise FileNotFoundError(_('File not found'))
    Qo = classmethod(getQo)

    def getQi(cls, repoName):
        "infos sur les attributs du paquet"
        return cls.run('Qi',repoName)
    Qi = classmethod(getQi)
    
    def getQl(cls, repoName):
        "liste des fichiers du paquet"
        out= cls.run('Ql',repoName)
        out= sorted(out.split('\n'))
        long=len(repoName)+1
        for i, elt in enumerate(out):
            out[i]=elt[long:]
        return out
    Ql = classmethod(getQl)
    
    def Qmq(cls, repoName):
        "AUR packages or other"
        return cls.run('Qml',repoName)
    Qml = sorted(classmethod(getQml))
    
    def run(cls,options,file):
        return subprocess.getoutput(Pacman.pacmanBin+' -'+options+' '+file)
    run = classmethod(run)
        

class Repot:
    """
        datas from -Qo
    """
    def __init__(self, fileName, pkginfo):
         self.name = ''
         self.fileName=fileName
         self.items = {}
         self.items[RepoAttributes.optionalDeps.value]=''
         self.deps=[]
         print (pkginfo+'\n')
         infos= pkginfo.split('\n')
         for line in infos: 
             items= line.split(' : ')
             items[0]=items[0].strip()
             if (len(items)==1):
                 self.deps.append(items[0].strip())
             if ((len(items)>1)and(items[1].strip()!='--')):
                 self.items[ items[0] ]= items[1].strip()
         self.name=self.items[_('Name')]
         self.deps.append(self.items[RepoAttributes.optionalDeps.value])
         del self.items[RepoAttributes.optionalDeps.value]

    
    @property
    def item(self, r = RepoAttributes.name):
        return self.items[RepoAttributes.optionalDeps.value]
    
    def toStr(self):
        ret=''
        for key in self.items: 
            ret +='['+key+'] : '+self.items[key]+'\n'
        deps=''
        for value in self.deps: 
            deps +='['+RepoAttributes.optionalDeps.value+'] : '+value.strip()+'\n'
        return ret+deps

