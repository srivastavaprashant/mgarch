from distutils.core import setup
setup(
  name = 'mgarch',         
  packages = ['mgarch'],   
  version = '0.1.3',      
  license='MIT',    
  description = 'DCC-GARCH(1,1)',
  author = 'Prashant Srivastava',
  author_email = 'srivastava.prashant898@gmail.com',
  url = 'https://github.com/srivastavaprashant/mgarch',
  download_url = 'https://github.com/srivastavaprashant/mgarch/archive/0.1.3.tar.gz',
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