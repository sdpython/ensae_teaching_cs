echo off

if "%1"=="" goto default_value:
set pythonexe="%1"
goto utpy34_64:

:default_value:
set pythonexe="c:\Python34_x64\python"

:utpy34_64:
%pythonexe% -u setup.py clean_space
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u setup.py unittests_all
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################