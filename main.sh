#! /bin/sh
#LANG=en
#LANG=fr_FR.UTF-8
python ./main.py $(kdialog --getopenfilename /usr/share/sounds/ '*.* |tous fichiers' 2>/dev/null)