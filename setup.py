from distutils.command import install_lib
from lib2to3.pygram import python_symbols
from platform import python_version
from setuptools import setup,find_packages
# every folder with "__init__" considered as package
# packages=find_packages()
setup(version='0.0.1',


author='Nitesh',

author_email='mail',
long_description='long description',
description='description',
packages=['src'],
name='lib_name',
install_requires=['pandas','dvc'],
python_version='>=3.7'
)
 # pip install wheel
 # python setup.py sdist bdist_wheel
 # pip install ./pkg.wheel
 # a stage without dependencies in dvc.yaml file will always run
 # you can see in dvc.lock file that all the components in a stage like outs,deps etc if you see a md5 over there which means that stage is being tracked
 