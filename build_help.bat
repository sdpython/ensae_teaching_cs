IF EXIST dist del /Q dist\*.*

if "%1"=="" goto setup34_x64_msi_wheel:
set pythonexe="%1"
%pythonexe% setup.py write_version
goto custom_python:

:setup34_x64_msi_wheel:
set pythonexe="c:\Python34_x64\python"
:custom_python:
%pythonexe% -u setup.py build_sphinx
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

:copyfiles:
if not exist dist\html mkdir dist\html
xcopy /E /C /I /Y _doc\sphinxdoc\build\html dist\html
if exist _doc\sphinxdoc\build\latex xcopy /E /C /I /Y _doc\sphinxdoc\build\latex\*.pdf dist\html
if %errorlevel% neq 0 exit /b %errorlevel%
xcopy /E /C /I /Y _doc\sphinxdoc\build2\html dist\html2
if %errorlevel% neq 0 exit /b %errorlevel%
xcopy /E /C /I /Y _doc\sphinxdoc\build3\html dist\html3
if %errorlevel% neq 0 exit /b %errorlevel%