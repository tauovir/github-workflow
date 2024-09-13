from setuptools import setup, find_packages
###
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Python Workflow Packages',
    version='1.0',
    description='Python package for source_scripts',
    author='khan',
    author_email='taukir707@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "source_scripts"},
    # packages=["source_scripts.aws_services", "source_scripts.components",
    #           "source_scripts.db", "source_scripts.configs", "source_scripts.exceptions"],
)