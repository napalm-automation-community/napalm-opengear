"""setup.py file."""

from setuptools import setup, find_packages

__author__ = 'Charlie Allom <charlie@evilforbeginners.com>'

with open("README.md", "r") as fh:
	long_description = fh.read()


def parse_reqs(file_path):
	"""Parse requirements from file."""
	with open(file_path, 'rt') as fobj:
		lines = map(str.strip, fobj)
		lines = filter(None, lines)
		lines = filter(lambda x: not x.startswith("#"), lines)
		return tuple(lines)


setup(
	name="napalm-opengear",
	version="0.3.0",
	packages=find_packages(),
	author="Charlie Allom",
	author_email="charlie@evilforbeginners.com",
	description="NAPALM driver for OpenGear Linux",
	long_description_content_type="text/markdown",
	long_description=long_description,
	classifiers=[
		'Topic :: Utilities',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.7',
		'Operating System :: POSIX :: Linux',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: MacOS',
	],
	url="https://github.com/yeled/napalm-opengear",
	include_package_data=True,
	install_requires=parse_reqs('requirements.txt'),
)
