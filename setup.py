from setuptools import setup, find_namespace_packages

setup(name="anuradatamodel", version="1.0", packages=find_namespace_packages(where='generated'), package_dir={"": "generated"})
