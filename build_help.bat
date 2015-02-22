rem we remove everything from dist
echo off

if "%1"=="" goto default_value:
set pythonexe="%1"
goto custom_python:

:default_value:
set pythonexe="c:\python34_x64\python"

:custom_python:
rem %pythonexe% clean_pyd.py


rem %pythonexe% -u setup.py build_pres
rem %pythonexe% -u setup.py build_pres_2A
rem %pythonexe% -u setup.py build_pres_3A
%pythonexe% -u setup.py build_pres_1Ap

if not exist dist\html_pres_3A mkdir dist\html_pres_3A
if not exist dist\html_pres_1Ap mkdir dist\html_pres_1Ap
rem xcopy /E /C /I /Y _doc\presentation_3A\build\html dist\html_pres_3A
xcopy /E /C /I /Y _doc\presentation_projets\a2015\build\html dist\html_pres_1Ap