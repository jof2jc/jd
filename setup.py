# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

#with open('requirements.txt') as f:
#	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in jd/__init__.py
#from jd import __version__ as version

setup(
	name='jd',
	version='1.0',
	description='JDID Open API',
	author='Jonathan',
	author_email='jof2jc@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[]#install_requires
)

