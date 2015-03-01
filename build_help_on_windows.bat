echo off
IF EXIST dist del /Q dist\*.*

if "%1"=="" goto default_value:
set pythonexe="%1"
goto presentation:

:default_value:
set pythonexe="c:\python34_x64\python"

:presentation:
%pythonexe% -u setup.py build_pres
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u setup.py build_pres_2A
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u setup.py build_pres_3A
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u setup.py build_pres_1Ap
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

:documentation:
%pythonexe% -u setup.py build_sphinx
if %errorlevel% eq 0 goto sphinx_no_error:
set errorlevel=0
rem we do a second run to go around the error
rem ImportError: No module named 'ensae_teaching_cs.faq'
rem which disappear after a second run
echo --------- SECOND RUN -----------
echo --------- SECOND RUN -----------
echo --------- SECOND RUN -----------
echo --------- SECOND RUN -----------
echo --------- SECOND RUN -----------
%pythonexe% -u setup.py build_sphinx
:sphinx_no_error:
echo --------- ERRORS? -----------
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

:copyfiles:
if not exist dist\html mkdir dist\html
if not exist dist\html2 mkdir dist\html2
if not exist dist\html3 mkdir dist\html3
if not exist dist\latex mkdir dist\latex
if not exist dist\html_pres mkdir dist\html_pres
if not exist dist\html_pres_2A mkdir dist\html_pres_2A
if not exist dist\html_pres_3A mkdir dist\html_pres_3A
if not exist dist\html_pres_1Ap mkdir dist\html_pres_1Ap

echo #######################################################F

xcopy /E /C /I /Y _doc\presentation_projets\a2015\build\html dist\html_pres_1Ap
if %errorlevel% neq 0 exit /b %errorlevel%
xcopy /E /C /I /Y _doc\presentation_2A\build\html dist\html_pres_2A
if %errorlevel% neq 0 exit /b %errorlevel%
xcopy /E /C /I /Y _doc\presentation_3A\build\html dist\html_pres_3A
if %errorlevel% neq 0 exit /b %errorlevel%
xcopy /E /C /I /Y _doc\presentation\build\html dist\html_pres
if %errorlevel% neq 0 exit /b %errorlevel%
xcopy /E /C /I /Y _doc\sphinxdoc\build\html dist\html
if %errorlevel% neq 0 exit /b %errorlevel%
xcopy /E /C /I /Y _doc\sphinxdoc\build2\html dist\html2
if %errorlevel% neq 0 exit /b %errorlevel%
xcopy /E /C /I /Y _doc\sphinxdoc\build3\html dist\html3
if %errorlevel% neq 0 exit /b %errorlevel%
xcopy /E /C /I /Y _doc\sphinxdoc\build\latex dist\latex
if %errorlevel% neq 0 exit /b %errorlevel%