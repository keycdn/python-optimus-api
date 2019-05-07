import setuptools
from distutils.core import setup

setup(
  name = 'optimus-api',
  packages = ['optimus'],
  version = '0.4.2',
  description = 'A Python API client for the Optimus image optimization service',
  long_description = open('README.md').read(),
  long_description_content_type = 'text/markdown',
  author = 'KeyCDN',
  url = 'https://github.com/keycdn/python-optimus-api',
  keywords = [
    'image compression',
    'image optimization',
    'image optimizer',
    'optimus'
  ],
  classifiers=[
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3'
  ],
  install_requires=[
    'requests>=2.11.1',
  ],
)
