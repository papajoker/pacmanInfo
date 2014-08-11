#! /bin/sh

#tar cvjf pacmanInfo-0.1.0.tar.gz ./pacmanInfo
mv pacmanInfo.tar.gz pacmanInfo-0.1.0.tar.gz
echo 'changer le md5sum du fichier PKGBUILD '
md5sum pacmanInfo-0.1.0.tar.gz | cut -d ' ' -f 1

echo 'faire un upload du fichier .tar.gz puis:'
echo 'makepkg'