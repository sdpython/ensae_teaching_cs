export pythonexe=$HOME/anaconda3/bin/python

echo #######################################################
$pythonexe setup.py unittests
echo #######################################################
$pythonexe clean_pyd.py
$pythonexe setup.py sdist --formats=gztar,zip --verbose
echo #######################################################
$pythonexe -u setup.py build_sphinx
echo #######################################################

if [ -f dist/html ] ; then
    mkdir dist/html
fi
rsync -ra _doc/sphinxdoc/build/html/* dist/html