if "%1"=="" goto default_value:
set pythonexe=%1\python
goto custom_python:

:default_value:
set pythonexe=c:\Python34_x64\python

:custom_python:
%pythonexe% setup.py rotate --match=.zip --keep=1
%pythonexe% setup.py rotate --match=.tar.gz --keep=3
rem %pythonexe% setup.py sdist register
%pythonexe% setup.py sdist --formats=gztar upload