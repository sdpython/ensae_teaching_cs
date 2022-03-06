# -*- coding: utf-8 -*-
import sys
import os
from setuptools import find_packages, setup
from pyquicksetup import read_version, read_readme, default_cmdclass

#########
# settings
#########

project_var_name = "ensae_teaching_cs"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'
history = "HISTORY.rst"

KEYWORDS = [project_var_name, 'ENSAE', 'teachings', 'Xavier Dupré']
DESCRIPTION = """Materials for teachings, notebooks, helpers..."""
CLASSIFIERS = [
    'Programming Language :: Python :: %d' % sys.version_info[0],
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Development Status :: 5 - Production/Stable'
]

#######
# data
#######

packages = find_packages('src', exclude='src')
package_dir = {k: "src/" + k.replace(".", "/") for k in packages}
package_data = {project_var_name + ".encrypted": ["*.crypted", "*.vigenere"],
                project_var_name + ".data.data_gutenberg": ["*.txt"],
                project_var_name + ".special.data": ["*.png", "*.txt"],
                project_var_name + ".data.data_1a": ["*.txt"],
                project_var_name + ".data.data_2a": ["*.csv"],
                project_var_name + ".data.data_sql": ["*.db", "*.zip"],
                project_var_name + ".data.data_web": ["*.csv", "*.zip"],
                project_var_name + ".data.data_competition": ["*.bin"],
                project_var_name + ".data.data_shp": ["*.csv"],
                project_var_name + ".data.zips": ["*.zip"],
                project_var_name + ".automation": ["*.xml", "*.r", "*.ico"],
                project_var_name: ["rss_teachings.xml"],
                }


setup(
    name=project_var_name,
    version=read_version(__file__, project_var_name, subfolder='src'),
    author='Xavier Dupré',
    author_email='xavier.dupre@gmail.com',
    license="MIT",
    url="http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html",
    download_url="https://github.com/sdpython/ensae_teaching_cs/",
    description=DESCRIPTION,
    long_description=read_readme(__file__),
    cmdclass=default_cmdclass(),
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
    setup_requires=["pyquicksetup"],
    install_requires=[
        "pyquickhelper>=1.10", "pyensae>=1.3",
        "pymyinstall", "pymmails>=0.3",
        "scikit-learn>=0.24", "pyrsslocal", "pandas>=1.0", "numpy", "pyenbc",
        "matplotlib", "jupyter", "mlstatpy", "manydataapi",
        "mlinsights>=0.3"],
)
