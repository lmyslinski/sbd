from setuptools import find_packages
from setuptools import setup

MAJOR_VERSION = '1'
MINOR_VERSION = '0'
MICRO_VERSION = '0'
VERSION = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)

setup(name='sbd',
      version=VERSION,
      description="Downloads safari online books for offline access",
      long_description="A python tool used for scraping html content from safari online pages."
                       " This tool is intended for personal offline storage only",
      author='Lukasz Myslinski',
      url='https://github.com/Humblehound',
      author_email='lukmyslinsi@gmail.com',
      install_requires=[
          'beautifulsoup4', 'lxml', 'mechanize', 'pdfkit'
      ],
      entry_points={
          'console_scripts': ['sbd= sbd.__main__:main']
      },
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Operating System :: Microsoft',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',

      ],
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      platforms='any')
