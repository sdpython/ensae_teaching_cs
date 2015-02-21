if "%1"=="" goto default_value:
set path=%path%;%1;%1\Scripts
goto custom_python:

:default_value:
set path=%path%;c:\Python34_x64;c:\Python34_x64\Scripts

:custom_python:
ipython3 notebook --notebook-dir=_doc\notebooks
rem ipython3 help notebook