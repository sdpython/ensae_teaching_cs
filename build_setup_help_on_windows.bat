rem we remove everything from dist
echo off
del /Q dist\*.*

rem unittests with python 3.4

IF EXIST c:\Python34vir GOTO next:
mkdir c:\Python34vir

:next:
IF EXIST c:\Python34vir\install GOTO fullsetup:
c:\Python34\Scripts\virtualenv c:\Python34vir\install --system-site-packages
if %errorlevel% neq 0 exit /b %errorlevel%

:fullsetup:

echo #######################################################
c:\Python34vir\install\Scripts\python -u setup.py install
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

set pythonexe="c:\Python34\python"
%pythonexe% -u setup.py clean_space
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u setup.py unittests
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

rem python 3.3

set pythonexe="c:\python33_x64\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py build bdist_wininst --plat-name=win-amd64
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

set pythonexe="c:\python33\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py sdist --formats=gztar,zip --verbose
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% setup.py bdist_wininst
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

rem python 3.4

set pythonexe="c:\python34_x64\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py build bdist_wininst --plat-name=win-amd64
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% setup.py build bdist_msi --plat-name=win-amd64
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

set pythonexe="c:\python34\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py sdist --formats=gztar,zip --verbose
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% setup.py bdist_wininst
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% setup.py bdist_msi
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

rem help

%pythonexe% -u setup.py build_pres
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u setup.py build_pres_2A
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u setup.py build_pres_3A
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u setup.py build_sphinx
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

if not exist dist\html mkdir dist\html
if not exist dist\html2 mkdir dist\html2
if not exist dist\html3 mkdir dist\html3
if not exist dist\latex mkdir dist\latex
if not exist dist\html_pres mkdir dist\html_pres
if not exist dist\html_pres_2A mkdir dist\html_pres_2A
if not exist dist\html_pres_3A mkdir dist\html_pres_3A

xcopy /E /C /I /Y _doc\presentation_2A\build\html dist\html_pres_2A
if %errorlevel% neq 0 exit /b %errorlevel%
xcopy /E /C /I /Y _doc\presentation_3A\build\html dist\html_pres_3A
if %errorlevel% neq 0 exit /b %errorlevel%
xcopy /E /C /I /Y _doc\presentation\build\html dist\html_pres
if %errorlevel% neq 0 exit /b %errorlevel%
xcopy /E /C /I /Y _doc\sphinxdoc\build\html dist\html
if %errorlevel% neq 0 exit /b %errorlevel%
xcopy /E /C /I /Y _doc\sphinxdoc\build2\html dist\html2
if %errorlevel% neq 0 exit /b %errorlevel%
xcopy /E /C /I /Y _doc\sphinxdoc\build3\html dist\html3
if %errorlevel% neq 0 exit /b %errorlevel%
xcopy /E /C /I /Y _doc\sphinxdoc\build\latex dist\latex
if %errorlevel% neq 0 exit /b %errorlevel%