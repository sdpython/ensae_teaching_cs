set path=%PATH%;%USERPROFILE%\AppData\Local\Pandoc
pandoc -t beamer cours_structure_donnee.txt -V theme:Warsaw -o cours_structure_donnee.pdf