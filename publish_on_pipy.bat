if "%1"=="" goto default_value:
set path=%path%;%1;%1\Scripts
goto custom_python:

:default_value:
set path=%path%;c:\Python34;c:\Python34\Scripts

:custom_python:
%pythonexe% setup.py sdist register upload