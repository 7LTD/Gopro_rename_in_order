@echo off

:: Definir en utf-8 pour utilisation de caractères spéciaux
chcp 65001 > nul

:: Récupérer le répertoire du script .bat
set "script_dir=%~dp0"

:: Changer de répertoire de travail vers le répertoire du script
cd /d "C:\LE DOSSIER OU EST RANGE rengopro.py"

echo on

python "rengopro.py" "%script_dir%"
pause