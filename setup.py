from setuptools import setup
from setuptools import find_packages

setup(name='linkedin_parser',
      version='0.1.0',
      description='linkedin_parser_for_jobs',
      packages=find_packages('lib'),
      package_dir={'': 'lib'},
      author='Zhongshuai',
      license='NA',
      zip_safe=False)