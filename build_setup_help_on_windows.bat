rem we remove everything from dist
echo off
del /Q dist\*.*

rem unittests with python 3.4

IF EXIST c:\Python34vir GOTO next:
mkdir c:\Python34vir

:next:
IF EXIST c:\Python34vir\install GOTO fullsetup:
c:\Python34\Scripts\virtualenv c:\Python34vir\install --system-site-packages

:fullsetup:

echo #######################################################
c:\Python34vir\install\Scripts\python -u setup.py install
echo #######################################################

set pythonexe="c:\Python34\python"
%pythonexe% -u setup.py unittests
echo #######################################################

rem python 3.3

set pythonexe="c:\python33_x64\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py build bdist_wininst --plat-name=win-amd64
echo #######################################################

set pythonexe="c:\python33\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py sdist --formats=gztar,zip --verbose
%pythonexe% setup.py bdist_wininst
echo #######################################################

rem python 3.4

set pythonexe="c:\python34_x64\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py build bdist_wininst --plat-name=win-amd64
%pythonexe% setup.py build bdist_msi --plat-name=win-amd64
echo #######################################################

set pythonexe="c:\python34\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py sdist --formats=gztar,zip --verbose
%pythonexe% setup.py bdist_wininst
%pythonexe% setup.py bdist_msi
echo #######################################################

rem help

%pythonexe% -u setup.py build_sphinx
echo #######################################################

if not exist dist\html mkdir dist\html
xcopy /E /C /I /Y _doc\sphinxdoc\build\html dist\html


