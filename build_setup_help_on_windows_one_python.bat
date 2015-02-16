echo off
IF EXIST dist del /Q dist\*.*

set pythonexe=%1\python

:utpy34_64:
%pythonexe% -u setup.py clean_space
%pythonexe% setup.py clean_pyd
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u setup.py unittests
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

:setup34_x64_msi_wheel:
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

echo #######################################################F

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

:all_unit_tests:
%pythonexe% -u setup.py unittests
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################