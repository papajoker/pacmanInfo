Par un clic droit dans dolphin, avoir la possibilité de savoir rapidement a quel dépôt un fichier appartient et d'avoir le détail du dépôt

**Python3 et QT 5**
ne fonctionne que en `fr` et `en` sous `pyQt5`

j'ai fait un paquet (aur) mais je ne l'ai pas déclaré; il faut donc une install a la main :
téléchargement du paquet (aur) sur : 
[e-nautia.com](https://e-nautia.com/manjarofrance/disk/espace%20upload/InfoPacmanAsSu.kde/pacmanInfo-0.1.0-1-any.pkg.tar.xz)

puis en ligne de commande :
```[bash]
sudo pacman -U ~/Téléchargements/pacmanInfo-0.1.0-1-any.pkg.tar.xz
(ou) yaourt -U ~/Téléchargements/pacmanInfo-0.1.0-1-any.pkg.tar.xz```

pour un petit test en ligne de commande:
```[bash]
/usr/share/pacmanInfo/main.py $(kdialog --getopenfilename /usr/share/sounds/ '*.* |tous fichiers' 2>/dev/null)
/usr/share/pacmanInfo/main.py /etc/rc.local```

ou avec Dolphin par clic droit sur un fichier "*Pacman Administration*"