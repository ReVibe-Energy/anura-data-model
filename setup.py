from setuptools import setup, find_namespace_packages

setup(name="anuradatamodel", version="0.1", packages=find_namespace_packages(where='generated'), package_dir={"": "generated"})
