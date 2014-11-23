export pythonexe=$HOME/anaconda3/bin/python
export PYTHONPATH=$PYTHONPATH:../../src:../../../pymyinstall/src:../../../pyquickhelper/src:../../../pyensae/src
export PYTHONPATH=$PYTHONPATH:../../../src:../../../../pymyinstall/src:../../../../pyquickhelper/src:../../../../pyensae/src
ipython notebook --notebook-dir=_doc/notebooks
