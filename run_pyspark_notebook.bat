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

:hive:
if NOT EXIST \tmp mkdir \tmp
if NOT EXIST \tmp\hive mkdir \tmp\hive

:update_path:
set HADOOP_HOME=%local_pyspark%
set SPARK_HOME=%local_pyspark%
set PATH=%local_python%;%local_python%\Scripts;%PATH%
set PATH=%PATH%;%local_pyspark%\bin
set PYSPARK_PYTHON=%local_python%\python
set SPARK_HIVE=true

@echo HADOOP_HOME=%HADOOP_HOME%
@echo PYTHONPATH=%PYTHONPATH%
@echo PYSPARK_PYTHON=%PYSPARK_PYTHON%
@echo SPARK_HIVE=%SPARK_HIVE%
@echo SPARK_HOME=%SPARK_HOME%
set PYTHONPATH=%PYTHONPATH%;%current%\src;%current%\..\pyquickhelper\src;%current%\..\jyquickhelper\src;%current%\..\pymmails\src;%current%\..\pyensae\src;%current%\..\pyrsslocal\src;%current%\..\pymyinstall\src;%current%\..\mlstatpy\src

:wintutils:
winutils.exe chmod -R 777 \tmp\hive
winutils.exe ls \tmp\hive

:run_pyspark:
set PYSPARK_DRIVER_PYTHON=jupyter-notebook
if NOT EXIST %local_pyspark% @echo Not found: %local_pyspark%
pushd _doc\notebooks
%local_pyspark%\bin\pyspark.cmd
popd

