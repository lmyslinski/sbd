from setuptools import find_packages
from setuptools import setup
import sbd

setup(name='sbd',
      version=sbd.__version__,
      description="Downloads safari online books for offline access",
      long_description="A python tool to convert Safari Books Online resources into PDF",
      author=sbd.__author__,
      author_email='lukmyslinski@gmail.com',
      url='https://github.com/Humblehound',
      download_url='https://github.com/Humblehound/sbd/tarball/0.1',
      install_requires=[
          'beautifulsoup4', 'lxml', 'mechanize', 'pdfkit', 'validators'
      ],
      entry_points={
          'console_scripts': [
              "sbd = sbd.__main__:main",
          ],
      },
      classifiers=[
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
      license=sbd.__license__,
      packages=find_packages(),
      zip_safe=False,
      platforms='any')
