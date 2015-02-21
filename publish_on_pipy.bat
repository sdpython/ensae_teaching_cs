if "%1"=="" goto default_value:
set pythonexe=%1\python
goto custom_python:

:default_value:
set pythonexe=c:\Python34\python

:custom_python:
%pythonexe% setup.py sdist register upload