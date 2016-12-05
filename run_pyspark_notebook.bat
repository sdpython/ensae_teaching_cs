@echo off
if "%1"=="" goto default_value_spark:
set local_pyspark="%1"
goto custom_spark:
:default_value_spark:
set local_pyspark=c:\%USERNAME%\spark\spark-2.0.2-bin-hadoop2.7
:custom_spark:

if "%2"=="" goto default_value_python:
set local_python="%2"
goto custom_python:
:default_value_python:
set local_python=c:\Python35_x64
:custom_python:

set CURRENT=%~dp0

:update_path:
set HADOOP_HOME=%local_pyspark%
set SPARK_HOME=%local_pyspark%
set PATH=%local_python%;%local_python%\Scripts;%PATH%
set PATH=%PATH%;%local_pyspark%\bin
set PYSPARK_PYTHON=%local_python%\python
@echo HADOOP_HOME=%HADOOP_HOME%
@echo SPARK_HOME=%SPARK_HOME%
@echo PYSPARK_PYTHON=%PYSPARK_PYTHON%
set PYTHONPATH=%PYTHONPATH%;%current%\src;%current%\..\pyquickhelper\src;%current%\..\jyquickhelper\src;%current%\..\pymmails\src;%current%\..\pyensae\src;%current%\..\pyrsslocal\src;%current%\..\pymyinstall\src;%current%\..\mlstatpy\src
@echo PYTHONPATH=%PYTHONPATH%


:run_pyspark:
set PYSPARK_DRIVER_PYTHON=jupyter-notebook
if NOT EXIST %local_pyspark% @echo Not found: %local_pyspark%
pushd _doc\notebooks
%local_pyspark%\bin\pyspark.cmd
popd

