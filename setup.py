from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cbpi4-GroupedActor',
      version='0.0.5',
      description='CraftBeerPi Plugin',
      author='Alexander VOllkopf',
      author_email='avollkopf@web.de',
      url='https://github.com/avollkopf/cbpi4-GroupedActor',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-GroupedActor': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-GroupedActor'],

	  long_description=long_description,
	  long_description_content_type='text/markdown'
     )
