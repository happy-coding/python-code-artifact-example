import os

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'README.md')) as f:
    README = f.read()

setup(
    name='my-hot-shit',
    long_description=README,
    version='1.0.0',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    packages=['rare', 'tests'],
    url='https://medium.com/@rare',
    license='MIT',
    author='medium rare',
    author_email='',
    description='This rare python package will be stored in AWS CodeArtifact'
)
