# This file lies in the same level as of the pyhton package. This file is necessary for the pip installing. pip will automatically look for this file.
# This file contains the information/metadata about the package
# To make it locally available in the given environment, goto cmd terminal in the same level as the package and setup, and type, "pip install ."
# To remove the package from the environment, goto the cmd terminal and type "pip uninstall pkg_name"
# package manager will automatically look for the setup.py file and will make this package available in the same python environment


from setuptools import setup

setup(
    name='arithmetic',  # Every pacage in the index needs to be unique
    version='0.1',
    description='Gaussian distribution',
    packages=['arithmetic'],
    author='Sharan Jaiswal',
    author_email='sharanjaiswal12@gmail.com',
    zip_safe=False  # This makes sure that the package can't be run directly from the zip file
                    # This is necessary if the package relies on the data files that need to remain unzipped for use
    )