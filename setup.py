from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ohada/__init__.py
from ohada import __version__ as version

setup(
	name="ohada",
	version=version,
	description="All Ohada specific implementation",
	author="Richard Amouzou",
	author_email="dodziamouzou@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
