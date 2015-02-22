echo off
IF EXIST dist del /Q dist\*.*

if "%1"=="" goto default_value:
set pythonexe="%1"
goto custom_python:

:default_value:
IF NOT EXIST c:\Python34 GOTO checkinstall64:

:checkinstall:
IF EXIST c:\Python34vir GOTO nexta:
mkdir c:\Python34vir

:nexta:
IF EXIST c:\Python34vir\install GOTO fullsetupa:
c:\Python34\Scripts\virtualenv c:\Python34vir\install --system-site-packages
if %errorlevel% neq 0 exit /b %errorlevel%
:fullsetupa:
echo #######################################################
c:\Python34vir\install\Scripts\python -u setup.py install
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

:checkinstall64:
IF EXIST c:\Python34_64vir GOTO nextb:
mkdir c:\Python34_64vir
:nextb:
echo #######################################################
c:\Python34_x64\Scripts\virtualenv c:\Python34_64vir\install --system-site-packages
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

:fullsetupb:
echo #######################################################
c:\Python34_64vir\install\Scripts\python -u setup.py install
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

:setup33:
IF NOT EXIST c:\Python33 GOTO setup33_64:
set pythonexe="c:\Python33\python"
%pythonexe% setup.py clean_pyd
%pythonexe% setup.py bdist_wininst
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

:setup33_64:
IF NOT EXIST c:\Python33_x64 GOTO setup34:
set pythonexe="c:\Python33_x64\python"
%pythonexe% setup.py clean_pyd
%pythonexe% setup.py sdist --formats=gztar,zip --verbose
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% setup.py build bdist_wininst --plat-name=win-amd64
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

:setup34:
IF NOT EXIST c:\Python34 GOTO setup34_x64_msi_wheel:
set pythonexe="c:\Python34\python"
%pythonexe% setup.py clean_pyd
%pythonexe% setup.py build bdist_wininst --plat-name=win-amd64
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

:setup34_x64_msi_wheel:
set pythonexe="c:\Python34_x64\python"
:custom_python:
%pythonexe% -u setup.py clean_space
%pythonexe% setup.py clean_pyd
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u setup.py unittests
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

%pythonexe% setup.py sdist --formats=gztar,zip --verbose
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% setup.py bdist_wininst --plat-name=win-amd64
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% setup.py bdist_msi
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% setup.py bdist_wheel
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

:presentation:
%pythonexe% -u setup.py build_pres
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u setup.py build_pres_2A
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u setup.py build_pres_3A
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u setup.py build_pres_1Ap
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

:documentation:
%pythonexe% -u setup.py build_sphinx
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

:copyfiles:
if not exist dist\html mkdir dist\html
if not exist dist\html2 mkdir dist\html2
if not exist dist\html3 mkdir dist\html3
if not exist dist\latex mkdir dist\latex
if not exist dist\html_pres mkdir dist\html_pres
if not exist dist\html_pres_2A mkdir dist\html_pres_2A
if not exist dist\html_pres_3A mkdir dist\html_pres_3A
if not exist dist\html_pres_1Ap mkdir dist\html_pres_1Ap

echo #######################################################F

xcopy /E /C /I /Y _doc\presentation_projets\a2015\build\html dist\html_pres_1Ap
if %errorlevel% neq 0 exit /b %errorlevel%
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