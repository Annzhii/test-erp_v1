from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erp_v1/__init__.py
from erp_v1 import __version__ as version

setup(
	name="erp_v1",
	version=version,
	description="ERP_V1",
	author="Anzhi",
	author_email="juananzhi@hotmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
