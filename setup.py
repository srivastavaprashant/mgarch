from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(

  name = 'mgarch',         
  packages = ['mgarch'],   
  version = '0.2.0',      
  license='MIT',    
  description = 'DCC-GARCH(1,1)',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 'Prashant Srivastava',
  author_email = 'srivastava.prashant898@gmail.com',
  url = 'https://github.com/srivastavaprashant/mgarch',
  download_url = 'https://github.com/srivastavaprashant/mgarch/archive/0.2.0.tar.gz',
  keywords = ['volatility', 'multivariate', 'garch'],
  install_requires=[
          'numpy',
          'scipy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
