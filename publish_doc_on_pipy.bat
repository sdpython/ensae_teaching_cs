if "%1"=="" goto default_value:
set pythonexe=%1\python
goto custom_python:

:default_value:
set pythonexe=c:\Python34_x64\python

:custom_python:
%pythonexe% setup.py upload_docs --upload-dir=dist/html