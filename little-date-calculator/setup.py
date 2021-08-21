#!/usr/bin/env python3
import os
import io
from setuptools import setup, find_packages

# Make sure we're actually in the directory containing setup.py.
root_dir = os.path.dirname(__file__)

if root_dir != "":
    os.chdir(root_dir)

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


with open('requirements.txt') as reqs:
    install_requires = [
        line for line in reqs.read().split('\n') if (line and not
                                                     line.startswith('--'))
    ]

setup(name='little-date-calculator',
      version='0.0.1',
      description='My little date calculator',
      long_description=read('README.md'),
      author='Danny Zhong',
      author_email='zho.danny@gmail.com',
      url='',
      packages=find_packages(exclude='tests'),
      include_package_data=True,
      install_requires=install_requires,
      entry_points={
          'console_scripts': [
              'little-date-calculator = little_date_calculator.main:main'
          ]
      },

      classifiers=[
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: Other/Proprietary License",
          "Natural Language :: English",
          "Operating System :: Unix",
          "Programming Language :: Python",
          "Topic :: Software Development",
      ]
      )
