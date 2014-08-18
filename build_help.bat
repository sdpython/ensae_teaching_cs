rem we remove everything from dist
echo off

rem python 3.4

set pythonexe="c:\python34\python"
%pythonexe% clean_pyd.py

rem help

%pythonexe% -u setup.py build_pres
echo #######################################################

if not exist dist\html_pres mkdir dist\html_pres
xcopy /E /C /I /Y _doc\presentation\build\html dist\html_pres
