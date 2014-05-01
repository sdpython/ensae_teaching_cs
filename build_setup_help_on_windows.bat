rem we remove everything from dist
echo off
del /Q dist\*.*

rem python 3.3

set pythonexe="c:\Python33_x64\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py build bdist_wininst --plat-name=win-amd64

set pythonexe="c:\Python33\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py sdist --formats=gztar,zip --verbose
%pythonexe% setup.py bdist_wininst

rem python 3.4

set pythonexe="c:\Python34_x64\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py build bdist_wininst --plat-name=win-amd64

set pythonexe="c:\Python34\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py sdist --formats=gztar,zip --verbose
%pythonexe% setup.py bdist_wininst

rem help

%pythonexe% -u make_help.py
if not exist dist\html mkdir dist\html
xcopy /E /C /I /Y _doc\sphinxdoc\build\html dist\html

if not exist dist\latex mkdir dist\latex
xcopy /E /C /I /Y _doc\sphinxdoc\build\latex dist\latex

if not exist dist\singlehtml mkdir dist\singlehtml
xcopy /E /C /I /Y _doc\sphinxdoc\build\latex dist\singlehtml
