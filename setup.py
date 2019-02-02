# Scaffolding inspired on Kenneth Reitz's solution (https://github.com/kennethreitz/setup.py)

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='zelus',
    version='0.1.0',
    description='Raspberry Pi based pet camera web-server.',
    long_description=readme,
    author='Ricardo Silva',
    author_email='',
    url='https://github.com/ohCancio/zelus',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
