echo off

:utpy34_64:
set pythonexe="c:\Python34_x64\python"
%pythonexe% -u setup.py clean_space
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u setup.py unittests
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################