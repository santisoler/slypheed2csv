"""
Build and install the project.
"""
from setuptools import setup, find_packages


NAME = "slypheed2csv"
FULLNAME = "Slypheed to CSV"
AUTHOR = "Santiago Soler"
AUTHOR_EMAIL = "santiago.r.soler@gmail.com"
MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL
LICENSE = "MIT License"
URL = "https://github.com/santisoler/slypheed2csv"
DESCRIPTION = "Convert Slypheed address book to a CSV file"
KEYWORDS = "slypheed addressbook csv".split()
VERSION = "0.0.1"
PLATFORMS = "Any"
PACKAGES = find_packages()
ENTRY_POINTS = {"console_scripts": "slypheed2csv = slypheed2csv.slypheed2csv:main"}
PACKAGE_DATA = {}
#  with open("requirements.txt") as f:
#      INSTALL_REQUIRES = f.readlines()
PYTHON_REQUIRES = ">=3.6"

if __name__ == "__main__":
    setup(
        name=NAME,
        fullname=FULLNAME,
        description=DESCRIPTION,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        license=LICENSE,
        url=URL,
        platforms=PLATFORMS,
        entry_points=ENTRY_POINTS,
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        keywords=KEYWORDS,
        #  install_requires=INSTALL_REQUIRES,
        python_requires=PYTHON_REQUIRES,
    )
