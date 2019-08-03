
from setuptools import setup, find_packages
from os import path

version = '1.2.0'
repo = 'soch-ugc-py'

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'sochugc',
  packages = find_packages(),
  install_requires=['requests', 'ksamsok'],
  python_requires='>=3.5.0',
  version = version,
  description = 'API library for the cultural heritage K-Samsök (SOCH) UGC API.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Albin Larsson',
  author_email = 'albin.post@gmail.com',
  url = 'https://github.com/Abbe98/' + repo,
  download_url = 'https://github.com/Abbe98/' + repo + '/tarball/' + version,
  keywords = ['SOCH', 'K-Samsök', 'heritage', 'cultural', 'API', 'UGC'],
  license='MIT',
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3 :: Only',
    'Intended Audience :: Developers',
    'Intended Audience :: Education'
  ]
)
