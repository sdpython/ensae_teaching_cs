
@echo off
@echo SCRIPT: windows_notebook
if "%1"=="" goto default_value:
if "%1"=="default" goto default_value:
set pythonexe=%1
goto nextn:

:default_value:
@echo ~LABEL default_value
set pythonexe=c:\Python35_x64
@echo ~SET pythonexe=c:\Python35_x64

:nextn:
@echo ~LABEL nextn
set current=%~dp0

set current=%~dp0
if EXIST %current%setup.py goto current_is_setup:
set current=%current%..\
cd ..
if EXIST %current%setup.py goto current_is_setup:
@echo Unable to find %current%setup.py
exit /b 1

:current_is_setup:
@echo ~SET current=%current%

set path=%path%;%pythonexe%;%pythonexe%\Scripts
@echo ~SET path=%path%;%pythonexe%;%pythonexe%\Scripts
@echo ~CALL jupyter-notebook --notebook-dir=..
set PYTHONPATH=%PYTHONPATH%;%current%\src;%current%\..\pyquickhelper\src;%current%\..\jyquickhelper\src;%current%\..\pymmails\src;%current%\..\pyensae\src;%current%\..\pyrsslocal\src;%current%\..\pymyinstall\src;%current%\..\mlstatpy\src
@echo ~SET PYTHONPATH=%PYTHONPATH%;%current%\src;%current%\..\pyquickhelper\src;%current%\..\jyquickhelper\src;%current%\..\pymmails\src;%current%\..\pyensae\src;%current%\..\pyrsslocal\src;%current%\..\pymyinstall\src;%current%\..\mlstatpy\src
jupyter-notebook --notebook-dir=..