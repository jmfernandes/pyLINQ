from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='pyLINQ',
      version='0.5.0',
      description='Makes filtering and sorting lists easier and more readable.',
      long_description=long_description,
      long_description_content_type='text/x-rst',
      url='https://github.com/jmfernandes/pyLINQ',
      author='Josh Fernandes',
      author_email='joshfernandes@mac.com',
      keywords=['LINQ', 'list', 'list comprehension' ,'lambda', 'utility', 'C#', 'where', 'set', 'filter', 'sort'],
      license='MIT',
      python_requires='>=3.4',
      packages=find_packages(),
      requires=[],
      install_requires=[
      ],
      zip_safe=False)
