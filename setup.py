import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='stashy',
      version="0.6.1",
      description='Python API client for the Atlassian Stash REST API',
      long_description=read('README.rst'),
      url='http://github.com/tgates42/stashy',
      download_url = 'https://github.com/tgates42/stashy/archive/0.6.1.zip',
      author='Cosmin Stejerean',
      author_email='cosmin@offbytwo.com',
      license='Apache License 2.0',
      packages=['stashy', 'stashy.admin'],
      test_suite = 'tests',
      #scripts=['bin/stash'],
      #tests_require=open('test-requirements.txt').readlines(),
      install_requires=open('requirements.txt').readlines(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries'
        ]
     )
