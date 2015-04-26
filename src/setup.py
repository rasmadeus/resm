from setuptools import setup, find_packages
from os.path import join, dirname
import resm

setup(
    name='resm',
    version=resm.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    install_requires=['Flask==0.10.1']
)