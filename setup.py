from distutils.command import install_lib
from lib2to3.pygram import python_symbols
from platform import python_version
from setuptools import setup,find_packages
# every folder with "__init__" considered as package
# packages=find_packages()
setup(version='major.minor.patch',
author='Nitesh'

author_email='mail',
long_description='long description',
description='description',
packages=['yourpackage'],
name='lib_name',
install_requires=['external packages','pandas','dvc']
python_version='>=3.7'
)
 # pip install wheel
 # python setup.py sdist bdist_wheel
 # pip install ./pkg.wheel